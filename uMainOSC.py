import P3picam
import picamera
from datetime import datetime
import time
import argparse
from pythonosc import osc_message_builder
from pythonosc import udp_client

motionState = False
sleepTime = 5

#Log
logFilePath = "/home/pi/Desktop/UNLP/umbilical1-1/logActividad.txt"
logFile = open(logFilePath,"a")
activarLog = True

def datahora():
    currentTime = datetime.now()
    return "%02d/%02d/%04d,%02d,%02d,%02d\n" % (currentTime.day, currentTime.month, currentTime.year, currentTime.hour, currentTime.minute, currentTime.second)

#OSC
oscPath = "/layer3/clip1/connect/"
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.0.4",help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=7000,help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)

print("Iniciando Loop")

try:
    while True:
        motionState = P3picam.motion()
        if motionState:
            client.send_message(oscPath, 1)
            currentTime = datetime.now()
            print("Usuario detectado - " + datahora())
            if activarLog:
                logFile.write("OK," + datahora()) 
            time.sleep(sleepTime)
        else:
            client.send_message(oscPath, 0)
            print("Fuera de rango")

except KeyboardInterrupt:
    logFile.write("ERR," + datahora()) 
    logFile.close()
    time.sleep(1)