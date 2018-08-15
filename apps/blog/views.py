# Django Rest Framework
from rest_framework import viewsets
# Models
from apps.blog.models import Post
from django.contrib.auth import get_user_model
# Serializers
from apps.blog.serializers import (
    PostSerializer,
    PostUpdateSerializer,
    UserSerializer,
    UserUpdateSerializer
    )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return PostUpdateSerializer
        else:
            return PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UserUpdateSerializer
        else:
            return UserSerializer
