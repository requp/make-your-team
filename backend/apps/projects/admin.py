from django.contrib import admin
from rangefilter.filters import DateRangeFilter

import apps.projects.models as project_models


@admin.action(
    permissions=["change"],
    description="Mark selected projects/technology names as published"
)
def make_published(_model_admin, _request, queryset):
    queryset.update(is_published=True)


@admin.action(
    permissions=["change"],
    description="Mark selected projects/technology names as unpublished"
)
def make_unpublished(_model_admin, _request, queryset):
    queryset.update(is_published=False)


@admin.register(project_models.Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin panel for Project model"""
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ("title",)
    autocomplete_fields = ["technology_stack", ]
    search_help_text = "You can search by project's title"
    actions = [make_published, make_unpublished]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "title",
                    "description",
                    "icon",
                    "is_published",
                    "technology_stack",
                    "start_date",
                    "end_date"
                ],
            },
        ),
        (
            "Other options",
            {
                "classes": ["collapse"],
                "fields": ["slug"],
            },
        ),
    ]


    list_display = ["title", "start_date", "end_date", "is_published"]
    list_filter = [
        "is_published",
        ("start_date", DateRangeFilter),
        ("end_date", DateRangeFilter),
        ("created_at", DateRangeFilter)
    ]


@admin.register(project_models.TechnologyName)
class TechnologyNameAdmin(admin.ModelAdmin):
    """Admin panel for TechnologyName model"""
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

    fieldsets = [
        (
            None,
            {
                "fields": ["name", "icon"],
            },
        ),
        (
            "Other options",
            {
                "classes": ["collapse"],
                "fields": ["slug", "description"],
            },
        ),
    ]