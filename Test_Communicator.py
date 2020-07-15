import random

class Communicator():



    def __init__(self, rocket):

        print("Test Communicator")
        self.rocket = rocket
        self.rocket.set_is_ready()

    def sendLaunchCommand(self):
        pass

    def refresh(self):

        if random.random() > 0.9:
            ''' OLD 
            self.rocket.temps.append(round(random.uniform(10, 30), 2))
            self.rocket.air_pressure.append(round(random.uniform(1000, 1100),2))
            self.rocket.timestamps.append(self.rocket.getAirTime())
            self.rocket.messages.append("Asdasdad")
            self.rocket.signalStrength.append(65)
            self.rocket._is_changed = True
            '''

            #### NEW
            self.rocket.set_temp(round(random.uniform(10, 30), 2))
            self.rocket.set_air_pressure(round(random.uniform(1000, 1100), 2))
            self.rocket.set_timestamp(self.rocket.getAirTime())
            self.rocket._is_changed = True