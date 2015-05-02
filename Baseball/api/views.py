from django.http import QueryDict
from rest_framework import generics
from serializers import *


class TeamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerListAPIView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerCreateAPIView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerCreateSerializer


class PlayerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameListCreateAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save()
        teams = self.request.POST.getlist('team')
        team1 = Team.objects.get(pk=teams[0])
        team2 = Team.objects.get(pk=teams[1])
        game = Game.objects.latest('pk') #gets current game
        Team.objects.create(name=team2.name)


class GameRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class InningListAPIView(generics.ListAPIView):
    queryset = Inning.objects.all()
    serializer_class = InningSerializer


class InningCreateAPIView(generics.CreateAPIView):
    queryset = Inning.objects.all()
    serializer_class = InningCreateSerializer


class InningRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inning.objects.all()
    serializer_class = InningSerializer


class BatListAPIView(generics.ListAPIView):
    queryset = Bat.objects.all()
    serializer_class = BatSerializer


class BatCreateAPIView(generics.CreateAPIView):
    queryset = Bat.objects.all()
    serializer_class = BatCreateSerializer


class BatRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bat.objects.all()
    serializer_class = BatSerializer
