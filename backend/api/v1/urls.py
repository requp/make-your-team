from django.urls import path, include
from rest_framework import routers
from apps.projects import views as project_views
router = routers.DefaultRouter()


router.register(r"products", project_views.ProjectViewSet, basename="projects")

urlpatterns = [
    path("", include(router.urls)),
]