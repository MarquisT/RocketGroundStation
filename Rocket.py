import time

class Rocket:

    def __init__(self):
        self._is_launched = False
        self._is_ready = True   # Change this to enable launch
        self.timestamps = []
        self.temps = []
        self.air_pressure = []
        self.launchTime = False



    def getAirTime(self):
        if self.launchTime:
            return time.time() - self.launchTime
        return "Null"

    def is_ready(self):
        return self._is_ready

    def is_launched(self):
        return self._is_launched

    def launch(self):
        self._is_launched = True
        self.launchTime = time.time()

