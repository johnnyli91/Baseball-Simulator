from rest_framework import serializers
from ..models import *


class BatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bat
        fields = ('pk', 'player', 'inning', 'result')


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('pk', 'name', 'team_player')


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('pk', 'name', 'role', 'power', 'eye', 'speed', 'pitcher_control', 'pitcher_power', 'pitcher_movement')


class PlayerWithBatSerializer(serializers.ModelSerializer):
    bat = BatSerializer(many=True)

    class Meta:
        model = Player
        fields = ('pk', 'name', 'role', 'bat')


class TeamDetailSerializer(serializers.ModelSerializer):
    team_player = PlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = ('pk', 'name', 'team_player')


class TeamDetailWithBatSerializer(serializers.ModelSerializer):
    team_player = PlayerWithBatSerializer(many=True)

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
    team = TeamDetailWithBatSerializer(read_only=True)

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


class BatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bat