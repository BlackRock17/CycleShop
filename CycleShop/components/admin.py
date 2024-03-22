from django.contrib import admin

from CycleShop.components.models import Components


@admin.register(Components)
class ComponentsAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "quantity")
    list_editable = ("quantity",)
    list_filter = ("type",)
    search_fields = ("name", "type")

