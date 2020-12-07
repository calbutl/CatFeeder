from gpiozero import OutputDevice
from gpiozero import DigitalInputDevice
from time import sleep

if __name__ == "__main__":
    PIRPinNum = 26
    PIR = DigitalInputDevice(PIRPinNum, pull_up=False)

    LEDPinNum = 19
    LED = OutputDevice(LEDPinNum)

    while(True):
        if(PIR.is_active == 1):
            LED.on()
        else:
            LED.off()
        print(LED.value)
        sleep(0.25)
