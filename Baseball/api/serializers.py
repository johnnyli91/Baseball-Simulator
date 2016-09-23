from rest_framework import serializers
from Baseball.models import Bat, Game, Inning, Player, Score, Team


class BatCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bat


class PlayerOnlyNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('name',)


class BatSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()
    player = PlayerOnlyNameSerializer()

    class Meta:
        model = Bat
        fields = ('pk', 'player', 'result')

    def get_result(self, obj):
        return obj.get_result_display()


class PlayerSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ('pk', 'name', 'role', 'rating', 'speed')

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


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('pk', 'name', 'team_player')


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


class GameBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('pk', 'name', 'team')


class InningCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inning


class InningSerializer(serializers.ModelSerializer):
    team = TeamDetailSerializer(read_only=True)

    class Meta:
        model = Inning


class InningDetailSerializer(serializers.ModelSerializer):
    team = TeamDetailSerializer(read_only=True)
    game = GameBasicSerializer()
    bat_inning = BatSerializer(many=True, read_only=True)

    class Meta:
        model = Inning
        fields = ('id', 'game', 'number', 'score', 'team', 'bat_inning')


class GameDetailSerializer(serializers.ModelSerializer):
    # has inning
    game_score = ScoreSerializer(many=True, read_only=True)
    inning = InningSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = ('pk', 'name', 'team', 'game_score', 'inning')