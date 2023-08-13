# Hand-Detection-Lib
this library is a university project in BSc. of software engineering field in urmia university.

This project is a Python script that utilizes computer vision techniques and machine learning models to create a hand gesture recognition system. It uses the Mediapipe library and OpenCV to detect and track hand movements from a webcam feed, and based on the detected hand gestures, it performs the following tasks:

1. Initializes a hand tracking module using the `handTrackingModule` class, which encapsulates the functionality of detecting and tracking hand landmarks.

2. Initializes a hand detection model from the Mediapipe library for detecting hand landmarks and gestures.

3. Reads images of emojis from a specified folder and stores them in an overlay list for later use.

4. Captures video frames from the webcam and processes them for hand detection and gesture recognition.

5. Determines the number of fingers raised or extended on the detected hand by comparing the positions of specific landmarks.

6. Displays a text label indicating whether the detected hand is the left or right hand.

7. Maps specific hand gestures (finger configurations) to corresponding emoji images and overlays the emojis on the video feed.

8. Displays the processed video feed with hand landmarks, finger count, and emoji overlays.

9. The program runs in a loop until the user presses the 'q' key, after which the webcam feed window is closed.

In summary, this code demonstrates a real-time hand gesture recognition system using computer vision and machine learning techniques, which can detect hand gestures, count the number of extended fingers, and overlay emojis based on the detected gestures. It provides a fun and interactive way to interact with the computer using hand movements and can have various applications in entertainment, education, and user interface design.

Below are some footage of project functionality :
in image below you can actually see all 4 features in one frame :

![2](https://github.com/Pouyatlp/Hand-Detection-Lib/assets/66587297/f360b690-e35f-4bab-b54b-de751eb8610d)

Displaying finger count :

![f4](https://github.com/Pouyatlp/Hand-Detection-Lib/assets/66587297/06af1164-5cdf-419d-8c34-f3ce581c4ba0)

A sample of emoji detection :

![11](https://github.com/Pouyatlp/Hand-Detection-Lib/assets/66587297/adaacd59-05fc-489d-b8bf-ac4ae217c414)

![9](https://github.com/Pouyatlp/Hand-Detection-Lib/assets/66587297/e8217092-38ac-488f-97c2-10b10e1a101b)



in conclusion this project consists of 4 features listed below :

1.detect the hand(s) in input image (Real-time camera video). wether or not there is a hand shown in the frame.

2.Right,Left or Both hands in the frame Detection.

3.How many fingers are up? (amount of fingers that are being heldup in the frame)

4.which emoji from 9 emojies defined , is being Showed by the hand? (Emoji Detection)

# How it Works
Run the project from main.py and make sure all files are in the same directory including "Emoji Pics" folders.
once the project is running , you can use all the features listed above and after you are done ; you can simply
press "Q" on your keyboard to terminate the video.

this project also has been uploaded to pypi as a package so all users globally can install and use it in their project.

# How to install
open Command Line and enter the command below :

`pip install HDL.v2`


Also you can find the package in links below :

https://test.pypi.org/project/HDL.v2/0.0.1/ 

https://pypi.org/project/HDL.v2/0.0.1/



