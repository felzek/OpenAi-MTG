
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
        self.showhand()
        choice = input("Enter the number of the card you want to play: ")
        choice = int(choice)

        if self.hand[choice].cardtype == "creature":
            print("You chose a creature to play")
            card = self.hand.pop(choice)
            self.battlefield.append(card)

        elif self.hand[choice].cardtype  == "spell":
            print("You chose a spell to play")
            target = input("Choose a target # (any creature or player)")
            target = int(target)
            print(targetables)
            if target == 1:
                targetables[1].life = targetables[1].life - self.hand[choice].effect

            elif target == 2:
                p2.life = p2.life - self.hand[choice].effect
        elif self.hand[choice].cardtype == "land":
            print("You chose a land to play")
            card = self.hand.pop(choice)
            self.battlefield.append(card)

        else:
            print("You have no hand!")

    
class card:
    def __init__(self, id, cardtype):
        self.status = "untapped"
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
    print("\n __________ P1 ____________")

    for i in range(len(p1.battlefield)):
            print(p1.battlefield[i].cardtype, i + 2, end=" ")
    
    print("\n - - - - - - - - - - ")

    for i in range(len(p2.battlefield)):
            print(p2.battlefield[i].cardtype, i + len(p1.battlefield) + 2, end=" ")

    print("\n __________ P2 _____________")