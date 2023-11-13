from django.contrib import admin

from .models import User
from .forms import UserCreationForm

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["uid", "first_name", "last_name","username", "phone"]
    fieldsets = (
        (None, {"fields": ("phone", "password", "new_password")}),
        (
            "Other",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "image",
                    "uid",
                    "slug",
                )
            },
        ),
        (
            "User Permission",
            {
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_verified",
                    "is_active",
                )
            },
        ),
        ("Groups and Permissions", {"fields": ("groups", "user_permissions")}),
    )
    list_filter = [
        "is_superuser",
        "is_staff",
        "user_type",
    ]
    search_fields = (
        "phone",
        "username",
    )
    readonly_fields = ("password", "uid", "slug")
    form = UserCreationForm
    ordering = ("-created_at",)
