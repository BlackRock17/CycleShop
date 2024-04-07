from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from CycleShop.accounts.models import CycleShopUser, Profile


@admin.register(CycleShopUser)
class CycleShopUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active",)
    list_filter = ("is_staff", "is_active", "groups",)
    search_fields = ("username", "first_name", "last_name", "email",)
    ordering = ("username",)
   
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2"),
        }),
    )


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = _("Profile")
    fk_name = "user"


class ProfileAdmin(CycleShopUserAdmin):
    inlines = (ProfileInline,)
    list_display = ("username", "get_email", "get_first_name", "get_last_name", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"), }),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def get_email(self, obj):
        return obj.profile.email
    get_email.short_description = "Email"

    def get_first_name(self, obj):
        return obj.profile.first_name
    get_first_name.short_description = "First Name"

    def get_last_name(self, obj):
        return obj.profile.last_name
    get_last_name.short_description = "Last Name"

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)


admin.site.unregister(CycleShopUser)
admin.site.register(CycleShopUser, ProfileAdmin)
