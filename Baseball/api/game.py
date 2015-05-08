from ..models import *
import random


class Simulation:
    def __init__(self, team1, team2, game):
        self.team1 = Player.objects.filter(team=team1.pk)
        self.team2 = Player.objects.filter(team=team2.pk)
        self.game = game

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
        Bat.objects.create(player=batter, inning=inning, result=result)
        return result

    def play(self):
        inning = 1
        team1_index = 0
        team2_index = 0
        for i in range(9):
            Inning.objects.create(game=self.game, number=inning, team=self.team1[0].team)
            team1_inning = Inning.objects.latest('pk')
            Inning.objects.create(game=self.game, number=inning, team=self.team2[0].team)
            team2_inning = Inning.objects.latest('pk')
            # TODO: make code more DRY
            outs = 0
            score = 0
            first_base = None
            second_base = None
            third_base = None
            while outs < 3:
                current_bat = self.bat(self.team1[team1_index], self.team2[0], team1_inning)
                if current_bat == 4:
                    score += 1
                    if third_base:
                        score += 1
                        third_base = None
                    if second_base:
                        score += 1
                        second_base = None
                    if first_base:
                        score += 1
                        first_base = None
                elif current_bat == 3:
                    if third_base:
                        score += 1
                        third_base = self.team1[team1_index]
                    if second_base:
                        score += 1
                        second_base = None
                    if first_base:
                        score += 1
                        first_base = None
                elif current_bat == 2:
                    if third_base:
                        score += 1
                        third_base = None
                    if second_base:
                        score += 1
                        second_base = self.team1[team1_index]
                    if first_base:
                        third_base = first_base
                        first_base = None
                elif current_bat == 1:
                    if third_base:
                        score += 1
                        third_base = None
                    if second_base:
                        third_base = second_base
                        second_base = None
                    if first_base:
                        second_base = first_base
                        first_base = self.team1[team1_index]
                elif current_bat == 0:
                    outs += 1
                if team1_index == len(self.team1) - 1:
                    team1_index = 0
                else:
                    team1_index += 1
            team1_inning.score = score
            outs = 0
            score = 0
            while outs < 3:
                current_bat = self.bat(self.team2[team1_index], self.team1[0], team2_inning)
                if current_bat == 4:
                    score += 1
                    if third_base:
                        score += 1
                        third_base = None
                    if second_base:
                        score += 1
                        second_base = None
                    if first_base:
                        score += 1
                        first_base = None
                elif current_bat == 3:
                    if third_base:
                        score += 1
                        third_base = self.team2[team1_index]
                    if second_base:
                        score += 1
                        second_base = None
                    if first_base:
                        score += 1
                        first_base = None
                elif current_bat == 2:
                    if third_base:
                        score += 1
                        third_base = None
                    if second_base:
                        score += 1
                        second_base = self.team2[team1_index]
                    if first_base:
                        third_base = first_base
                        first_base = None
                elif current_bat == 1:
                    if third_base:
                        score += 1
                        third_base = None
                    if second_base:
                        third_base = second_base
                        second_base = None
                    if first_base:
                        second_base = first_base
                        first_base = self.team2[team1_index]
                elif current_bat == 0:
                    outs += 1
                if team2_index == len(self.team2) - 1:
                    team2_index = 0
                else:
                    team2_index += 1
            team2_inning.score = score
            inning += 1
