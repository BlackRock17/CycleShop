from django.apps import apps
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Cart, CartItem


def get_product_image(product):
    image_fields = ["bicycle_images", "accessory_images", "components_images", "equipment_images"]

    for field in image_fields:
        if hasattr(product, field):
            images = getattr(product, field)
            if images.exists():
                return images.first()

    return None


def add_to_cart(request, product_type, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    app_label, model_name = product_type.split(".")
    product_model = apps.get_model(app_label, model_name)
    product = product_model.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product_type=product_type,
        product_id=product_id,
        defaults={"price": product.price},
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    if product.quantity > 0:
        product.quantity -= 1
        product.save()
    else:
        pass

    return redirect("cart")


def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()

    if not cart_items:
        return render(request, "cart/empty_cart.html")

    for item in cart_items:
        product = item.get_product()
        if product:
            item.image = get_product_image(product)

    total_price = sum(item.price * item.quantity for item in cart_items)
    context = {"cart_items": cart_items, "total_price": total_price}
    return render(request, "cart/cart.html", context)


def update_cart_item(request, item_id):
    if request.method == "POST":
        cart_item = CartItem.objects.get(id=item_id)
        new_quantity = int(request.POST.get("quantity"))

        if new_quantity > cart_item.quantity:
            product = cart_item.get_product()
            if product.quantity >= new_quantity - cart_item.quantity:
                product.quantity -= new_quantity - cart_item.quantity
                product.save()
                cart_item.quantity = new_quantity
                cart_item.save()
            else:
                messages.error(request, f"Insufficient quantity for {product.name}. Available: {product.quantity}")

        else:
            product = cart_item.get_product()
            product.quantity += cart_item.quantity - new_quantity
            product.save()
            cart_item.quantity = new_quantity
            cart_item.save()

    return redirect("cart")


def delete_cart_item(request, item_id):
    if request.method == "POST":
        cart_item = CartItem.objects.get(id=item_id)
        product = cart_item.get_product()
        product.quantity += cart_item.quantity
        product.save()
        cart_item.delete()

    return redirect("cart")


def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()

    for item in cart_items:
        item.delete()

    return render(request, "cart/checkout.html")
