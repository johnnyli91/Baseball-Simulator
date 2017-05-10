from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=120)
    user = models.ForeignKey(User, null=True)
    def __unicode__(self):
        return self.name


class Player(models.Model):
    ROLE_CHOICES = (
        (0, "Batter"),
        (1, "Pitcher")
    )
    MAX_RATING = 99

    name = models.CharField(max_length=120)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    batter_double_rating = models.IntegerField(default=1)
    batter_home_run_rating = models.IntegerField(default=1)
    batter_hit_rating = models.IntegerField(default=1)
    pitcher_home_run_rating = models.IntegerField(default=1)
    pitcher_hit_rating = models.IntegerField(default=1)
    speed_rating = models.IntegerField(default=1)
    power_rating = models.IntegerField(default=1)
    team = models.ForeignKey(Team, null=True)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=120)
    team = models.ManyToManyField(Team)

    def __unicode__(self):
        return self.name


class Score(models.Model):
    team = models.ForeignKey(Team, related_name="team_score")
    score = models.IntegerField()
    game = models.ForeignKey(Game, related_name="game_score")

    def __unicode__(self):
        return "{}: {}".format(self.game, self.team)


class Inning(models.Model):
    game = models.ForeignKey(Game, related_name="inning")
    number = models.IntegerField()
    score = models.IntegerField(null=True)
    team = models.ForeignKey(Team, related_name="inning")

    def __unicode__(self):
        return "{}, Inning: {}, Team: {}".format(self.game, self.number, self.team)


class Bat(models.Model):
    RESULT_CHOICES = (
        (1, "Single"),
        (2, "Double"),
        (3, "Triple"),
        (4, "Home Run"),
        (5, "Walk"),
        (6, "Strikeout"),
        (7, "Groundout"),
        (8, "Flyout")
    )
    player = models.ForeignKey(Player, related_name="bat")
    inning = models.ForeignKey(Inning, related_name="bat_inning")
    result = models.IntegerField(choices=RESULT_CHOICES)

    def __unicode__(self):
        return "{}, {}".format(self.inning, self.player)
