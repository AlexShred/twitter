from django.urls import path, include
from rest_framework import routers
from .views import ReplyRetrieveUpdateDestroyAPIView

from . import views

router = routers.DefaultRouter()
router.register('reply', views.ReplyViewSet)
router.register('tweet', views.TweetViewSet, basename='tweet')
router.register(r'tweet/(?P<tweet_id>\d+)/reply', views.ReplyViewSet, basename='tweet-reply')

urlpatterns=[
    path('viewset/', include(router.urls)),
    path('tweets/<int:tweet_id>/reply/<int:pk>/', ReplyRetrieveUpdateDestroyAPIView.as_view(), name='reply-detail'),
]



