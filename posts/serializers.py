from rest_framework import serializers

from .models import Tweet, Reply


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = "__all__"

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"