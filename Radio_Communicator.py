import serial
import threading
import re


class Communicator():



    def __init__(self, rocket):

        print("Real Communicator")
        self.ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 115200, timeout=1)
        self.rocket = rocket

        thread = threading.Thread(target=self.read_from_port).start()

    def read_from_port(self):

        while not self.rocket._is_done:

            reading = self.ser.readline().decode()
            self.handleIncomingData(reading)

        print("Shutting down Communicator")
        return

    def refresh(self):
        pass

    def handleIncomingData(self, data):
        print(data)

        if "Ready - ACK send":
            self.rocket.set_is_ready()
        if "Data:" in data:
            #print("We need to process data", data)

            data_array = re.findall(r'\[.*?\]', data)[2]  #


            self.rocket.temps.append(float(re.findall(',T=(\d+)', data_array)[0])/100)
            self.rocket.air_pressure.append(float(re.findall(',P=(\d+)', data_array)[0])/100)
            self.rocket.timestamps.append(re.findall('ET=(\d+)', data_array)[0])
            #self.rocket.messages.append("Asdasdad")
            self.rocket.signalStrength.append(re.findall(r':(-[0-9]+)', data)[0])
            self.rocket._is_changed = True



    def sendLaunchCommand(self):
        self.ser.write('l\r'.encode())
        # self.rocket.message.append(ser_bytes.decode('utf-8'))



