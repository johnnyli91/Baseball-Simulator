import random
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView, Response
from Baseball.models import Game, Inning, Player, Score, Team
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


class InningListAPIView(generics.ListAPIView):
    queryset = Inning.objects.all()
    serializer_class = InningSerializer


class InningCreateAPIView(generics.CreateAPIView):
    queryset = Inning.objects.all()
    serializer_class = InningCreateSerializer


class InningRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inning.objects.all()
    serializer_class = InningDetailSerializer


class GameDetailView(APIView):
    def get(self, request, game_id):

        try:
            game = Game.objects.prefetch_related('team').get(id=game_id)
        except Game.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Game not found.'
            })
        innings = Inning.objects.filter(game=game).order_by('number')
        scores = Score.objects.filter(game=game)

        result_dict = {
            'game_name': game.name,
            'game_data': {}
        }

        for team in game.team.all():
            result_dict['game_data'][team.id] = {
                'name': team.name,
                'innings': [],
                'score': 0
            }
        for inning in innings:
            result_dict['game_data'][inning.team_id]['innings'].append({
                'inning_id': inning.id,
                'number': inning.number,
                'score': inning.score
            })
        for score in scores:
            result_dict['game_data'][score.team_id]['score'] = score.score

        return Response(result_dict)


class PlayerDetailView(APIView):

    def get(self, request, player_id):
        player = get_object_or_404(Player, id=player_id)

        result_dict = {
            'name': player.name,
            'role': player.role,
            'power': player.power_rating,
            'speed': player.speed_rating
        }
        return Response(result_dict)


class TeamDetailView(APIView):

    def get(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        players = Player.objects.filter(team=team).values('id', 'name', 'team')

        result_dict = {
            'name': team.name,
            'players': players
        }

        return Response(result_dict)


class RosterView(APIView):
    def get(self, request, team_id):
        if request.user.is_authenticated():
            user_team = Team.objects.filter(id = team_id)  # returns a list of objects
            team_list = []

            for team in user_team:
                team_list.append({'id': team.id, 'name': team.name})

            user_player = Player.objects.filter(team__in=user_team).values('id', 'name', 'team__name')  # returns a dictionary, filter only works on objects

            result_dict = {
                'user_team': team_list,
                'user_player': user_player
            }
            return Response(result_dict)
        else:
            return Response(request, '../static/app/views/registration/login.html')


class TeamView(APIView):
    def get(self, request):
        if request.user.is_authenticated():
            user_team = Team.objects.filter(user=request.user)  # returns a list of objects
            team_list = []

            for team in user_team:
                team_list.append({'team_name':team.name, 'team_id': team.id})

            result_dict = {
                'user_team': team_list,
            }
            return Response(result_dict)
        else:
            return Response(request, '../static/app/views/registration/login.html')

class PlayerView(APIView):
    def get(self, request, player_id):
        if request.user.is_authenticated():
            user_players = Player.objects.filter(id=player_id)
            player_attributes = []
            player_stats = []

            for player in user_players:
                player_attributes.append({'name': player.name, 'role': player.role, 'power': player.batter_home_run_rating,
                                         'speed': player.speed_rating, 'team': player.team.name,
                                          'hit': player.batter_hit_rating})

                player_stats.append({'year': player.year, 'team': player.team.name, 'games': player.games, 'AB': player.AB,
                                     'R': player.runs, 'H': player.hits, 'double': player.doubles, 'triples': player.triples,
                                     'HR': player.HR, 'RBI': player.RBI, 'BB': player.BB, 'K': player.K, 'SB': player.SB,
                                     'CS': player.CS, 'AVG': player.AVG, 'OBP': player.OBP, 'SLG': player.SLG})
                result_dict = {
                    'player_attributes': player_attributes, 'player_stats': player_stats
                }
            return Response(result_dict)




# TODO: Remove when done testing
class TestBat(APIView):

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

