from gpiozero import OutputDevice
from time import sleep

if __name__ == "__main__":
    pinNum = 19
    pin = OutputDevice(pinNum)

    while(True):
        pin.on()
        sleep(1)
        pin.off()
        sleep(1)