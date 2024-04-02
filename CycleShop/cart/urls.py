from django.urls import path
from CycleShop.cart.views import cart_view, add_to_cart, update_cart_item, delete_cart_item, checkout

urlpatterns = (
    path("add-to-cart/<str:product_type>/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("", cart_view, name="cart"),
    path("update_cart_item/<int:item_id>/", update_cart_item, name="update_cart_item"),
    path("delete_cart_item/<int:item_id>/", delete_cart_item, name="delete_cart_item"),
    path("checkout/", checkout, name="checkout"),
)
