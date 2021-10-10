# this is proof of concept I realize the method is dogshit dont bother me about it, I just needed the datasets for now to see if it will even work
import random
import csv
from pairing_functions import szudzik
import time

requested_amount = int(input("How many entities should be created? (int): "))
complexity = 10

# npc class with name, plus traits
class Entity:
    def __init__(self, name, aggression, morality, wanderlust, greed):
        self.name = name
        self.aggression = aggression
        self.morality = morality
        self.wanderlust = wanderlust
        self.greed = greed
        
        # use pairing functions to create behavior digit (szudzik is slightly faster)
        self.behavior = szudzik.pair(self.aggression, self.morality, self.wanderlust)
        
# start of timer
start_time = time.time_ns()


# loop creation of NPC objects
with open('entities.csv', 'w') as f:
    i = 0
    entity_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    entity_writer.writerow(['Name', 'Behavior ID', 'Aggression', 'Morality', 'Wanderlust', 'Greed'])
    while i < requested_amount:
        entity = Entity(f"npc#{i}", random.randint(0, complexity), random.randint(0, complexity), random.randint(0, complexity), random.randint(0, complexity))
        entity_writer.writerow([entity.name, entity.behavior, entity.aggression, entity.morality, entity.wanderlust, entity.greed])
        i += 1
        
# end of timer
stop_time = time.time_ns()
elapsed_time = (int(stop_time - start_time)) / 1000000000
print(f"Finished generation of {requested_amount} entities in {elapsed_time} seconds.")