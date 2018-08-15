# django
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# drf
from rest_framework import routers
# views
from apps.blog import views  # make sure to add your new views to __init__.py

router = routers.DefaultRouter()

router.register(r'post',
                views.PostViewSet,
                base_name='post'
                )

router.register(r'users',
                views.UserViewSet,
                base_name='user'
                )

urlpatterns = [
    path('', include(router.urls)),
]
