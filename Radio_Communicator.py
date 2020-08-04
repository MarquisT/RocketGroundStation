import serial
import threading
import re
import time

class Communicator():



    def __init__(self, rocket):

        print("Real Communicator")
        self.ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 115200, timeout=1)
        self.rocket = rocket
        self.lastReadySignal = False

        thread = threading.Thread(target=self.read_from_port).start()

    def read_from_port(self):
        print("reading from port")
        while not self.rocket._is_done:

            try:
                reading = self.ser.readline().decode()
                if reading:
                    self.handleIncomingData(reading)

            except serial.SerialException:  # catch error and ignore it
                print('uh oh', )




        print("Shutting down Communicator")
        return

    def refresh(self):
        pass

    def handleIncomingData(self, data):
        if not data:
            print("Emtpy data", data)
            return

        if "Ready - ACK sent" in data:
            print("We received a ready signal", data)
            self.lastReadySignal = time.time()
           # self.rocket.set_is_ready()
        if "Data:" in data:
            print("We need to process data", data)

            data_array = re.findall(r'\[.*?\]', data)[2]  #
            print(data_array)

            self.rocket.temps.append(float(re.findall(',T=(\d+)', data_array)[0])/100)
            self.rocket.air_pressure.append(float(re.findall(',P=(\d+)', data_array)[0])/100)
            self.rocket.timestamps.append(re.findall('ET=(\d+)', data_array)[0])
            #self.rocket.messages.append("Asdasdad")
            self.rocket.signal_strength.append(re.findall('RX_RSSI:(-\d+)', data)[0])
            self.rocket._is_changed = True



    def sendLaunchCommand(self):
        self.ser.write('l\r'.encode())
        # self.rocket.message.append(ser_bytes.decode('utf-8'))


    def check_if_last_ready_in_seconds(self, seconds):

        if self.lastReadySignal:
            if time.time() > self.lastReadySignal + seconds:
                return False
            return True
        return False
