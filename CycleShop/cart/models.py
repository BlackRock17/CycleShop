from django.apps import apps
from django.contrib.auth.models import User
from django.db import models


class Cart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class CartItem(models.Model):
    MAX_PRODUCT_TYPE_LENGTH = 100
    MAX_PRICE_DIGITS = 10
    MAX_DECIMAL_PLACES_DIGITS = 2

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )

    product_type = models.CharField(
        max_length=MAX_PRODUCT_TYPE_LENGTH
    )

    product_id = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=MAX_PRICE_DIGITS,
        decimal_places=MAX_DECIMAL_PLACES_DIGITS,
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    def get_product(self):
        try:
            app_label, model_name = self.product_type.split(".")
            model = apps.get_model(app_label, model_name)
            return model.objects.get(id=self.product_id)
        except (LookupError, model.DoesNotExist):
            return None
