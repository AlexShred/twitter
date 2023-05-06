from django.shortcuts import render
from rest_framework import viewsets

from .models import Reply, Tweet
from .serializers import TweetSerializer, ReplySerializer


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
