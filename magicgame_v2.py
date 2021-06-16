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
        
        #phases for each player will be main phase 1, attacker phase, and blocking phase (1, 2, 3)
        self.phase = 1

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
        if card_choice == 0:
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
                self.p1_hand.remove(card_choice)
                self.p1_battlefield.append(0)

        elif card_choice == 1:
            # Play a spell, target choices are [p1, p2, p1 u_c, p1 t_c, p2 u_c, p2 t_C]
            # going from 1-6
            
            # First check to see if enough mana available to play spell
            manapool = 0
        
            for k in range(len(self.p1_battlefield)):
                if self.p1_battlefield[k] == 2:
                    if manapool < 1:
                        manapool += 1
            print("mana is ", manapool)
            if manapool < 1:
                print("You dont have enough untapped mana to play that")
            else:
                # Tap the appropriate mana
                tapper = 0
                for k in range(len(self.p1_battlefield)):
                    if self.p1_battlefield[k] == 2:
                        if tapper < 1:
                            self.p1_battlefield[k] = 4
                            tapper += 1

                # Based on choice, remove that amount of life or that kind of creature from
                # appopriate battlefield

                if target_choice == 1:
                    self.p1_life -= 3
                elif target_choice == 2:
                    self.p2_life -= 3
                elif target_choice == 3:
                    self.p1_battlefield.remove(0)
                elif target_choice == 4:
                    self.p1_battlefield.remove(3)
                elif target_choice == 5:
                    self.p2_battlefield.remove(0)
                elif target_choice == 6:
                    self.p2_battlefield.remove(3)
                else:
                    pass

                self.p1_hand.remove(card_choice)

        elif card_choice == 2:
            self.p1_landforturn == False
            if self.p1_landforturn == True:
                print("You have already played a land for turn")
            else:
                self.p1_hand.remove(card_choice)
                self.p1_battlefield.append(card_choice)
                self.landforturn = True

    def p2_play(self, card_choice, target_choice = 0):
        if card_choice == 0:
            manapool = 0
            for k in range(len(self.p2_battlefield)):
                if self.p2_battlefield[k] == 2:
                    # Check manacost of creature
                        if manapool < 2:
                            manapool +=1
            if manapool < 2:
                print("You dont have enough untapped mana to play that")
            else:
                tapper = 0
                for k in range(len(self.p2_battlefield)):
                    if self.p2_battlefield[k] == 2:
                        if tapper < 2:
                            self.p2_battlefield[k] = 4
                            tapper += 1
                self.p2_hand.remove(card_choice)
                self.p2_battlefield.append(0)

        elif card_choice == 1:
            # Play a spell, target choices are [p1, p2, p1 u_c, p1 t_c, p2 u_c, p2 t_C]
            # going from 1-6
            
            # First check to see if enough mana available to play spell
            manapool = 0
            
            for k in range(len(self.p2_battlefield)):
                if self.p2_battlefield[k] == 2:
                    if manapool < 1:
                        self.p2_battlefield[k] == 4
                        manapool +=1

            if manapool < 1:
                print("You dont have enough untapped mana to play that")
            else:
                # Tap the appropriate mana
                tapper = 0
                for k in range(len(self.p2_battlefield)):
                    if self.p2_battlefield[k] == 2:
                        if tapper < 1:
                            self.p2_battlefield[k] = 4
                            tapper += 1

                # Based on choice, remove that amount of life or that kind of creature from
                # appopriate battlefield

                if target_choice == 1:
                    self.p1_life = self.p1_life - 3
                elif target_choice == 2:
                    self.p2_life = self.p2_life - 3
                elif target_choice == 3:
                    if 0 in self.p1_battlefield: self.p1_battlefield.remove(0)
                elif target_choice == 4:
                    if 3 in self.p1_battlefield: self.p1_battlefield.remove(3)
                elif target_choice == 5:
                    if 0 in self.p2_battlefield: self.p2_battlefield.remove(0)
                else:
                    if 3 in self.p2_battlefield: self.p2_battlefield.remove(3)

                self.p2_hand.remove(card_choice)

        elif card_choice == 2:
            self.p2_landforturn == False
            if self.p2_landforturn == True:
                print("You have already played a land for turn")
            else:
                self.p2_hand.remove(card_choice)
                self.p2_battlefield.append(2)
                self.landforturn = True
    
    def nextphase(self):
        self.phase += 1
        if self.phase == 4:
            self.phase = 11
        elif self.phase == 14:
            self.phase = 1
        else:
            pass

    def p1_attack(self, num_attackers):
        tapper = 0
        for k in range(len(self.p1_battlefield)):
            if self.p1_battlefield[k] == 0:
                if tapper < num_attackers:
                    self.p1_battlefield[k] = 3
                    tapper += 1
        self.phase += 1

    def p2_attack(self, num_attackers):
        num_attack
        tapper = 0
        for k in range(len(self.p2_battlefield)):
            if self.p2_battlefield[k] == 0:
                if tapper < num_attackers:
                    self.p2_battlefield[k] = 3
                    tapper += 1
        self.phase += 1

    def p1_block(self, num_block, num_attack):
        counter = 0
        for k in range(num_block):
            self.p2_battlefield.remove(3)
            self.p1_battlefield.remove(0)
        damage = (num_attack - num_block) * 2
        self.p1.life -= damage
        self.phase = 1

    def p2_block(self, num_block, num_attack):
        counter = 0
        for k in range(num_block):
            self.p1_battlefield.remove(3)
            self.p2_battlefield.remove(0)
        damage = (num_attack - num_block) * 2
        self.p2_life -= damage
        self.phase = 11

    def p1_turn(self):
        for k in range(len(self.p1_battlefield)):
            if self.p1_battlefield[k] == 3:
                    self.p1_battlefield[k] = 0
            if self.p1_battlefield[k] == 4:
                    self.p1_battlefield[k] = 2

    def p2_turn(self):
        for k in range(len(self.p2_battlefield)):
            if self.p2_battlefield[k] == 3:
                    self.p2_battlefield[k] = 0
            if self.p2_battlefield[k] == 4:
                    self.p2_battlefield[k] = 2

    def show_battlefield(self):
        print("\n __________________________________________________________")
        print("\n", self.p2_hand)
        print("\n _____ P2 _____ Life: ", self.p2_life)
        for k in range(len(self.p2_battlefield)):
            if self.p2_battlefield[k] == 2:
                print("L", end = " ")
            elif self.p2_battlefield[k] == 4:
                print("l", end = " ")
        print("\n")
        for k in range(len(self.p2_battlefield)):
            if self.p2_battlefield[k] == 0:
                print("C", end = " ")
            elif self.p2_battlefield[k] == 3:
                print("c", end = " ")
        print("\n")
        for k in range(len(self.p1_battlefield)):
            if self.p1_battlefield[k] == 0:
                print("C", end = " ")
            elif self.p1_battlefield[k] == 3:
                print("c", end = " ")
        print("\n")
        for k in range(len(self.p1_battlefield)):
            if self.p1_battlefield[k] == 2:
                print("L", end = " ")
            elif self.p1_battlefield[k] == 4:
                print("l", end = " ")
        print("\n _____ P1 _____ Life: ", self.p1_life)
        print("\n", self.p1_hand)
        
