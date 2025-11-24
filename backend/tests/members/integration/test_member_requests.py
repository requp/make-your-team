from rest_framework import status

from tests.members.conftest import *
from django.urls import reverse
from rest_framework.test import APIClient
from apps.members import serializers as member_serializers
client = APIClient()

class TestMemberCreateRequest:
    def test_positive_full_member_create_request(
            self, correct_full_member_data_fixture
    ):
        """Test should create a new member object with all text fields possible"""
        response = client.post(path=reverse("member-list"), data=correct_full_member_data_fixture)
        assert response.status_code == status.HTTP_201_CREATED

        serializer = member_serializers.MemberCreateSerializer(correct_full_member_data_fixture)
        assert response.data == serializer.data


    def test_positive_min_member_create_request(
            self, correct_minimum_member_data_fixture,
    ):
        """Test should create a new member object with required minimum fields"""
        response = client.post(path=reverse("member-list"), data=correct_minimum_member_data_fixture)
        assert response.status_code == status.HTTP_201_CREATED

        assert response.data["username"] == correct_minimum_member_data_fixture["username"]
        assert response.data["email"] == correct_minimum_member_data_fixture["email"]


    def test_without_repass_member_data(
            self, without_repass_member_data_fixture,
    ):
        """Test should return 400 Bad Request with a lack of re_password"""
        response = client.post(path=reverse("member-list"), data=without_repass_member_data_fixture)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert response.data["re_password"][0] == "This field is required."


    def test_without_username_member_data(
            self, without_username_member_data_fixture,
    ):
        """Test should return 400 Bad Request with a lack of username"""
        response = client.post(path=reverse("member-list"), data=without_username_member_data_fixture)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert response.data["username"][0] == "This field is required."


    def test_without_email_member_data(
            self, without_email_member_data_fixture,
    ):
        """Test should return 400 Bad Request with a lack of email"""
        response = client.post(path=reverse("member-list"), data=without_email_member_data_fixture)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert response.data["email"][0] == "This field is required."


    def test_with_not_equal_passwords_member_data(
            self, with_not_equal_passwords_member_data_fixture,
    ):
        """Test should return 400 Bad Request with not equal passwords"""
        response = client.post(path=reverse("member-list"), data=with_not_equal_passwords_member_data_fixture)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        assert response.data["re_password"][0] == "The two password fields didn't match."


class TestMemberUpdateRequest:
    def test_positive_member_update_request_by_me(self, member_fixture):
        """Test should change text fields of a given member object by action 'me'"""
        data = {
            "first_name": "SomeName",
            "last_name": "SomeLastName",
            "bio": "SomeBio",
            "username": "SomeUsername",
        }
        # Check that changing data is not equal to the current member object's data
        for key, value in data.items():
            assert member_fixture.__dict__[key] != value
        client.force_authenticate(user=member_fixture)
        response = client.put(path=reverse(viewname="member-me"), data=data)
        assert response.status_code == status.HTTP_200_OK

        # Check that changing data is equal to the current member object's data after an update request
        member_fixture.refresh_from_db()
        for key, value in data.items():
            assert member_fixture.__dict__[key] == value


    def test_positive_member_update_request_by_own_id(self, member_fixture):
        """Test should change text fields of a given member object by the object's id"""
        data = {
            "first_name": "SomeName",
            "last_name": "SomeLastName",
            "bio": "SomeBio",
            "username": "SomeUsername",
        }
        # Check that changing data is not equal to the current member object's data
        for key, value in data.items():
            assert member_fixture.__dict__[key] != value
        client.force_authenticate(user=member_fixture)
        response = client.put(path=reverse(viewname="member-detail", args=[member_fixture.id]), data=data)
        assert response.status_code == status.HTTP_200_OK

        # Check that changing data is equal to the current member object's data after an update request
        member_fixture.refresh_from_db()
        for key, value in data.items():
            assert member_fixture.__dict__[key] == value


    def test_taken_username_update_request(self, member_queryset_fixture):
        """Test should return 400 Bad Request because username is taken"""
        member1 = member_queryset_fixture[0]
        member2 = member_queryset_fixture[1]
        assert member1.username != member2.username
        client.force_authenticate(user=member1)
        response = client.put(path=reverse(viewname="member-me"), data={"username": member2.username})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["username"][0] == "Current username is taken."

        assert member1.username != member2.username
        
    def test_member_update_request_by_other_id(self, member_queryset_fixture):
        """Test should return 404 because of other member's id"""
        data = {
            "first_name": "SomeName",
            "last_name": "SomeLastName",
            "bio": "SomeBio",
        }
        member1 = member_queryset_fixture[0]
        member2 = member_queryset_fixture[1]
        # Check that changing data is not equal to other member object's data
        for key, value in data.items():
            assert member2.__dict__[key] != value
        client.force_authenticate(user=member1)
        response = client.put(path=reverse(viewname="member-detail", args=[member2.id]), data=data)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.status_text == "Not Found"

        # Check that changing data is not equal to the other member object's data after an update request
        member1.refresh_from_db()
        for key, value in data.items():
            assert member1.__dict__[key] != value

    def test_positive_skill_update_request(self, member_queryset_fixture, skill_fixture):
        #TODO Add tests to skill updating
        pass


