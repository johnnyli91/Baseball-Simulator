from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name


class Player(models.Model):
    ROLE_CHOICES = (
        (0, "Batter"),
        (1, "Pitcher")
    )
    name = models.CharField(max_length=120)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    # display stats
    power = models.IntegerField()
    eye = models.IntegerField()
    speed = models.IntegerField()
    team = models.ForeignKey(Team, related_name="team_player")
    # actual stats for calculations
    batter_contact = models.IntegerField()
    batter_single = models.IntegerField()
    batter_double = models.IntegerField()
    batter_triple = models.IntegerField()
    batter_homerun = models.IntegerField()
    batter_walk = models.IntegerField()
    batter_strikeout = models.IntegerField()
    batter_groundout = models.IntegerField()
    batter_flyout = models.IntegerField()
    batter_speed = models.IntegerField()
    pitcher_contact = models.IntegerField(default=0)
    pitcher_single = models.IntegerField(default=0)
    pitcher_double = models.IntegerField(default=0)
    pitcher_triple = models.IntegerField(default=0)
    pitcher_homerun = models.IntegerField(default=0)
    pitcher_walk = models.IntegerField(default=0)
    pitcher_strikeout = models.IntegerField(default=0)
    pitcher_groundout = models.IntegerField(default=0)
    pitcher_flyout = models.IntegerField(default=0)


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
    inning = models.ForeignKey(Inning, related_name="inning")
    result = models.IntegerField(choices=RESULT_CHOICES)

    def __unicode__(self):
        return "{}, {}".format(self.inning, self.player)