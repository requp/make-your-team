from rest_framework import viewsets
from apps.projects import serializers as project_serializers
from apps.projects import models as project_models


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        project_models.Project.objects.filter(is_published=True)
        .prefetch_related("technology_stack")
    )
    serializer_class = project_serializers.ProjectSerializerBase
    lookup_field = "slug"
