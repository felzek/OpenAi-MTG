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
    # u = untapped, t = tapped, c = creature, l = land, s = spell
    t_c = u_c # tapped creature to untapped creature
    t_l = u_l # tapped land to untapped land
    #upkeep is not important right now
    #if player 1's turn then [on very first turn, you don't get to draw a card] 
    p1_draw(1)
    #if player 2's turn then
    p2_draw(1)

# main phase I
class mainPhaseOne(Enum):
    play_l = 5 # play land (only allowed to do once per turn)
    play_c = 0 #  use land as mana to play a creature or spell
    play_s_u_c = 1
    play_s_t_c = 2
    play_s_self = 3
    play_s_opp = 4

# combat phase
class combatPhase(Enum):
    # player who's turn it is chooses to attack with creature
    # other player either blocks with untapped creature or takes the hit
    attack_c = 6
    # if choose to block
    block_u_c = 7
    # if choose not to block
    p2.life -= 1 #player who's turn it is not loses a life point

# main phase II
class mainPhaseTwo(Enum):
    # play a land if you didn't do it during main phase I
    play_l = 5
    # everything else is exactly the same as phase I
    play_c = 0 #  use land as mana to play a creature or spell
    play_s_u_c = 1
    play_s_t_c = 2
    play_s_self = 3
    play_s_opp = 4

# discard phase
class discardPhase(Enum):
    # if you have more than 7 cards in your hand. get rid of one of them
    # insert code to make that happen here

#end of turn could technically be a phase but we have nothing to do in this because of our simplified setup