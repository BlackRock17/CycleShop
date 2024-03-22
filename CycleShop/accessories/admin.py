from django.contrib import admin
from .models import Accessories


@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "quantity",)
    list_editable = ("quantity",)
    list_filter = ("category",)
    search_fields = ("name",)



