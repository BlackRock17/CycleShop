from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import ProductImage


class ProductImageInline(GenericTabularInline):
    model = ProductImage
    extra = 1


