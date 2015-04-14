__author__ = 'davidjue'

import random

class Simulation():
    #ratings = ['Name', power, contact, speed, pitcher contact, 'Team']
    #setting homeTeamHitter ratings until we have database to call them from
    def __init__(self):
        self.homeHitter = ['Home Hitter', 60, 0.6, 50, 100, 'Home']
        self.awayHitter = ['Away Hitter', 50, 0.5, 50, 100, 'Away']
        self.homePitcher = ['Home Pitcher', 50, 50, 50, 40, 'Home']
        self.awayPitcher = ['Away Pitcher', 50, 50, 50, 50, 'Away']

    def contactOrNot(self):
        randomNumber = random.randint(0,100)
        chanceOfContact = self.homeHitter[2]*self.awayPitcher[4]
        if chanceOfContact <= randomNumber:
            self.typeOfHit()

        else:
            contactResult = 'Contact not made'
            print(contactResult)


    def typeOfHit(self):
        randomNumber = random.randint(0,self.homeHitter[1])
        double = self.homeHitter[1]/5
        triple = double-self.homeHitter[4]/10
        homerun = self.homeHitter[1]/10
        single = self.homeHitter[1]-double-triple-homerun
        if randomNumber < single:
            print('Single')
        elif randomNumber > single and randomNumber < single+double:
            print('Double')
        elif randomNumber > single+double and randomNumber < single+double+triple:
            print('Triple')
        else:
            print('Homerun')

    def printHitter(self):
        print(self.homeHitter)

lemon = Simulation()

lemon.contactOrNot()


