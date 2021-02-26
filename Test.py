# from magicgame import *
import os
import random
from enum import Enum
os.system('cls')


p1 = []
p2 = []

class match:
    def __init__(self, player1, player2):
        pass

class player:
    def __init__(self, playername):
        self.name = playername
        self.decknum = 60
        self.life = 20
        print(playername,"has started with", self.decknum, "cards and", \
            self.life, "life")

        self.battlefield = []
        self.hand = []
        self.deck = []
        self.landforturn = False

    def builddeck(self, decknum, creature_number, spell_number):
        print("A Deck with", creature_number, "creatures,", spell_number, "spells and", \
              decknum - creature_number - spell_number ,"lands in deck.")
        for s in ["creature", "spell", "land"]:
            cardtype = s
            if s == "creature":
                for i in range(creature_number):
                    c = creature(i, s)
                    self.deck.append(c)
            elif s == "spell":
                for j in range(creature_number, spell_number + creature_number):
                    c = spell(j, s)
                    self.deck.append(c)
            else:
                for k in range(creature_number + spell_number, decknum):
                    c = land(k, s)
                    self.deck.append(c)

    def showdeck(self):
        print("Showing deck for ", self.name)
        for i in range(self.decknum):
            print(self.deck[i].cardtype, i)

    def showhand(self):
        print("Showing hand for ", self.name)
        for i in range(len(self.hand)):
            print(self.hand[i].cardtype, i)

    def draw(self, number_draw = 1):
        for i in range(number_draw):
            self.hand.append(self.deck.pop(0))

    def play(self, card_to_play = 0):
        choice = input("Enter the number on the card you want to play: ")
        choice = int(choice)

        # Check if mana is available to do that action, if yes then the spell is cast and leaves hand
        if self.hand[choice].cardtype == "creature":
            manapool = 0
            for k in range(len(self.battlefield)):
                if isinstance(self.battlefield[k], land):
                    if self.battlefield[k].untapped:
                        if manapool < self.hand[choice].manacost:
                            manapool +=1
            if manapool < self.hand[choice].manacost:
                print("You dont have enough untapped mana to play that")
            else:
                tapper = 0
                for k in range(len(self.battlefield)):
                    if isinstance(self.battlefield[k], land):
                        if self.battlefield[k].untapped:
                            if tapper < self.hand[choice].manacost:
                                self.battlefield[k].untapped = False
                                tapper += 1
                card = self.hand.pop(choice)
                self.battlefield.append(card)

        elif self.hand[choice].cardtype  == "spell":
            print("You chose a spell to play")
            target = input("Choose a target # (any creature or player) : ")
            i = int(target) - 1
            targetables = [p1, p2]
            targetables.extend(p1.battlefield + p2.battlefield)

            manapool = 0
            for k in range(len(self.battlefield)):
                if isinstance(self.battlefield[k], land):
                    if self.battlefield[k].untapped:
                        if manapool < self.hand[choice].manacost:
                            self.battlefield[k].untapped = False
                            manapool +=1
                            print("1 mana added")
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
            
        elif self.hand[choice].cardtype == "land":
            if self.landforturn == True:
                print("You have already played a land for turn")
            else:
                print("You chose a land to play")
                card = self.hand.pop(choice)
                self.battlefield.append(card)
                self.landforturn = True

        else:
            print("You have no hand!")

        showbattlefield(p1, p2)
        self.showhand()

    
class card:
    def __init__(self, id, cardtype):
        self.untapped = True
        self.id = id
        self.cardtype = cardtype
        self.handposition = 0
        self.battlefieldposition = 0
		

    def show(self):
        print("Card with ID {} is of type {}".format(self.id, self.cardtype))

    def play(self):
        if self.type == "permanent":
            player.zone.battlefield.append(card)

class creature(card):
    def __init__(self, id, cardtype):
        super().__init__(id, cardtype)
        self.type = "permanent"
        self.stats = [2, 2]
        self.manacost = 2

    def attack(card):
        if card.status == "untapped":
            card.status = "attacking"

    def block(self):
        if card.status == "untapped":
            card.status = "blocking"

class spell(card):
    def __init__(self, id, cardtype):
        super().__init__(id, cardtype)
        self.type = "nonpermanent"
        self.effect = 3
        self.manacost = 1

    def target(target):
        if isinstance(target, creature):
            player.battlefield.remove(target)

        if isinstance(target, player):
            player.life = player.life - self.effect

class land(card):
    def __init__(self, id, cardtype):
        super().__init__(id, cardtype)
        self.type = "permanent"
        self.mana = 1

def showbattlefield(p1, p2):
    print("\n __________ P1 | ", p1.life, " ____________")

    for i in range(len(p1.battlefield)):
            if p1.battlefield[i].untapped:
                untapped = "U"
            else:
                untapped = "t"
            print(p1.battlefield[i].cardtype, i + 3, untapped, end="   ")
    
    print("\n - - - - - - - - - - ")

    for i in range(len(p2.battlefield)):
            if p2.battlefield[i].untapped:
                untapped = "U"
            else:
                untapped = "t"
            print(p2.battlefield[i].cardtype, i + len(p1.battlefield) + 3, untapped, end="   ")

    print("\n __________ P2 | ", p2.life, " _____________ \n")


p1 = player("p1")
p1.builddeck(60, 20, 20)
random.shuffle(p1.deck)
p1.draw(7)

p2 = player("p2")
p2.builddeck(60, 20, 20)
random.shuffle(p2.deck)
p2.draw(7)

targetables = [p1, p2]
test1 = creature(500, "creature")
test2 = creature(501, "creature")
test3 = land(502, "land")
p2.battlefield.extend([test1, test2, test3])
targetables.extend([test1, test2, test3])

showbattlefield(p1, p2)
p2.showhand()
p2.play()
p2.play()
p2.play()
p2.play()


