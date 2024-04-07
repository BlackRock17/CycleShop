from django.contrib import admin

from .models import (
    MountainBicycle, RoadBicycle, ElectricBicycle
)
from ..images.admin import ProductImageInline


class BicycleTypeFilter(admin.SimpleListFilter):
    title = "Bicycle Type"
    parameter_name = "bicycle_type"

    def lookups(self, request, model_admin):
        return (
            ("mountainbicycle", "Mountain Bicycle"),
            ("roadbicycle", "Road Bicycle"),
            ("electricbicycle", "Electric Bicycle")
        )

    def queryset(self, request, queryset):
        if self.value() == "mountainbicycle":
            return queryset.filter(bicycle__mountainbicycle__isnull=False)
        elif self.value() == "roadbicycle":
            return queryset.filter(bicycle__roadbicycle__isnull=False)
        elif self.value() == "electricbicycle":
            return queryset.filter(bicycle__electricbicycle__isnull=False)


class BaseBicycleAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "size", "tyres_size", "quantity")
    list_editable = ("quantity",)
    list_filter = ("category", "size", "tyres_size")
    search_fields = ("name",)
    inlines = [ProductImageInline]


@admin.register(MountainBicycle)
class MountainBicycleAdmin(BaseBicycleAdmin):
    pass


@admin.register(RoadBicycle)
class RoadBicycleAdmin(BaseBicycleAdmin):
    pass


@admin.register(ElectricBicycle)
class ElectricBicycleAdmin(BaseBicycleAdmin):
    pass


