from django.contrib import admin
from apps.members import models as members_models
from rangefilter.filters import DateRangeFilter

@admin.register(members_models.Member)
class MemberAdmin(admin.ModelAdmin):
    """Admin panel for Member model"""
    search_fields = ("username", "first_name", "last_name", "email", "phone_number")

    autocomplete_fields = ["skills", ]
    search_help_text = "You can search by member's username, email, first_name, last_name or phone_number"
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "profile_pic",
                    "is_active",
                    "is_verified",
                    "skills",
                    "password",
                ],
            },
        ),
        (
            "Other options",
            {
                "classes": ["collapse"],
                "fields": ["is_superuser", "bio"],
            },
        ),
    ]


    list_display = ["username", "is_active", "is_verified", "email", "first_name", "last_name"]
    list_filter = [
        "is_active",
        "is_superuser",
        "is_verified",
        ("created_at", DateRangeFilter)
    ]


@admin.register(members_models.Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin panel for Skill model"""
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    search_help_text = "You can search by skill's name"

    fieldsets = [
        (
            None,
            {
                "fields": ["name"],
            },
        ),
        (
            "Other options",
            {
                "classes": ["collapse"],
                "fields": ["slug", "description", "icon", "is_published"],
            },
        ),
    ]

    list_display = ["name", "is_published", "slug"]