from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("email", "first_name", "last_name", "phone_number")},
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ("username", "password1", "password2", "is_staff", "is_active")},
        ),
    )


admin.site.register([Profile])
