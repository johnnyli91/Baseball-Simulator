from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^teams/$', TeamListCreateAPIView.as_view()),
    url(r'^teams/(?P<pk>\d+)', TeamRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^players/$', PlayerListAPIView.as_view()),
    url(r'^players/create', PlayerCreateAPIView.as_view()),
    url(r'^players/(?P<pk>\d+)', PlayerRetrieveUpdateDestroyAPIView),
    url(r'^games/$', GameListCreateAPIView.as_view()),
    url(r'^games/(?P<pk>\d+)', GameRetrieveUpdateDestroyAPIView.as_view()),
]