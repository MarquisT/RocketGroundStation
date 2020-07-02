import time
from Test_Communicator import Communicator

class Rocket:

    def __init__(self):
        self._is_changed = False
        self._is_launched = False
        self._is_ready = True   # Change this to enable launch
        self.timestamps = []
        self.temps = []
        self.air_pressure = []
        self.launchTime = False

        self._communicator = Communicator(self)

    def is_changed(self):
        self.load_new_data()

        if self._is_changed:
            self._is_changed = False    # Reset the Flag for next time.
            return True
        return False        # Return False if it wasn't true above.
    def load_new_data(self):
        self._communicator.refresh()


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

