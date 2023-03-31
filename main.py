"""Departure Warning System with a Monocular Camera"""


from top_level_lane_detection import *
import cv2
import serial
import time

input_video = "examples/project_video.mp4"


try:
    # Open a serial port with the same baud rate that you used in the Arduino sketch
    ser = serial.Serial('COM7')
    # ser.open()
    print("serial port", ser.name, " opened")
except Exception as e:
    print("Was unable to open serial port: " + str(e))
    ser = "n/a"

capture = cv2.VideoCapture(input_video)
frameNr = 0
frame_interval = 1
running = True

while capture.isOpened():
    # process frames
    success, frame = capture.read()
    
    if success:
        if frameNr % frame_interval == 0:
            #cv2.imwrite(r'C:\Users\patri\Desktop\ESPIT\Lane Follow\Lane Follow CV\Databank_Of_Images/frame_{frameNr}.jpg', frame)
            #print("recording frame # ", frameNr)
            center_offset = find_offset(frame)
            print("Center offset : ", center_offset, " On Frame # :", frameNr)

            if(ser != "n/a"):
                try:
                    # Send a value to the Arduino
                    serial_input = str(center_offset)+","
                    ser.write(serial_input.encode())
                    # print("Writing to serial!")
                    # Close the serial port
                except Exception as e:
                    print("error writing serial port: " + str(e))

                


            #if(center_offset > .1 or center_offset < -.1):
                


        else:
            pass
            # print("Not reco / / rding frame # ", frameNr)

    else:
        print("Failed to process image # ", frameNr)
        # ser.close()
        # running = False
        break;

    frameNr = frameNr+1

capture.release()







