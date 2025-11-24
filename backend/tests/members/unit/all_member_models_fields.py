from django.db.models import fields

from apps.members import models as member_models

ALL_SKILL_FIELDS = {
    "id": {
        "field_type": fields.BigAutoField,
    },
    "name": {
        "field_type": fields.CharField,
        "max_length": 100,
    },
    "description": {
        "field_type": fields.TextField,
        "max_length": 500,
        "blank": True,
        "null": True,
    },
    "icon": {
        "field_type": fields.files.ImageField,
        "upload_to": "skill_icons/",
        "blank": True,
        "null": True,
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


ALL_MEMBER_FIELDS = {
    "id": {
        "field_type": fields.BigAutoField,
    },
    "username": {
        "field_type": fields.CharField,
        "max_length": 32,
    },
    "email": {
        "field_type": fields.EmailField,
        "max_length": 254,
        "unique": True,
    },
    "password": {
        "field_type": fields.CharField,
        "max_length": 128,
    },
    "first_name": {
        "field_type": fields.CharField,
        "max_length": 150,
        "blank": True,
        "null": False,
    },
    "last_name": {
        "field_type": fields.CharField,
        "max_length": 150,
        "blank": True,
        "null": False,
    },
    "last_login": {
        "field_type": fields.DateTimeField,
        "auto_now_add": False,
        "auto_now": False,
        "blank": True,
        "auto_created": False,
    },
    "bio": {
        "field_type": fields.TextField,
        "max_length": 300,
        "blank": True,
        "null": True,
    },
    "profile_pic": {
        "field_type": fields.files.ImageField,
        "upload_to": "member_pics/"
    },
    "is_superuser": {
        "field_type": fields.BooleanField,
        "default": False
    },
    "is_active": {
        "field_type": fields.BooleanField,
        "default": True
    },
    "is_staff": {
        "field_type": fields.BooleanField,
        "default": False
    },
    "is_verified": {
        "field_type": fields.BooleanField,
        "default": False
    },
    "phone_number": {
        "field_type": fields.CharField,
        "blank": True,
        "null": True,
    },
    "date_joined": {
        "field_type": fields.DateTimeField,
        "auto_now_add": False,
        "auto_now": False,
        "auto_created": False,
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

ALL_MEMBER_MODELS_TO_CHECK = (
    (member_models.Skill, ALL_SKILL_FIELDS),
    (member_models.Member, ALL_MEMBER_FIELDS),
)
