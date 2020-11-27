import numpy as np
import cv2
from gpiozero import InputDevice
from time import sleep, strftime


if __name__ == "__main__":
    fps = 10
    frame_size = (640,480)
    timestr = strftime("%Y%m%d-%H%M%S")
    output_file = f"video_{timestr}"

    cap = cv2.VideoCapture(0) # Create video capture object with 0th camera
    fourcc = cv2.VideoWriter_fourcc(*'X264') # Create VideoWriter format object with smallest file size
    out = cv2.VideoWriter(output_file, fourcc, fps, frame_size) # fps on write and wait on read should match? frame size?

    pinNumber = 3
    pir = InputDevice(pinNumber, pull_up=True, active_state=True)

    while(cap.isOpened()):
        # Check if motion is sensed
        if(pir.is_active):
            triggered = True
            ret, frame = cap.read()
            if ret==True:
                out.write(frame)
        else:
            if(triggered):
                timestr = strftime("%Y%m%d-%H%M%S")
                output_file = f"video_{timestr}"
                out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)
                triggered = False

        sleep(1/fps)


    cap.release()
    out.release()
    cv2.destroyAllWindows()