# this is proof of concept I realize the method is dogshit dont bother me about it, I just needed the datasets for now to see if it will even work
import random
import csv

requested_amount = int(input("How many entities should be created? (int): "))
complexity = 10

'''
Two trait axis:
- aggression
- morality
- wanderlust

Four jobs quadrants:
   a,  m = security
   a, -m = pirate
  -a,  m = trading
  -a, -m = smuggling
'''

# npc class with name, plus traits
class NPC:
    def __init__(self, name, aggression, morality, wanderlust):
        self.name = name
        self.aggression = aggression
        self.morality = morality
        self.wanderlust = wanderlust
        

# loop creation of NPC objects
i = 0
        
while i < requested_amount:
    name = f"npc#{i}"
    entity = NPC(name, random.randint(-complexity, complexity), random.randint(-complexity, complexity), random.randint(-complexity, complexity))
    