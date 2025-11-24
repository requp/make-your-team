from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.projects import views as project_views
from apps.members import views as member_views
router = routers.DefaultRouter()


router.register(r"products", project_views.ProjectViewSet, basename="projects")

urlpatterns = [
    re_path(
            route='^auth/users/(?!me$)(?P<username>[a-zA-Z0-9._@-]{4,150})/$',
            view=member_views.MemberAPIView.as_view(),
            name='member-detail'
        ),
    re_path(r'^auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls)),

]