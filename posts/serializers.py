from rest_framework import serializers

from .models import Tweet, Reply


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"
        read_only_fields = ['profile', ]


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"
        read_only_fields = ['profile', ]
