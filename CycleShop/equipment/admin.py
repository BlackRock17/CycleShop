from django.contrib import admin

from CycleShop.equipment.models import Goggles, Gloves, Helmet, Protection, EquipmentImage


class EquipmentImageInline(admin.TabularInline):
    model = EquipmentImage
    extra = 1


@admin.register(Goggles)
class GogglesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [EquipmentImageInline]


@admin.register(Gloves)
class GlovesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [EquipmentImageInline]


@admin.register(Helmet)
class HelmetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [EquipmentImageInline]


@admin.register(Protection)
class ProtectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    inlines = [EquipmentImageInline]
