from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^teams/$', TeamListCreateAPIView.as_view()),
    url(r'^teams/(?P<pk>\d+)', TeamRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^players/$', PlayerListAPIView.as_view()),
    url(r'^players/(?P<pk>\d+)', PlayerRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^games/$', GameListCreateAPIView.as_view()),
    url(r'^games/(?P<pk>\d+)', GameRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^innings/$', InningListAPIView.as_view()),
    url(r'^innings/create', InningCreateAPIView.as_view()),
    url(r'^innings/(?P<pk>\d+)', InningRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^bats/$', BatListAPIView.as_view()),
    url(r'^bats/create', BatCreateAPIView.as_view()),
    url(r'^bats/(?P<pk>\d+)', BatRetrieveUpdateDestroyAPIView.as_view())
]