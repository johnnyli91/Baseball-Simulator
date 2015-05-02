from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=120)
    power = models.IntegerField()
    contact = models.IntegerField()
    speed = models.IntegerField()
    pitch = models.IntegerField()
    team = models.ForeignKey(Team, related_name="team_player")

    def __unicode__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=120)
    team = models.ManyToManyField(Team)

    def __unicode__(self):
        return self.name


class Inning(models.Model):
    game = models.ForeignKey(Game, related_name="inning")
    number = models.IntegerField()
    score = models.IntegerField()
    team = models.ForeignKey(Team, related_name="inning")

    def __unicode__(self):
        return "{}, Inning: {}, Team: {}".format(self.game, self.number, self.team)


class Bat(models.Model):
    RESULT_CHOICES = (
        (0, "Out"),
        (1, "Single"),
        (2, "Double"),
        (3, "Triple"),
        (4, "Home Run")
    )
    player = models.ForeignKey(Player, related_name="bat")
    inning = models.ForeignKey(Inning, related_name="inning")
    result = models.IntegerField(choices=RESULT_CHOICES)

    def __unicode__(self):
        return "{}, {}".format(self.inning, self.player)