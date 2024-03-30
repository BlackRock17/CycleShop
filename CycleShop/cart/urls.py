from django.urls import path
from CycleShop.cart.views import cart_view, add_to_cart

urlpatterns = (
    path('add-to-cart/<str:product_type>/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path("", cart_view, name='cart'),
)
