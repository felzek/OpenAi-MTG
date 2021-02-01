from magicgame import *
import os
import random
os.system('cls')

p1 = player("p1")
p1.builddeck(60, 20, 20)
random.shuffle(p1.deck)
p1.draw(7)

p2 = player("p2")
p2.builddeck(60, 20, 20)
random.shuffle(p2.deck)
p2.draw(7)

targetables = [p1, p2]
print(targetables)
print(targetables[1].life)

testcreature = card(500, "creature")
p1.battlefield.append(testcreature)

p2.play()
showbattlefield(p1, p2)