a = magicgame()

while (a.p1_life and a.p2_life > 0) and (len(a.p2_deck) > 0):
    if a.phase == 1:
        a.show_battlefield()
        
        print("What does P1 want to play? 0 = creature, 1 = spell (and target of P1 = 1, P2 = 2, \
            P1 U creature = 3, P1 T creature = 4, P2 U creature = 5, P2 T creature = 6),\
                 2 = land, 8 = pass phase")
        x = int(input())
        y = 0

        if x == 1:
            print("Target?")
            y = int(input())
            a.p1_play(x, y)
        if x == 8:
            a.nextphase()
        else:
            a.p1_play(x)
    elif a.phase == 2:
        a.show_battlefield()
        print("How many P1 attackers? Any N attackers, 0 is pass")
        global num_attack
        num_attack = int(input())
        a.p1_attack(num_attack)
    elif a.phase == 3:
        if num_attack == 0:
            a.nextphase()
            pass
        else:
            a.show_battlefield()
            print("How many P2 blockers? Any N blockers, 0 is pass")
            x = int(input())
            a.p2_block(x, num_attack)
        a.p2_turn()
        a.p2_draw()

    if a.phase == 11:
        a.show_battlefield()

        print("What does P2 want to play? 0 = creature, 1 = spell (and target of P1 = 1, P2 = 2, \
            P1 U creature = 3, P1 T creature = 4, P2 U creature = 5, P2 T creature = 6),\
                 2 = land, 8 = pass phase")

        x = int(input())
        y = 0

        if x == 1:
            print("Target?")
            y = int(input())
            a.p2_play(x, y)
        if x == 8:
            a.nextphase()
        else:
            a.p2_play(x)
    elif a.phase == 12:
        a.show_battlefield()
        print("How many P2 attackers? Any N attackers, 0 is pass")
        num_attack = int(input())
        a.p2_attack(num_attack)
    elif a.phase == 13:
        if num_attack == 0:
            a.nextphase()
            pass
        else:
            a.show_battlefield()
            print("How many P1 blockers? Any N blockers, 0 is pass" )
            x = int(input())
            a.p1_block(x, num_attack)
        a.p1_turn()
        a.p1_draw()
    else:
        pass

# Winner / Loser
if a.p1_life < 1:
    print("P1 loses, P2 wins")
elif a.p2_life < 1:
    print("P2 loses, P2 wins")
elif len(a.p2_deck) < 0:
    print("P2 has no more cards in library, P1 wins")