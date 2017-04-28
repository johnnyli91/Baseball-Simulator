import random
from rest_framework import generics, views
from rest_framework.response import Response
from Baseball.models import Game, Inning, Player, Team
from game import Simulation
from serializers import GameSerializer, GameDetailSerializer, InningDetailSerializer, \
    InningSerializer, InningCreateSerializer, PlayerSerializer, \
    TeamSerializer, TeamDetailSerializer


class TeamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        FIRST_NAME_LIST = ["Robert", "Joe", "David", "John"]
        LAST_NAME_LIST = ["Richards", "Chan", "Li", "Jue"]
        TEAM_SIZE = 8

        serializer.save()
        team_pk = Team.objects.latest('pk')
        # TODO: power calculation
        player_list = [Player(name="{} {}".format(random.choice(FIRST_NAME_LIST), random.choice(LAST_NAME_LIST)),
                              team=team_pk,
                              batter_double_rating=random.randint(1, Player.MAX_RATING),
                              batter_home_run_rating=random.randint(1, Player.MAX_RATING),
                              batter_hit_rating=random.randint(1, Player.MAX_RATING),
                              pitcher_home_run_rating=random.randint(1, Player.MAX_RATING),
                              speed_rating=random.randint(1, Player.MAX_RATING),
                              pitcher_hit_rating=random.randint(1, Player.MAX_RATING),
                              role=0) for i in xrange(TEAM_SIZE)]
        player_list.append(Player(name="{} {}".format(random.choice(FIRST_NAME_LIST), random.choice(LAST_NAME_LIST)),
                                  team=team_pk,
                                  batter_double_rating=random.randint(1, Player.MAX_RATING),
                                  batter_home_run_rating=random.randint(1, Player.MAX_RATING),
                                  batter_hit_rating=random.randint(1, Player.MAX_RATING),
                                  pitcher_home_run_rating=random.randint(1, Player.MAX_RATING),
                                  speed_rating=random.randint(1, Player.MAX_RATING),
                                  pitcher_hit_rating=random.randint(1, Player.MAX_RATING),
                                  role=1))
        Player.objects.bulk_create(player_list)


class TeamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer


class PlayerListAPIView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameListCreateAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
        serializer.save()
        teams = self.request.data['team']
        team1 = Team.objects.get(pk=teams[0])
        team2 = Team.objects.get(pk=teams[1])
        game = Game.objects.latest('pk') #gets current game
        sim = Simulation(team1, team2, game)
        sim.play()


class GameRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameDetailSerializer


class InningListAPIView(generics.ListAPIView):
    queryset = Inning.objects.all()
    serializer_class = InningSerializer


class InningCreateAPIView(generics.CreateAPIView):
    queryset = Inning.objects.all()
    serializer_class = InningCreateSerializer


class InningRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inning.objects.all()
    serializer_class = InningDetailSerializer


#TODO: Remove when done testing
class TestBat(views.APIView):

    def get(self, request):
        result_dict = {}
        team_1 = Team.objects.get(pk=1)
        team_2 = Team.objects.get(pk=2)
        game = Game.objects.latest('pk')
        sim = Simulation(team_1, team_2, game)
        for i in xrange(1000):
            current_result = sim.test_at_bat()
            try:
                result_dict[current_result] += 1
            except KeyError:
                result_dict[current_result] = 1
        return Response(result_dict)

