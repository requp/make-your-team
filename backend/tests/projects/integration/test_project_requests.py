from rest_framework import status

from tests.projects.conftest import *
from django.urls import reverse
from rest_framework.test import APIClient
from apps.projects import serializers as project_serializers
client = APIClient()


def _add_test_url_to_data(
        data: dict | list, field_name: str, uri_name: str, many: bool = False
) -> None:
    """Add "http://testserver" to every fixture uri, because response data get a full url path"""
    if not many:
        data = [data]
    for field_dict in data:
        for item in field_dict[field_name]:
            item[uri_name] = "http://testserver" + item[uri_name]


class TestProjectRequests:
    def test_positive_project_list_request(self, project_queryset_fixture):
        response = client.get(path=reverse("projects-list"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == PROJECT_AMOUNT_FIXTURE

        serializer = project_serializers.ProjectSerializerBase(project_queryset_fixture, many=True)
        assert serializer.data == response.data


    def test_positive_project_detail_request(self, project_queryset_fixture):
        project = project_queryset_fixture[0]
        response = client.get(path=reverse(viewname="projects-detail", args=[project.slug]))
        assert response.status_code == status.HTTP_200_OK

        serializer = project_serializers.ProjectSerializerBase(project)
        assert serializer.data == response.data


    def test_not_exist_project_detail_request(self, project_queryset_fixture):
        response = client.get(path=reverse(viewname="projects-detail", args=["some-random-slug-5345535"]))
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"].code == "not_found"
