from gpiozero import OutputDevice
from gpiozero import DigitalInputDevice
from time import sleep

def turnOnLED():
    LED.on()

def turnOffLED():
    LED.off()

if __name__ == "__main__":
    PIRPinNum = 26
    PIR = DigitalInputDevice(PIRPinNum, pull_up=False)

    LEDPinNum = 19
    LED = OutputDevice(LEDPinNum)

    PIR.when_activated = turnOnLED
    PIR.when_deactivated = turnOffLED

    while(True):
        print(LED.value)
        sleep(0.25)
