from ..models import *
import random


class Simulation:
    def __init__(self, team1, team2, game):
        self.team1 = Player.objects.filter(team=team1.pk)
        self.team2 = Player.objects.filter(team=team2.pk)
        self.game = game
        self.team1_index = 0
        self.team2_index = 0

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

    def inning(self, team, team2, team_index, team_inning):
        outs = 0
        score = 0
        first_base = None
        second_base = None
        third_base = None
        while outs < 3:
            current_bat = self.bat(team[team_index], team2[0], team_inning)
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
                    third_base = team[team_index]
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
                    second_base = team[team_index]
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
                    first_base = team[team_index]
            elif current_bat == 0:
                outs += 1
            if team_index == len(team) - 1:
                team_index = 0
            else:
                team_index += 1
        team_inning.score = score
        team_inning.save()

    def play(self):
        inning = 1
        for i in range(9):
            Inning.objects.create(game=self.game, number=inning, team=self.team1[0].team)
            team1_inning = Inning.objects.latest('pk')
            Inning.objects.create(game=self.game, number=inning, team=self.team2[0].team)
            team2_inning = Inning.objects.latest('pk')
            # TODO: fix bug about resetting team indexes
            self.inning(self.team1, self.team2, self.team1_index, team1_inning)
            self.inning(self.team2, self.team1, self.team2_index, team2_inning)
            inning += 1
        all_innings = Inning.objects.filter(game=self.game)
        team1_inning = all_innings.filter(team=self.team1[0].team)
        team2_inning = all_innings.filter(team=self.team2[0].team)
        team1_score = 0
        team2_score = 0
        for inning in team1_inning:
            team1_score += inning.score
        for inning in team2_inning:
            team2_score += inning.score
        Score.objects.create(team=self.team1[0].team, game=self.game, score=team1_score)
        Score.objects.create(team=self.team2[0].team, game=self.game, score=team2_score)
