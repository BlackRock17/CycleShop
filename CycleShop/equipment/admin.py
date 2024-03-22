from django.contrib import admin

from CycleShop.equipment.models import Goggles, Gloves, Helmet, Protection


@admin.register(Goggles)
class GogglesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)


@admin.register(Gloves)
class GlovesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)


@admin.register(Helmet)
class HelmetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)


@admin.register(Protection)
class ProtectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', "size", "quantity")
    list_filter = ("category", "size",)
    search_fields = ("name",)
