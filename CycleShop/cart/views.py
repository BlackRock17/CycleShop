from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Cart, CartItem
from ..accounts.forms import CheckoutForm
from ..accounts.models import Profile
from ..common.models import Order, OrderItem
from ..core.helpers import get_product_image


@login_required
def add_to_cart(request, product_type, product_id):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        app_label, model_name = product_type.split(".")
        product_model = apps.get_model(app_label, model_name)
        product = product_model.objects.get(id=product_id)

        if product.quantity > 0:
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product_type=product_type,
                product_id=product_id,
                defaults={"price": product.price},
            )

            if not created:
                cart_item.quantity += 1
                cart_item.save()

            product.quantity -= 1
            product.save()
            return redirect("cart")
        else:
            messages.error(request, f"Insufficient quantity for {product.name}")
            return redirect("cart")
    else:
        return redirect(f"/accounts/login/?next={request.path}")


@login_required
def cart_view(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.cartitem_set.all()

        if not cart_items:
            return render(request, "cart/empty_cart.html")

        for item in cart_items:
            product = item.get_product()
            if product:
                item.image = get_product_image(product)

        total_price = sum(item.price * item.quantity for item in cart_items)
        total_price_formatted = f"Total Price: ${total_price:.2f}"
        context = {"cart_items": cart_items, "total_price": total_price_formatted}
        return render(request, "cart/cart.html", context)
    else:
        return redirect(f"/accounts/login/?next={request.path}")


@login_required
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


@login_required
def delete_cart_item(request, item_id):
    if request.method == "POST":
        cart_item = CartItem.objects.get(id=item_id)
        product = cart_item.get_product()
        product.quantity += cart_item.quantity
        product.save()
        cart_item.delete()

    return redirect("cart")


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()

    profile = Profile.objects.filter(user=request.user).first()

    if not profile or not all(
            [profile.first_name, profile.last_name, profile.email, profile.town, profile.address, profile.postcode]):
        return redirect(reverse("profile_edit", kwargs={"pk": profile.pk}) + "?next=" + request.path)

    if request.method == "POST":
        form = CheckoutForm(request.POST, user=request.user)
        if form.is_valid():
            profile.first_name = form.cleaned_data['full_name'].split()[0]
            profile.last_name = ' '.join(form.cleaned_data['full_name'].split()[1:])
            profile.email = form.cleaned_data['email']
            profile.town = form.cleaned_data['town']
            profile.address = form.cleaned_data['address']
            profile.postcode = form.cleaned_data['postcode']
            profile.save()

            total_price = sum(item.price * item.quantity for item in cart_items)
            shipping_address = form.cleaned_data["address"]
            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                shipping_address=shipping_address
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product_type=item.product_type,
                    product_id=item.product_id,
                    price=item.price,
                    quantity=item.quantity
                )

            cart_items.delete()
            return render(request, "cart/checkout_success.html", {"order": order})
    else:
        form = CheckoutForm(user=request.user)

    context = {'form': form, 'cart_items': cart_items}

    return render(request, "cart/checkout.html", context)
