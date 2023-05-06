from django.shortcuts import render

from rest_framework import generics

from .models import User, Profile
from .serializers import UserReqisterSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserReqisterSerializer



