                        #   FACE DETECTION USING OPENCV

import cv2  

# Load the Haar Cascade Classifieer for Face deeection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


# open a cideo stream
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces int the frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors=  5,
        minSize = (30, 30)
    )

    # Draw rectangles around the detected faces
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    # Display resulting frame
    cv2.imshow("Video", frame)

    # Exit the loop if "q" is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close the OpenCV window
video_capture.release()