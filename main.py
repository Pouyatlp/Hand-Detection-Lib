# Importing Libraries
import cv2
import mediapipe as mp
import numpy as np
import time
import os
import handTrackingModule as htm
from PIL import ImageFont, ImageDraw, Image

detector = htm.handDetector(max_num_hands=1, min_detection_confidence=0.7)


# Used to convert protobuf message to a dictionary.
from google.protobuf.json_format import MessageToDict

# Initializing the Model
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2,
)

# Define finger tip landmarks
finger_tip_landmarks = [4, 8, 12, 16, 20]


# Start capturing video from webcam
cap = cv2.VideoCapture(0)


# Initialize drawing utilities
mpDraw = mp.solutions.drawing_utils


folderPath = "Emoji Pics"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overlayList.append(image)


while True:
    # Read video frame by frame
    success, img = cap.read()

    # Flip the image(frame)
    img = cv2.flip(img, 1)

    # Convert BGR image to RGB image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image
    results = hands.process(imgRGB)

    thumb = True
    index = True
    middle = True
    ring = True
    pinky = True

    imp = detector.findHands(img, cv2)
    lmList = detector.findPosition(img, cv2, draw=False)

    # If hands are present in image(frame)
    if results.multi_hand_landmarks:
        # Both Hands are present in image(frame)

        if len(results.multi_handedness) == 2:
            # Display 'Both Hands' on the image

            cv2.putText(
                img,
                "Both Hands",
                (250, 50),
                cv2.FONT_HERSHEY_COMPLEX,
                0.9,
                (0, 255, 0),
                2,
            )

        # If any hand present

        else:
            for i in results.multi_handedness:
                # Return whether it is Right or Left Hand

                label = MessageToDict(i)["classification"][0]["label"]

                if label == "Left":
                    # Display 'Left Hand' on

                    # left side of window

                    cv2.putText(
                        img,
                        label + " Hand",
                        (20, 400),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )

                if label == "Right":
                    # Display 'Left Hand'

                    # on left side of window

                    cv2.putText(
                        img,
                        label + " Hand",
                        (460, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )

        finger_count = 0

        for hand_landmarks in results.multi_hand_landmarks:
            # Count the number of extended fingers
            # finger_count = 0
            for landmark in finger_tip_landmarks:
                finger_tip = hand_landmarks.landmark[landmark]
                if finger_tip.y < hand_landmarks.landmark[landmark - 2].y:
                    finger_count += 1

            # Display the finger count on the image

        cv2.putText(
            img,
            f"Fingers: {finger_count}",
            (20, 350),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

    # No hands found
    else:
        cv2.putText(
            img,
            "No Hand detected",
            (200, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2,
        )

    if len(lmList) != 0:
        ########################################## ---Detecting Fingers--- ###########################################

        if lmList[4][1] < lmList[2][1]:
            thumb = False

        if lmList[8][2] > lmList[6][2]:
            index = False

        if lmList[12][2] > lmList[10][2]:
            middle = False

        if lmList[16][2] > lmList[14][2]:
            ring = False

        if lmList[20][2] > lmList[18][2]:
            pinky = False

        ######################################### ---Conditions For Emoji--- #########################################

        if (
            index == True
            and middle == True
            and thumb == False
            and ring == False
            and pinky == False
        ):
            h, w, c = overlayList[0].shape
            img[0:h, 0:w] = overlayList[0]

        elif (
            index == True
            and pinky == True
            and middle == False
            and ring == False
            and thumb == False
        ):
            h, w, c = overlayList[1].shape
            img[0:h, 0:w] = overlayList[1]

        elif (
            index == True
            and thumb == False
            and middle == False
            and ring == False
            and pinky == False
        ):
            h, w, c = overlayList[2].shape
            img[0:h, 0:w] = overlayList[2]

        elif (
            index == True
            and thumb == True
            and middle == False
            and ring == False
            and pinky == False
        ):
            h, w, c = overlayList[3].shape
            img[0:h, 0:w] = overlayList[3]

        elif (
            middle == True
            and thumb == False
            and index == False
            and ring == False
            and pinky == False
        ):
            h, w, c = overlayList[4].shape
            img[0:h, 0:w] = overlayList[4]

        elif (
            thumb == True
            and index == False
            and middle == False
            and ring == False
            and pinky == False
        ):
            h, w, c = overlayList[5].shape
            img[0:h, 0:w] = overlayList[5]

        elif (
            thumb == True
            and index == True
            and middle == True
            and ring == True
            and pinky == True
        ):
            h, w, c = overlayList[6].shape
            img[0:h, 0:w] = overlayList[6]

        elif (
            thumb == False
            and index == False
            and middle == False
            and ring == False
            and pinky == False
        ):
            h, w, c = overlayList[7].shape
            img[0:h, 0:w] = overlayList[7]

        elif (
            thumb == True
            and index == False
            and middle == False
            and ring == False
            and pinky == True
        ):
            h, w, c = overlayList[8].shape
            img[0:h, 0:w] = overlayList[8]

    # Display Video and when 'q' is entered, destroy the window
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
