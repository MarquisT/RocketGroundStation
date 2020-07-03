import random

class Communicator():



    def __init__(self, rocket):

        print("Test Communicator")
        self.rocket = rocket


    def refresh(self):

        if random.random() > 0.9:
            self.rocket.temps.append(round(random.uniform(10, 30), 2))
            self.rocket.air_pressure.append(round(random.uniform(1000, 1100),2))
            self.rocket._is_changed = True