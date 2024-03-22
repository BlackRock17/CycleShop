from django.contrib import admin

from .models import (
    MountainBicycle, RoadBicycle, ElectricBicycle
)
from ..images.admin import ProductImageInline


class BicycleTypeFilter(admin.SimpleListFilter):
    title = 'Bicycle Type'
    parameter_name = 'bicycle_type'

    def lookups(self, request, model_admin):
        return (
            ('mountainbicycle', 'Mountain Bicycle'),
            ('roadbicycle', 'Road Bicycle'),
            ('electricbicycle', 'Electric Bicycle')
        )

    def queryset(self, request, queryset):
        if self.value() == 'mountainbicycle':
            return queryset.filter(bicycle__mountainbicycle__isnull=False)
        elif self.value() == 'roadbicycle':
            return queryset.filter(bicycle__roadbicycle__isnull=False)
        elif self.value() == "electricbicycle":
            return queryset.filter(bicycle__electricbicycle__isnull=False)


class BaseBicycleAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


@admin.register(MountainBicycle)
class MountainBicycleAdmin(BaseBicycleAdmin):
    list_display = ('name', 'category')


@admin.register(RoadBicycle)
class RoadBicycleAdmin(BaseBicycleAdmin):
    list_display = ('name', 'category')


@admin.register(ElectricBicycle)
class ElectricBicycleAdmin(BaseBicycleAdmin):
    list_display = ('name', 'category')


