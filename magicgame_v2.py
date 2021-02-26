# from magicgame import *
import os
import random
import gym
from gym import Env
import numpy
from gym.spaces import Discrete
from enum import Enum
os.system('cls')

class Action(Enum):
    # Allowed Actions
    # u = untapped, t = tapped, c = creature, l = land, s = spell
    # s_u_c is to play a spell targeting an untapped creature
    play_c = 0
    play_s_u_c = 1
    play_s_t_c = 2
    play_s_self = 3
    play_s_opp = 4
    play_l = 5
    attack_c = 6
    block_u_c = 7
    pass_phase = 8

class Community_Data:
    # Data available to everyone
    def __init__(self):
        self.p1_life = 20
        self.p2_life = 20
        self.p1_deck = 60
        self.p2_deck = 60
        self.p1_num_hand = 0
        self.p2_num_hand = 0
        self.p1_battlefield = []
        self.p2_battlefield = []

class Player_Data:
    def __init__(self):
        self.position = 0
        self.deckconstruction = [0, 0, 0]

class Stage(Enum):
    main = 0
    attack = 1
    block = 2

class Card_Data(Enum):
    # u = untapped, t = tapped, c = creature, l = land, s = spell
    u_c = 0 
    s = 1
    u_l = 2
    t_c = 3
    t_l = 4

class magicgame(Env):
    def __init__(self, decksize = 60, num_creatures = 20, num_spells = 20):
        self.p1_life = 20
        self.p2_life = 20
        self.p1_decksize = decksize
        self.p2_decksize = decksize
        self.p1_battlefield = []
        self.p2_battlefield = []
        self.p1_deck = self.builddeck(decksize, num_creatures, num_spells)
        self.p2_deck = self.builddeck(decksize, num_creatures, num_spells)
        random.shuffle(self.p1_deck)
        random.shuffle(self.p2_deck)
        self.p1_hand = []
        self.p2_hand = []
        self.p1_draw(7)
        self.p2_draw(7)
        self.p1_landforturn = False
        self.p2_landforturn = False

    def builddeck(self, decksize, num_creatures, num_spells):
        deck = []
        for c in [0,1,2]:
            if c == 0:
                for i in range(0,num_creatures):
                    deck.append(0)
            elif c == 1:
                for i in range(0, num_spells):
                    deck.append(1)
            else:
                for i in range(0, decksize - num_creatures - num_spells):
                    deck.append(2)
        return deck

    def p1_draw(self, number_draw = 1):
        for i in range(number_draw):
            self.p1_hand.append(self.p1_deck.pop(0))

    def p2_draw(self, number_draw = 1):
        for i in range(number_draw):
            self.p2_hand.append(self.p2_deck.pop(0))

    def p1_play(self, card_choice, target_choice = 0):
        if self.p1_hand[card_choice] == 0:
            manapool = 0
            for k in range(len(self.p1_battlefield)):
                if self.p1_battlefield[k] == 2:
                    # Check manacost of creature
                        if manapool < 2:
                            manapool +=1
            if manapool < 2:
                print("You dont have enough untapped mana to play that")
            else:
                tapper = 0
                for k in range(len(self.p1_battlefield)):
                    if self.p1_battlefield[k] == 2:
                        if tapper < 2:
                            self.p1_battlefield[k] = 4
                            tapper += 1
                card = self.p1_hand.pop(card_choice)
                self.p1_battlefield.append(card)

        elif self.hand[choice].cardtype  == 1:
            targetables = [-1, -2]
            targetables.extend(a.p1_battlefield + a.p2_battlefield)

            if self.p1_hand[card_choice] == 1:
            manapool = 0
            for k in range(len(self.p1_battlefield)):
                if self.p1_battlefield[k] == 2:
                    # Check manacost of creature
                        if manapool < 2:
                            manapool +=1
            if manapool < self.hand[choice].manacost:
                print("You dont have enough untapped mana to play that")
            else:
                if i == 0:
                    targetables[i].life = targetables[i].life - self.hand[choice].effect

                elif i == 1:
                    targetables[i].life = targetables[i].life - self.hand[choice].effect

                else:
                    if targetables[i] in p1.battlefield:
                        p1.battlefield.remove(targetables[i])
                    if targetables[i] in p2.battlefield:
                        p2.battlefield.remove(targetables[i])
                self.hand.pop(choice)


a = magicgame()
a.p1_hand = [0, 0, 1, 2]
a.p1_battlefield = [2 , 2, 2]   ==   [4 , 4 , 2 ,0]
print(a.p1_battlefield)
a.p1_play(0)
print(a.p1_battlefield)
