from django.apps import apps
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem


def add_to_cart(request, product_type, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    app_label, model_name = product_type.split('.')
    product_model = apps.get_model(app_label, model_name)
    product = product_model.objects.get(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product_type=product_type,
        product_id=product_id
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    if product.quantity > 0:
        product.quantity -= 1
        product.save()
    else:
        pass

    return redirect('cart')


def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    context = {'cart_items': cart_items}
    return render(request, 'cart/cart.html', context)
