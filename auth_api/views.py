from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from auth_api.models import User

from drf_spectacular.utils import extend_schema, OpenApiParameter


class UserSerializer(serializers.ModelSerializer):
    """shema生成用"""

    class Meta:
        model = User
        fields = (
            "id",
            "password",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
        )


class UserViewSet(viewsets.ViewSet):
    @extend_schema(responses=UserSerializer)
    @extend_schema(description="セッションからユーザ情報を取得する。", methods=["GET"])
    @action(detail=False, methods=["get"])
    def get_info(self, request):
        user = self.request.user.__dict__["_wrapped"].__dict__
        user.pop("_state")
        if user:
            return Response(user)
        else:
            return Response({})
