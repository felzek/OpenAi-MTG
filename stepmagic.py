# from magicgame import *
import os
import random
import gym
from gym import Env
import numpy
from gym.spaces import Discrete
from enum import Enum
os.system('cls')
## create the phases
# beginning of turn: untap, upkeep, draw
# coin flip mechanism to decide turn order, maybe?
class beginTurn(Enum):
    landforturn == False
    if p1: #this line needs editing
        for k in p1.battlefield:
        p1.battlefield[k].untapped = True
        p1_draw(1)
        #If it's the very first turn p1 does not draw
    if p2:
        for k in p2.battlefield:
        p2.battlefield[k].untapped = True
        p2_draw(1)


# main phase I
class mainPhaseOne(Enum):
    # call play function, and "do... while" possible to play a card or pass the phase
    if p1:
        do {
            #Add a line for passing phase to attack phase
            p1.play()
            manapool = 0
                for k in range(len(self.battlefield)):
                    if isinstance(self.battlefield[k], land):
                        if self.battlefield[k].untapped:
                            if manapool < self.hand[choice].manacost:
                                manapool +=1
        } while(landforturn == False and manapool != 0)
    if p2:
        do {
            #Add a line for passing phase to attack phase
            p2.play()
            manapool = 0
                for k in range(len(self.battlefield)):
                    if isinstance(self.battlefield[k], land):
                        if self.battlefield[k].untapped:
                            if manapool < self.hand[choice].manacost:
                                manapool +=1
        } while(landforturn == False and manapool != 0)

# combat phase
class combatPhase(Enum):
    # player who's turn it is chooses to attack with creature
    # other player either blocks with untapped creature or takes the hit
    attack_c = 6
    # if choose to block
    block_u_c = 7
    # if choose not to block
    p2.life -= 1 #player who's being attacked loses a life point (to be changed)
    pass_phase = 8

# main phase II
class mainPhaseTwo(Enum):
        if p1:
        do {
            #Add a line for passing phase to attack phase
            p1.play()
            manapool = 0
                for k in range(len(self.battlefield)):
                    if isinstance(self.battlefield[k], land):
                        if self.battlefield[k].untapped:
                            if manapool < self.hand[choice].manacost:
                                manapool +=1
        } while(landforturn == False and manapool != 0)
    if p2:
        do {
            #Add a line for passing phase to attack phase
            p2.play()
            manapool = 0
                for k in range(len(self.battlefield)):
                    if isinstance(self.battlefield[k], land):
                        if self.battlefield[k].untapped:
                            if manapool < self.hand[choice].manacost:
                                manapool +=1
        } while(landforturn == False and manapool != 0)

# discard phase
class discardPhase(Enum):
    if p1:
        if len(p1.hand()) > 7:
            #discard down to 7 cards
            num = len(p1.hand()) - 7
            print("You need to discard " + num + "cards.")
            #Take player input on which cards to discard

#end of turn could technically be a phase but we have nothing to do in this because of our simplified setup

class switchTurn():
    # after discard phase, starts beginTurn() for next player

class PlayerTurn():
    # go through the phases
    beginTurn
    mainPhaseOne
    combatPhase
    mainPhaseTwo
    discardPhase
    #in this particular order, please

class endGame():
    # game ends when life point is at or below 0
    # game ends when you try to draw a card from a non-existant deck
