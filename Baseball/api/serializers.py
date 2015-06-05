from rest_framework import serializers
from ..models import *


class BatSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()

    class Meta:
        model = Bat
        fields = ('pk', 'player', 'inning', 'result')

    def get_result(self, obj):
        return obj.get_result_display()


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('pk', 'name', 'team_player')


class PlayerSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ('pk', 'name', 'role', 'power', 'eye', 'speed', 'pitcher_control', 'pitcher_power', 'pitcher_movement')

    def get_role(self, obj):
        return obj.get_role_display()


class PlayerWithBatSerializer(serializers.ModelSerializer):
    bat = BatSerializer(many=True)
    role = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ('pk', 'name', 'role', 'bat')

    def get_role(self, obj):
        return obj.get_role_display()


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
    team = TeamDetailSerializer(read_only=True)

    class Meta:
        model = Inning


class GameBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('pk', 'name', 'team')


class InningDetailSerializer(serializers.ModelSerializer):
    team = TeamDetailWithBatSerializer(read_only=True)
    game = GameBasicSerializer()

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