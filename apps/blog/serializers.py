from rest_framework import serializers
# models
from apps.blog.models import Post
from django.conf import settings

from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url',
                  'id',
                  'author',
                  'name',
                  'content',
                  'created_date',
                  )


class PostUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url',
                  'id',
                  'author',
                  'name',
                  'content',
                  'created_date',
                  )
        read_only_fields = (
                            'created_date',
                            )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url',
                  'id',
                  'email',
                  'username',
                  'password'
                  )


class UserUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url',
                  'id',
                  'email',
                  'username',
                  'password'
                  )
