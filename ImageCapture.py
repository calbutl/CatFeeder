import numpy as np
import cv2
from gpiozero import DigitalInputDevice, OutputDevice
from time import sleep, strftime


if __name__ == "__main__":
    # Tunables
    fps = 10

    # Video Reader Initial Setup
    cap = cv2.VideoCapture(0) # Create video capture object with 0th camera
    frame_size = (int(cap.get(3)), int(cap.get(4)))   

    # Video Writer Initial Setup
    fourcc = cv2.VideoWriter_fourcc(*'MJPG') # Create VideoWriter format object with smallest file size

    # PIR Setup
    PIRPinNum = 26
    PIR = DigitalInputDevice(PIRPinNum, pull_up=False)

    # LED Setup
    LEDPinNum = 19
    LED = OutputDevice(LEDPinNum)


    INACTIVE_THRESHOLD = 10*fps # frames
    inactive_time = 10*fps # frames
    rolling = False


    while(cap.isOpened()):

        # if there is movement and we're not rolling
        if PIR.is_active and not rolling:
            inactive_time = 0
            rolling = True
            LED.on()

            output_path = "images/TrainingCollection"
            timestr = strftime("%Y%m%d-%H%M%S")
            output_file = f"video_{timestr}.avi"
            out = cv2.VideoWriter(f"{output_path}/{output_file}", fourcc, fps, frame_size)

        # if we're rolling
        if inactive_time < INACTIVE_THRESHOLD:
            ret, frame = cap.read()
            if ret==True:
                out.write(frame)

            if(PIR.is_active):
                inactive_time = 0
            else:
                inactive_time +=1

        # if we're done rolling
        else:
            rolling = False
            LED.off()
            out.release()

        sleep(1/fps)


    cap.release()
    cv2.destroyAllWindows()