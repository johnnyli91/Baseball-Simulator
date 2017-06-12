from django.conf.urls import include, url
from views import TeamListCreateAPIView, TeamDetailView, PlayerListAPIView, \
    PlayerDetailView, GameListCreateAPIView, GameDetailView, \
    InningListAPIView, InningCreateAPIView, InningRetrieveUpdateDestroyAPIView, TestBat, RosterView, TeamView, \
    PlayerView

urlpatterns = [
    url(r'^teams/$', TeamListCreateAPIView.as_view()),
    url(r'^teams/(?P<team_id>\d+)', TeamDetailView.as_view()),
    url(r'^players/$', PlayerListAPIView.as_view()),
    url(r'^players/(?P<player_id>\d+)', PlayerDetailView.as_view()),
    url(r'^games/$', GameListCreateAPIView.as_view()),
    url(r'^games/(?P<game_id>\d+)', GameDetailView.as_view()),
    url(r'^innings/$', InningListAPIView.as_view()),
    url(r'^innings/create', InningCreateAPIView.as_view()),
    url(r'^innings/(?P<pk>\d+)', InningRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^test/', TestBat.as_view()),
    url(r'^teamview/$', TeamView.as_view()),
    url(r'^teamview/(?P<team_id>\d+)', RosterView.as_view()),
    url(r'^playerprofile/(?P<player_id>\d+)', PlayerView.as_view()),
]
