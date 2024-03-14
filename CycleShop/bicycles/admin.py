from django.contrib import admin
from .models import (
    MountainBicycle, RoadBicycle, ElectricBicycle, BicycleInventory, Bicycle
)


class BicycleInventoryInline(admin.TabularInline):
    model = BicycleInventory
    extra = 1


@admin.register(MountainBicycle)
class MountainBicycleAdmin(admin.ModelAdmin):
    inlines = [BicycleInventoryInline]


@admin.register(RoadBicycle)
class RoadBicycleAdmin(admin.ModelAdmin):
    inlines = [BicycleInventoryInline]


@admin.register(ElectricBicycle)
class ElectricBicycleAdmin(admin.ModelAdmin):
    pass


@admin.register(BicycleInventory)
class BicycleInventoryAdmin(admin.ModelAdmin):
    list_display = ('bicycle', 'size', 'quantity')
    list_editable = ('quantity',)
    list_filter = ('size', 'quantity')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(quantity__gt=0)
        return qs


