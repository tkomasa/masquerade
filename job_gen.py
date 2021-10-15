# this is proof of concept I realize the method is dogshit dont bother me about it, I just needed the datasets for now to see if it will even work
import random
import csv
from pairing_functions import szudzik
import time

requested_amount = int(input("How many entities should be created? (int): "))  # just for testing
complexity = 10  # simply defines how high a number the random trait values can go to, cannot be negative


def generate_jobs(num_jobs, complexity):
    class Job:
        def __init__(self, name, aggression, morality, distance):
            self.name = name
            self.aggression = aggression
            self.morality = morality
            self.distance = distance
            self.reward = random.randint(100, 10000)
            
            # assign the human-understandable job type
            self.job_type = ""
            
            # use pairing functions to create behavior digit (szudzik is slightly faster)
            self.behavior = szudzik.pair(self.aggression, self.morality, self.distance)
            
    # start of timer
    start_time = time.time_ns()


    # loop creation of NPC objects
    with open('jobs.csv', 'w') as f:
        i = 0
        job_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        job_writer.writerow(['Name', 'Behavior ID', 'Aggression', 'Morality', 'Distance', 'Reward'])
        while i < num_jobs:
            job = Job(f"job#{i}", random.randint(0, complexity), random.randint(0, complexity), random.randint(0, complexity))
            job_writer.writerow([job.name, job.behavior, job.aggression, job.morality, job.distance, job.reward])
            i += 1
            
    # end of timer
    stop_time = time.time_ns()
    elapsed_time = (int(stop_time - start_time)) / 1000000000
    print(f"Finished generation of {requested_amount} entities in {elapsed_time} seconds.")
    

generate_jobs(requested_amount, complexity)
