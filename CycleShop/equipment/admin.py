from django.contrib import admin

from CycleShop.equipment.models import Goggles, Gloves, Helmet, Protection
from CycleShop.images.admin import ProductImageInline


@admin.register(Goggles)
class GogglesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)
    inlines = [ProductImageInline]


@admin.register(Gloves)
class GlovesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)
    inlines = [ProductImageInline]


@admin.register(Helmet)
class HelmetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)
    inlines = [ProductImageInline]


@admin.register(Protection)
class ProtectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)
    inlines = [ProductImageInline]
