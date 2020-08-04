import time
#import csv
import pickle
import datetime

from Test_Communicator import Communicator

class Rocket:

    def __init__(self, pressure):
        self._is_changed = False
        self._is_launched = False
        self._is_done = False # This is for the real communcator to allow it gracefully kill the radio. Otherwise it hangs.
        self.timestamps = []
        self.temps = []
        self.air_pressure = []
        self.signal_strength = []
        self.launchTime = False
        self.messages = []
        self.sea_level_pressure = pressure
        self.altitude = []
        self.launchDate = False
        self.ground_station_elevation = False

        self._communicator = Communicator(self)


    def set_timestamp(self, timestamp):
        self.timestamps.append(timestamp)

    def set_temp(self, temp):
        self.temps.append(temp)


    def set_air_pressure(self, pressure):
        self.air_pressure.append(pressure)

    def set_signal_strength(self, signal):
        self.signal_strength.append(signal)

    def set_altitude(self, new_alt):
        self.altitude.append(new_alt)

    def get_status(self):

        status = {}
        status["Temperature"] = self.temps[-1:]
        status["Pressure"] = self.air_pressure[-1:]
        status["ASL"] = self.altitude[-1:]
        status["Signal"] = self.signal_strength[-1:]
        status["Height"] = self.calculate_height()

        return status


    def saveData(self):

        self._is_done = True

        if self.launchDate:
            with open('flight_data_{}.pickle'.format(self.launchDate.today()), 'wb') as flight_data_file:
                pickle.dump(self, flight_data_file)





    def is_changed(self):
        self.load_new_data()

        if self._is_changed:
            self.set_altitude(self.calculate_altitude())
            self._is_changed = False    # Reset the Flag for next time.
            return True
        return False        # Return False if it wasn't true above.

    def load_new_data(self):
        self._communicator.refresh()


    def calculate_altitude(self):
        print("we have {} and {} ".format(self.air_pressure[-1:][0], self.sea_level_pressure))
        altitude = 44330 * (1.0 - pow(((self.air_pressure[-1:][0]*100) / self.sea_level_pressure), 0.1903));
        return round(altitude, 1)

    def calculate_height(self):
        if self.ground_station_elevation == False:
            if(len(self.altitude)<1):
                return 0

            else:
                print("First is", self.altitude)
                print("Second is", self.altitude[0])

                self.ground_station_elevation = self.altitude[0]
        if len(self.altitude)<2:
            return 0

        return round(self.altitude[-1:][0] - self.ground_station_elevation, 1)


    def getAirTime(self):
        if self.launchTime:
            return time.time() - self.launchTime
        return "Null"

    #def set_is_ready(self):

   #    self._is_ready = True

    def is_ready(self):
        return self._communicator.check_if_last_ready_in_seconds(2)
        #we need to check when the last is ready signal was recieved






        #return self._is_ready

    def is_launched(self):
        return self._is_launched

    def launch(self):
        self._is_launched = True
        self.launchTime = time.time()
        self.launchDate = datetime.datetime.now()
        self._communicator.sendLaunchCommand()

