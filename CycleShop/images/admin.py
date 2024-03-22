from django.contrib import admin
from .models import ProductImage


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1
    fields = ['image']


admin.site.register(ProductImage)


