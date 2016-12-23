from django.conf.urls import url
from django.contrib import admin

from views import PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDestroyAPIView

urlpatterns = [
    url(r'^$', PostListAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view()),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/delete/$', PostDestroyAPIView.as_view()),
]


