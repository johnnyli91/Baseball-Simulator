from rest_framework import generics
from serializers import *
from game import Simulation
import random
import math


class TeamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        def round_down(x):
            return math.floor(x/5) * 5
        serializer.save()
        team_pk = Team.objects.latest('pk')
        b_contact = random.randint(1, 100)
        b_single = random.randint(1, 100)
        b_double = random.randint(1, 100)
        b_triple = random.randint(1, 100)
        b_homerun = random.randint(1, 100)
        b_walk = random.randint(1, 100)
        b_strikeout = random.randint(1, 100)
        b_groundout = random.randint(1, 100)
        b_flyout = random.randint(1, 100)
        b_speed = random.randint(1, 100)
        p_contact = random.randint(1, 100)
        p_single = random.randint(1, 100)
        p_double = random.randint(1, 100)
        p_triple = random.randint(1, 100)
        p_homerun = random.randint(1, 100)
        p_walk = random.randint(1, 100)
        p_strikeout = random.randint(1, 100)
        p_groundout = random.randint(1, 100)
        p_flyout = random.randint(1, 100)
        speed = round_down(b_triple * 0.49 + 50)
        power = round_down(b_homerun * 0.49 + 50)
        eye = round_down(b_walk * 0.49 + 50)
        Player.objects.create(name="Pitcher", team=team_pk, power=power, eye=eye, speed=speed, batter_contact=b_contact, batter_single=b_single,
                              batter_double=b_double, batter_triple=b_triple, batter_homerun=b_homerun,
                              batter_walk=b_walk, batter_strikeout=b_strikeout, batter_groundout=b_groundout,
                              batter_flyout=b_flyout, batter_speed=b_speed, pitcher_contact=p_contact,
                              pitcher_single=p_single, pitcher_double=p_double, pitcher_triple=p_triple,
                              pitcher_homerun=p_homerun, pitcher_walk=p_walk, pitcher_strikeout=p_strikeout,
                              pitcher_groundout=p_groundout, pitcher_flyout=p_flyout, role=1)
        for i in range(8):
            b_contact = random.randint(1, 100)
            b_single = random.randint(1, 100)
            b_double = random.randint(1, 100)
            b_triple = random.randint(1, 100)
            b_homerun = random.randint(1, 100)
            b_walk = random.randint(1, 100)
            b_strikeout = random.randint(1, 100)
            b_groundout = random.randint(1, 100)
            b_flyout = random.randint(1, 100)
            b_speed = random.randint(1, 100)
            speed = round_down(b_triple * 0.49 + 50)
            power = round_down(b_homerun * 0.49 + 50)
            eye = round_down(b_walk * 0.49 + 50)
            Player.objects.create(name="Player " + str(i), team=team_pk, power=power, eye=eye, speed=speed, batter_contact=b_contact, batter_single=b_single,
                              batter_double=b_double, batter_triple=b_triple, batter_homerun=b_homerun,
                              batter_walk=b_walk, batter_strikeout=b_strikeout, batter_groundout=b_groundout,
                              batter_flyout=b_flyout, batter_speed=b_speed)



class TeamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer


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
