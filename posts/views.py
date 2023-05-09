from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permisions import IsAuthorOrIsAuthenticated

from .models import Reply, Tweet
from .serializers import TweetSerializer, ReplySerializer


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorOrIsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(tweet_id=self.kwargs['tweet_id'])

    def perform_create(self, serializer):
        tweet_id = self.kwargs['tweet_id']
        tweet = Tweet.objects.get(id=tweet_id)
        serializer.save(tweet=tweet)


class ReplyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [IsAuthenticated, IsAuthorOrIsAuthenticated]
    lookup_url_kwarg = 'reply_id'

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(id=self.kwargs[self.lookup_url_kwarg])
        return obj

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorOrIsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    # def list(self, request, *args, **kwargs):
    #     print(request.auth)
    #     print(request.user)
    #     return super().list(request, *args, **kwargs)