class TestMemberGetRequest:
    def test_positive_member_get_request_by_own_user_id(self, member_queryset_fixture):
        """Test should return a member object by its own id"""
        member1 = member_queryset_fixture[0]
        client.force_authenticate(user=member1)
        response = client.get(path=reverse(viewname="member-detail", args=[member1.id]), )
        assert response.status_code == status.HTTP_200_OK

        serializer = member_serializers.MemberSerializer(member1)
        assert response.data == serializer.data


    def test_positive_member_get_request_by_me(self, member_queryset_fixture):
        """Test should return a member object by action 'me'"""
        member1 = member_queryset_fixture[0]
        client.force_authenticate(user=member1)
        response = client.get(path=reverse(viewname="member-detail", args=["me"]), )
        assert response.status_code == status.HTTP_200_OK

        serializer = member_serializers.MemberSerializer(member1)
        assert response.data == serializer.data


    def test_positive_member_get_request_by_own_username(self, member_queryset_fixture):
        """Test should return a member object by its own username"""
        member1 = member_queryset_fixture[0]
        client.force_authenticate(user=member1)
        response = client.get(path=reverse(viewname="member-detail", args=[member1.username]), )
        assert response.status_code == status.HTTP_200_OK

        serializer = member_serializers.MemberSerializer(member1)
        assert response.data == serializer.data


    def test_positive_member_get_request_by_others_username(self, member_queryset_fixture):
        """Test should return a member object by other member's username"""
        member1 = member_queryset_fixture[0]
        member2 = member_queryset_fixture[1]
        client.force_authenticate(user=member1)
        response = client.get(path=reverse(viewname="member-detail", args=[member2.username]), )
        assert response.status_code == status.HTTP_200_OK

        serializer = member_serializers.MemberSerializer(member2)
        assert response.data == serializer.data


    def test_member_get_request_by_others_id(self, member_queryset_fixture):
        """
        Test should return 404 because of other member's id
        p.s. default djoser logic
        """
        member1 = member_queryset_fixture[0]
        member2 = member_queryset_fixture[1]
        client.force_authenticate(user=member1)
        response = client.get(path=reverse(viewname="member-detail", args=[member2.id]), )
        assert response.status_code == status.HTTP_404_NOT_FOUND

        assert response.status_text == "Not Found"


    def test_member_get_request_by_others_username_not_active(self, member_queryset_fixture):
        """Test should return 404 because of other member is not active"""
        member1 = member_queryset_fixture[0]
        member2 = member_queryset_fixture[1]
        member2.is_active = False
        member2.save()
        client.force_authenticate(user=member1)
        response = client.get(path=reverse(viewname="member-detail", args=[member2.id]), )
        assert response.status_code == status.HTTP_404_NOT_FOUND

        assert response.status_text == "Not Found"


    def test_member_get_request_by_others_username_not_verified(self, member_queryset_fixture):
        """Test should return 404 because of other member is not verified"""
        member1 = member_queryset_fixture[0]
        member2 = member_queryset_fixture[1]
        member2.is_verified = False
        member2.save()
        client.force_authenticate(user=member1)
        response = client.get(path=reverse(viewname="member-detail", args=[member2.id]), )
        assert response.status_code == status.HTTP_404_NOT_FOUND

        assert response.status_text == "Not Found"


    def test_unverified_member_get_request_by_username(self, member_queryset_fixture):
        """Test should return 404 because of unverified member"""
        member1 = member_queryset_fixture[0]
        member1.is_verified = False
        member1.save()
        client.force_authenticate(user=member1)
        response = client.get(path=reverse(viewname="member-detail", args=[member1.username]), )
        assert response.status_code == status.HTTP_404_NOT_FOUND

        assert response.status_text == "Not Found"


    def test_unactive_member_get_request_by_username(self, member_queryset_fixture):
        """Test should return 404 because of unverified member"""
        member1 = member_queryset_fixture[0]
        member1.is_active = False
        member1.save()
        client.force_authenticate(user=member1)
        response = client.get(path=reverse(viewname="member-detail", args=[member1.username]), )
        assert response.status_code == status.HTTP_404_NOT_FOUND

        assert response.status_text == "Not Found"