from ..models import *
import random


class Simulation:
    def __init__(self, team1, team2, game):
        self.team1 = Player.objects.filter(team=team1.pk)
        self.team2 = Player.objects.filter(team=team2.pk)
        self.pitcher1 = self.team1.filter(role=1)
        self.pitcher2 = self.team2.filter(role=1)
        self.game = game
        self.team1_index = 0
        self.team2_index = 0

    def bat(self, batter, pitcher, inning):
        random_number_for_contact = random.randint(0, 1)
        chance_of_contact = (batter.batter_contact-pitcher.pitcher_contact) * 0.0025 + 0.25
        if chance_of_contact <= random_number_for_contact:
            # determines which hit the batter received
            random_number_for_result = random.uniform(0, 1)
            outcome_single = (batter.batter_single - pitcher.pitcher_single) * 0.001 + 0.67
            outcome_double = (batter.batter_double - pitcher.pitcher_double) * 0.001 + 0.2
            outcome_triple = (batter.batter_triple - pitcher.pitcher_triple) * 0.001 + 0.01
            outcome_homerun = (batter.batter_homerun - pitcher.pitcher_homerun) * 0.001 + 0.1
            outcome_walk = (batter.batter_walk - pitcher.pitcher_walk) * 0.001 + 0.08
            outcome_total = outcome_single + outcome_double + outcome_triple + outcome_homerun + outcome_walk
            percent_single = outcome_single/outcome_total
            percent_double = outcome_double/outcome_total
            percent_triple = outcome_triple/outcome_total
            percent_homerun = outcome_homerun/outcome_total
            if random_number_for_result <= percent_single:
                result = 1
            elif random_number_for_result <= percent_single + percent_double:
                result = 2
            elif random_number_for_result <= percent_single + percent_double + percent_triple:
                result = 3
            elif random_number_for_result <= percent_single + percent_double + percent_triple + percent_homerun:
                result = 4
            else:
                result = 5
        else:
            random_number_for_out = random.uniform(0, 1)
            strikeout = 0.001 + (pitcher.pitcher_strikeout/batter.batter_strikeout) * 0.0099
            groundout = 0.001 + (pitcher.pitcher_groundout/batter.batter_groundout) * 0.0099
            flyout = 0.001 + (pitcher.pitcher_flyout/batter.batter_flyout) * 0.0099
            out_total = strikeout + groundout + flyout
            percent_strikeout = strikeout/out_total
            percent_groundout = groundout/out_total
            if random_number_for_out <= percent_strikeout:
                result = 6
            elif random_number_for_out <= percent_strikeout + percent_groundout:
                result = 7
            else:
                result = 8
        Bat.objects.create(player=batter, inning=inning, result=result)
        return result

    def inning(self, team, pitcher, team_index, team_inning):
        outs = 0
        score = 0
        first_base = None
        second_base = None
        third_base = None
        while outs < 3:
            current_bat = self.bat(team[team_index], pitcher, team_inning)
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
                if second_base:
                    score += 1
                    second_base = None
                if first_base:
                    score += 1
                    first_base = None
                third_base = team[team_index]
            elif current_bat == 2:
                if third_base:
                    score += 1
                    third_base = None
                if second_base:
                    score += 1
                if first_base:
                    third_base = first_base
                    first_base = None
                second_base = team[team_index]
            elif current_bat == 1 or current_bat == 5:
                if third_base:
                    score += 1
                    third_base = None
                if second_base:
                    third_base = second_base
                    second_base = None
                if first_base:
                    second_base = first_base
                first_base = team[team_index]
            else:
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
            self.inning(self.team1, self.pitcher2[0], self.team1_index, team1_inning)
            self.inning(self.team2, self.pitcher1[0], self.team2_index, team2_inning)
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
