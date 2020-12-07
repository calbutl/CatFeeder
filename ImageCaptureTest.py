import numpy as np
import cv2
from time import sleep, strftime

if __name__ == "__main__":
    fps = 10
    timestr = strftime("%Y%m%d-%H%M%S")
    output_file = f"images/video_{timestr}.avi"

    cap = cv2.VideoCapture(0) # Create video capture object with 0th camera
    frame_size = (int(cap.get(3)), int(cap.get(4)))


    fourcc = cv2.VideoWriter_fourcc(*'MJPG') # Create VideoWriter format object with smallest file size
    out = cv2.VideoWriter(output_file, fourcc, fps, frame_size) # fps on write and wait on read should match? frame size?

    for _ in range(200):
        if(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Display video we just saved.
cap = cv2.VideoCapture(output_file)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

cap.release()
cv2.destroyAllWindows()