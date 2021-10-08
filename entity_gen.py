# this is proof of concept I realize the method is dogshit dont bother me about it, I just needed the datasets for now to see if it will even work
import random
import csv
from pairing_functions import szudzik

requested_amount = int(input("How many entities should be created? (int): "))
complexity = 10

'''
Three trait axis:
- aggression
- morality
- wanderlust
'''

# npc class with name, plus traits
class Entity:
    def __init__(self, name, aggression, morality, wanderlust):
        self.name = name
        self.aggression = aggression
        self.morality = morality
        self.wanderlust = wanderlust
        
        # use pairing functions to create behavior digit (szudzik is slightly faster)
        self.behavior = szudzik.pair(self.aggression, self.morality, self.wanderlust)
        

# loop creation of NPC objects
with open('entities.csv', 'w') as f:
    i = 0
    entity_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    entity_writer.writerow(['Name', 'Behavior ID', 'Aggression', 'Morality', 'Wanderlust'])
    while i < requested_amount:
        name = f"npc#{i}"
        entity = Entity(name, random.randint(0, complexity), random.randint(0, complexity), random.randint(0, complexity))
        entity_writer.writerow([entity.name, entity.behavior, entity.aggression, entity.morality, entity.wanderlust])
        i += 1
        
'''
Career choices:

'''