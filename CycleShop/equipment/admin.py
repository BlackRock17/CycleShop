from django.contrib import admin

from CycleShop.equipment.models import Goggles, Gloves, Helmet, Protection
from CycleShop.images.admin import ProductImageInline


class BaseEquipmentAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


@admin.register(Goggles)
class GogglesAdmin(BaseEquipmentAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)


@admin.register(Gloves)
class GlovesAdmin(BaseEquipmentAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)


@admin.register(Helmet)
class HelmetAdmin(BaseEquipmentAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)


@admin.register(Protection)
class ProtectionAdmin(BaseEquipmentAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)
