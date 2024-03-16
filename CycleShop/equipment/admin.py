from django.contrib import admin

from CycleShop.equipment.models import Goggles, Gloves, Helmet, Protection, EquipmentInventory, EquipmentImage


class EquipmentInventoryFilter(admin.SimpleListFilter):
    title = "Equipment Type"
    parameter_name = "equipment_type"

    def lookups(self, request, model_admin):
        return (
            ("goggles", "Goggles"),
            ("gloves", "Gloves"),
            ("helmet", "Helmet"),
            ("protection", "Protection"),
        )

    def queryset(self, request, queryset):
        if self.value() == "goggles":
            return queryset.filter(equipment__goggles__isnull=False)
        elif self.value() == "gloves":
            return queryset.filter(equipment__gloves__isnull=False)
        elif self.value() == "helmet":
            return queryset.filter(equipment__helmet__isnull=False)
        elif self.value() == "protection":
            return queryset.filter(equipment__protection__isnull=False)

class EquipmentInventoryInline(admin.TabularInline):
    model = EquipmentInventory
    extra = 1


class EquipmentImageInline(admin.TabularInline):
    model = EquipmentImage
    extra = 1


@admin.register(Goggles)
class GogglesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [EquipmentInventoryInline, EquipmentImageInline]


@admin.register(Gloves)
class GlovesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [EquipmentInventoryInline, EquipmentImageInline]


@admin.register(Helmet)
class HelmetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [EquipmentInventoryInline, EquipmentImageInline]


@admin.register(Protection)
class ProtectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [EquipmentInventoryInline, EquipmentImageInline]


@admin.register(EquipmentInventory)
class EquipmentInventoryAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'category', 'size', 'quantity')
    list_editable = ('quantity',)
    list_filter = (EquipmentInventoryFilter, 'size',)
    search_fields = ('equipment__name',)

    def category(self, obj):
        if hasattr(obj.equipment, 'goggles'):
            return obj.equipment.goggles.category
        elif hasattr(obj.equipment, 'gloves'):
            return obj.equipment.gloves.category
        elif hasattr(obj.equipment, 'helmet'):
            return obj.equipment.helmet.category
        elif hasattr(obj.equipment, "protection"):
            return obj.equipment.protection.category
        return '-'
