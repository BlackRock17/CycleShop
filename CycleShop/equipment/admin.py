from django.contrib import admin

from CycleShop.equipment.models import Goggles, Gloves, Helmet, Protection
from CycleShop.images.admin import ProductImageInline


class BaseEquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "size", "quantity")
    list_editable = ("quantity",)
    list_filter = ("category", "size",)
    search_fields = ("name",)
    inlines = [ProductImageInline]


@admin.register(Goggles)
class GogglesAdmin(BaseEquipmentAdmin):
    pass


@admin.register(Gloves)
class GlovesAdmin(BaseEquipmentAdmin):
    pass


@admin.register(Helmet)
class HelmetAdmin(BaseEquipmentAdmin):
    pass


@admin.register(Protection)
class ProtectionAdmin(BaseEquipmentAdmin):
    pass
