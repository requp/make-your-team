from django.db.models import fields

from apps.projects import models as project_models

ALL_TECHNOLOGY_NAME_FIELDS = {
    "id": {
        "field_type": fields.BigAutoField,
    },
    "name": {
        "field_type": fields.CharField,
        "max_length": 100,
    },
    "description": {
        "field_type": fields.TextField,
        "max_length": 1000,
    },
    "icon": {
        "field_type": fields.files.ImageField,
        "upload_to": "technology_icons/"
    },
    "slug": {
        "field_type": fields.SlugField,
        "max_length": 100,
        "unique": True,
        "db_index": True
    },
    "is_published": {
        "field_type": fields.BooleanField,
        "default": True
    },
    "created_at": {
        "field_type": fields.DateTimeField,
        "auto_now_add": True,
    },
    "updated_at": {
        "field_type": fields.DateTimeField,
        "auto_now": True,
    }
}


ALL_PROJECT_FIELDS = {
    "id": {
        "field_type": fields.BigAutoField,
    },
    "title": {
        "field_type": fields.CharField,
        "max_length": 100,
    },
    "description": {
        "field_type": fields.TextField,
        "max_length": 1000,
        "null": True,
        "blank": True,
    },
    "icon": {
        "field_type": fields.files.ImageField,
        "upload_to": "project_icons/",
        "null": True,
        "blank": True,
    },
    "slug": {
        "field_type": fields.SlugField,
        "max_length": 100,
        "unique": True,
        "db_index": True
    },
    "is_published": {
        "field_type": fields.BooleanField,
        "default": False
    },
    "start_date": {
        "field_type": fields.DateField,
    },
    "end_date": {
        "field_type": fields.DateField,
    },
    "created_at": {
        "field_type": fields.DateTimeField,
        "auto_now_add": True,
    },
    "updated_at": {
        "field_type": fields.DateTimeField,
        "auto_now": True,
    }
}

ALL_PROJECT_MODELS_TO_CHECK = (
    (project_models.TechnologyName, ALL_TECHNOLOGY_NAME_FIELDS),
    (project_models.Project, ALL_PROJECT_FIELDS),
)
