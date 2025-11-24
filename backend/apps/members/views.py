from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.members.models import Member
from apps.members import serializers  as member_serializers


class MemberAPIView(APIView):
    permission_classes = [IsAuthenticated]
    lookup_field = "username"
    serializer_class = member_serializers.MemberSerializer
    queryset = Member.objects.filter(is_active=True, is_verified=True)

    def get(self, request, username):
        """Get member by username"""
        try:
            member = self.queryset.prefetch_related("skills").get(username=username)
        except Member.DoesNotExist:
            raise NotFound()
        serializer = self.serializer_class(member, context={'request': request})
        return Response(serializer.data)

