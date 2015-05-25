from rest_framework import serializers
from ..models import *


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('pk', 'name', 'team_player')


class PlayerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('pk', 'name', 'power', 'contact', 'speed', 'pitch')


class TeamDetailSerializer(serializers.ModelSerializer):
    team_player = PlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = ('pk', 'name', 'team_player')


class ScoreSerializer(serializers.ModelSerializer):
    team = TeamDetailSerializer()

    class Meta:
        model = Score
        fields = ('team', 'score')


class GameSerializer(serializers.ModelSerializer):
    # no inning
    game_score = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('pk', 'name', 'team', 'game_score')


class InningSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Inning


class GameDetailSerializer(serializers.ModelSerializer):
    # has inning
    game_score = ScoreSerializer(many=True, read_only=True)
    inning = InningSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('pk', 'name', 'team', 'game_score', 'inning')


class InningCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inning


class BatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bat
        fields = ('pk', 'player', 'inning', 'result')


class BatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bat