from rest_framework import serializers
from apps.projects import models as project_models


class TechnologyNameMiniSerializer(serializers.ModelSerializer):
    """Technology name serializer for a project serializer"""
    class Meta:
        model = project_models.TechnologyName
        fields = ("id", "name")


class ProjectSerializerBase(serializers.ModelSerializer):
    """Project model serializer"""
    technology_stack = TechnologyNameMiniSerializer(read_only=True, many=True)
    class Meta:
        model = project_models.Project
        fields = "__all__"