import numpy as np
import cv2
from gpiozero import InputDevice
from time import sleep, strftime


if __name__ == "__main__":
    # Tunables
    fps = 10
    capture_length = 30

    # OpenCV setup
    frame_size = (int(cap.get(3)), int(cap.get(4)))    
    timestr = strftime("%Y%m%d-%H%M%S")
    output_file = f"video_{timestr}"

    cap = cv2.VideoCapture(0) # Create video capture object with 0th camera
    fourcc = cv2.VideoWriter_fourcc(*'MJPG') # Create VideoWriter format object with smallest file size
    out = cv2.VideoWriter(output_file, fourcc, fps, frame_size) # fps on write and wait on read should match? frame size?

    # PIR Setup
    PIRPinNum = 26
    PIR = DigitalInputDevice(PIRPinNum, pull_up=False)

    # LED Setup
    LEDPinNum = 19
    LED = OutputDevice(LEDPinNum)

    # MAIN LOOP
    while(True):
        # Check if motion is sensed
        if(pir.is_active):
            timer = 0
            while(timer < capture_length*fps):
                # If we detect more motion we reset the timer
                if(pir.is_active):
                    timer = 0
                
                # Capture frame
                if(cap.isOpened()):
                    ret, frame = cap.read()
                    if ret==True:
                        out.write(frame)

                else:
                    exit()
                # Sleep and increment 
                sleep(1/fps)
                timer += 1
            
            # If PIR was triggered for longer than capture length so save
            if(timer > capture_length*fps):
                timestr = strftime("%Y%m%d-%H%M%S")
                output_file = f"video_{timestr}"
                out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)
            
            # Else we detected something other than cat so clear VideoWriter
            else:

        sleep(1/fps)


    cap.release()
    out.release()
    cv2.destroyAllWindows()