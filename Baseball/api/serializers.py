from rest_framework import serializers
from ..models import *


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team


class PlayerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player


class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Player


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game


class InningSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Inning


class BatSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    inning = InningSerializer(read_only=True)

    class Meta:
        model = Bat


