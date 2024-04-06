from django.db import models
from CycleShop.accounts.models import CycleShopUser


class Order(models.Model):
    MAX_TOTAL_PRICE_DIGITS = 8
    MAX_DECIMAL_PLACES = 2
    MAX_SHIPPING_ADDRESS_LENGTH = 150

    total_price = models.DecimalField(
        max_digits=MAX_TOTAL_PRICE_DIGITS,
        decimal_places=MAX_DECIMAL_PLACES,
    )

    shipping_address = models.CharField(
        max_length=MAX_SHIPPING_ADDRESS_LENGTH,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    user = models.ForeignKey(
        CycleShopUser,
        on_delete=models.CASCADE
    )


class OrderItem(models.Model):
    MAX_PRODUCT_TYPE_LENGTH = 100
    MAX_PRICE_DIGITS = 10
    MAX_DECIMAL_PLACES = 2

    product_type = models.CharField(
        max_length=MAX_PRODUCT_TYPE_LENGTH
    )

    product_id = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=MAX_PRICE_DIGITS,
        decimal_places=MAX_DECIMAL_PLACES
    )
    quantity = models.PositiveIntegerField()

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
