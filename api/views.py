from django.shortcuts import render
from rest_framework import viewsets

from .models import CustomUser, Profile
from .serializers import UserSerializer, ProfileSerializer


# create uservieset that inherits from the ModelViewSet


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
