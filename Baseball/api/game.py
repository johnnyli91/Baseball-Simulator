from ..models import *
import random


class Simulation:
    def __init__(self, team1, team2, game):
        self.team1 = Player.objects.filter(team=team1.pk)
        self.team2 = Player.objects.filter(team=team2.pk)
        self.game = game.pk

    def bat(self, batter, pitcher, inning):
        random_number_for_contact = random.randint(0, 100)
        chance_of_contact = batter.contact * pitcher.pitch
        result = 0
        if chance_of_contact <= random_number_for_contact:
            # determines which hit the batter received
            random_number_for_hit = random.randint(0, batter.power)
            double = batter.power/5
            triple = double - pitcher.pitch/10
            home_run = batter.power/10
            single = batter.power - double - triple - home_run
            if random_number_for_hit < single:
                result = 1
            elif random_number_for_hit < single + double:
                result = 2
            elif random_number_for_hit < single + double + triple:
                result = 3
            else:
                result = 4
        Bat.objects.create(player=batter.pk, inning=inning, result=result)
        return result

    def play(self):
        inning = 1
        team1_index = 0
        team2_index = 0
        for i in range(9):
            outs = 0
            Inning.objects.create(game=self.game, number=inning, team=self.team1[0].team)
            team1_inning = Inning.objects.latest('pk')
            Inning.objects.create(game=self.game, number=inning, team=self.team2[0].team)
            team2_inning = Inning.objects.latest('pk')
            while outs < 3:
                if self.bat(self.team1[team1_index], self.team2[0], team1_inning.pk) == 0:
                    outs += 1
                if team1_index == len(self.team1) - 1:
                    team1_index = 0
                else:
                    team1_index += 1
            outs = 0
            while outs < 3:
                if self.bat(self.team2[team2_index], self.team1[0], team2_inning.pk) == 0:
                    outs += 1
                if team2_index == len(self.team2) - 1:
                    team2_index = 0
                else:
                    team2_index += 1
            inning += 1
