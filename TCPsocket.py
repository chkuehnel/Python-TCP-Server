import socket
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# and the Mapping to Signals A-D and ON/OFF
Pins={ 'A': 14, 'B':15, 'C':18, 'D':25, 'ON': 24, 'OFF':23 }

# Define Status
Status = ["", "", "", "", "end"]

# Set all pins as output

GPIO.setup(Pins['A'],GPIO.OUT)
GPIO.setup(Pins['B'],GPIO.OUT)
GPIO.setup(Pins['C'],GPIO.OUT)
GPIO.setup(Pins['D'],GPIO.OUT)
GPIO.setup(Pins['ON'],GPIO.OUT)
GPIO.setup(Pins['OFF'],GPIO.OUT)

start = 1

# To enable a plug the pins for the chosen plug and the
# one for the on signal have to be HIGH
def Setter(data_str):
    if "oneOn" in data_str:
        print("1on")
        Status[0] = "1on"
        GPIO.output(Pins['A'], 1)
        GPIO.output(Pins['ON'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['A'], 0)
        GPIO.output(Pins['ON'], 0)
    if "1off" in data_str:
        print("1off")
        Status[0] = "1off"
        GPIO.output(Pins['A'], 1)
        GPIO.output(Pins['OFF'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['A'], 0)
        GPIO.output(Pins['OFF'], 0)
    if "2on" in data_str:
        print("2on")
        Status[1] = "2on"
        GPIO.output(Pins['B'], 1)
        GPIO.output(Pins['ON'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['B'], 0)
        GPIO.output(Pins['ON'], 0)
    if "2off" in data_str:
        print("2off")
        Status[1] = "2off"
        GPIO.output(Pins['B'], 1)
        GPIO.output(Pins['OFF'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['B'], 0)
        GPIO.output(Pins['OFF'], 0)
    if "3on" in data_str:
        print("3on")
        Status[2] = "3on"
        GPIO.output(Pins['C'], 1)
        GPIO.output(Pins['ON'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['C'], 0)
        GPIO.output(Pins['ON'], 0)
    if "3off" in data_str:
        print("3off")
        Status[2] = "3off"
        GPIO.output(Pins['C'], 1)
        GPIO.output(Pins['OFF'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['C'], 0)
        GPIO.output(Pins['OFF'], 0)
    if "4on" in data_str:
        print("4on")
        Status[3] = "4on"
        GPIO.output(Pins['D'], 1)
        GPIO.output(Pins['ON'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['D'], 0)
        GPIO.output(Pins['ON'], 0)
    if "4off" in data_str:
        print("4off")
        Status[3] = "4off"
        GPIO.output(Pins['D'], 1)
        GPIO.output(Pins['OFF'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['D'], 0)
        GPIO.output(Pins['OFF'], 0)
    if "6on" in data_str:
        print("MasterOn START")
        Status[0] = "1on"
        Status[1] = "2on"
        Status[2] = "3on"
        Status[3] = "4on"
        GPIO.output(Pins['A'], 1)
        GPIO.output(Pins['ON'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['A'], 0)
        GPIO.output(Pins['B'], 1)
        time.sleep(0.1)
        GPIO.output(Pins['B'], 0)
        GPIO.output(Pins['C'], 1)
        time.sleep(0.1)
        GPIO.output(Pins['C'], 0)
        GPIO.output(Pins['D'], 1)
        time.sleep(0.1)
        GPIO.output(Pins['D'], 0)
        GPIO.output(Pins['ON'], 0)
        print("MasterOn DONE")
    if "6off" in data_str:
        print("MasterOff START")
        Status[0] = "1off"
        Status[1] = "2off"
        Status[2] = "3off"
        Status[3] = "4off"
        GPIO.output(Pins['A'], 1)
        GPIO.output(Pins['OFF'], 1)
        time.sleep(0.5)
        GPIO.output(Pins['A'], 0)
        GPIO.output(Pins['B'], 1)
        time.sleep(0.1)
        GPIO.output(Pins['B'], 0)
        GPIO.output(Pins['C'], 1)
        time.sleep(0.1)
        GPIO.output(Pins['C'], 0)
        GPIO.output(Pins['D'], 1)
        time.sleep(0.1)
        GPIO.output(Pins['D'], 0)
        GPIO.output(Pins['OFF'], 0)
        print("MasterOff DONE")
    if "act" in data_str:
	    for x in range(0, 5):
		    komm.send(Status[x] + '\n')
		    print(Status[x])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50000))
s.listen(1)

try:

    while True:
        if start == 1:
            Setter("6on")
            start = 0
        komm, addr = s.accept()
        merker = 0
        while True:
            data = komm.recv(1024)
            
            data_str1 = str(data)
            Setter(data_str1)
            if "act" in data_str1:
                merker = 1
            time.sleep(0.5)
            
            if not data:
                komm.close()
                break


except KeyboardInterrupt:
    GPIO.cleanup()
    
#except: s.close()
finally:
    s.close()

print("ende")
