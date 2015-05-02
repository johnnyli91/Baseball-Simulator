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
    team = TeamSerializer()

    class Meta:
        model = Player
        fields = ('pk', 'name', 'power', 'contact', 'speed', 'pitch', 'team', 'bat')


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('name', 'team')


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