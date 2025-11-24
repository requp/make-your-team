from djoser.constants import Messages as djoser_messages
from djoser import serializers as djoser_serializers
from rest_framework import serializers

from apps.members import models as member_models

class SkillMiniSerializer(serializers.ModelSerializer):
    """Skill serializer for a member serializer"""
    class Meta:
        model = member_models.Skill
        fields = ("id", "name")

class MemberCreateSerializer(djoser_serializers.UserCreateSerializer):
    """Member create serializer"""
    re_password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta(djoser_serializers.UserCreateSerializer.Meta):
        model = member_models.Member
        fields = (
            "username",
            "email",
            "password",
            "re_password",
            "first_name",
            "last_name",
        )
    def validate(self, attrs):
        if not attrs.get("email"):
            raise serializers.ValidationError({"email": "This field is required."})
        if attrs["password"] != attrs["re_password"]:
            raise serializers.ValidationError(
                {"re_password": djoser_messages.PASSWORD_MISMATCH_ERROR}
            )
        del attrs["re_password"]
        return super().validate(attrs=attrs)


class MemberSerializer(djoser_serializers.UserSerializer):
    """Member serializer"""
    username = serializers.CharField(min_length=4, max_length=32, required=False)

    class Meta(djoser_serializers.UserCreateSerializer.Meta):
        model = member_models.Member
        fields = (
            "username",
            "first_name",
            "last_name",
            "bio",
        )
    def validate(self, attrs):
        if attrs.get("username") and self.instance.username != attrs["username"]:
            if member_models.Member.objects.filter(username=attrs["username"]).exists():
                raise serializers.ValidationError({"username": "Current username is taken."})
        return super().validate(attrs=attrs)


    def to_representation(self, instance):
        if not instance.is_verified:
            raise serializers.ValidationError({"is_verified": "User not verified"})
        return super().to_representation(instance=instance)

