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
