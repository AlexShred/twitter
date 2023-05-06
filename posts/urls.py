from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('reply', views.ReplyViewSet)
router.register('tweet', views.TweetViewSet)

urlpatterns=[
    path('viewset/', include(router.urls))
]
