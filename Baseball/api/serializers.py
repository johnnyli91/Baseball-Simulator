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


class TeamForScoreSerializer(serializers.ModelSerializer):
    team_player = PlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = ('pk', 'name', 'team_player')


class ScoreSerializer(serializers.ModelSerializer):
    team = TeamForScoreSerializer()

    class Meta:
        model = Score
        fields = ('team', 'score')


class GameSerializer(serializers.ModelSerializer):
    game_score = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('name', 'team', 'game_score')


class InningSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Inning


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