
import socket
import cv2
from ultralytics import YOLO
from twilio.rest import Client

# Initialize YOLO model
model = YOLO(model="C:/Users/swapn/Downloads/best (2).pt")
names = model.names

# Twilio API credentials
account_sid = 'twilio account sid'
auth_token = 'twilio auth token'
client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms(detected_class):
    message = client.messages.create(
        from_='twilio account number',
        body=f'{detected_class.title()} Detected',
        to='your number'
    )
    print("SMS sent:", message.sid)

# The server's hostname or IP address
HOST = 'server host ip address'
# The port used by the server
PORT = 12345

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port number
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print("Server is listening for incoming connections...")
    # Accept a connection
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Receive the data sent by the client
            data = conn.recv(1024)
            if not data:
                break
            # Print the message received from the client
            message = data.decode()
            print(f"Received message: {message}")
            if message == "Motion Detected!":
                # Perform object detection on the frame
                video_capture = cv2.VideoCapture(0)
                start_time = cv2.getTickCount()
                consecutive_detections = 0
                while True:
                    ret, frame = video_capture.read()
                    if not ret:
                        break

                    # Perform object detection on the frame
                    results = model.predict(frame, imgsz=512, conf=0.6)
                    for r in results:
                        for c in r.boxes.cls:
                            detected_class = names[int(c)]
                            print("Detected:", detected_class)
                            if detected_class in ['monkey', 'pig']:
                                consecutive_detections += 1
                                if consecutive_detections >= 5:
                                    print('sms sent')
                                    # send_sms(detected_class)
                                    consecutive_detections = 0
                            else:
                                consecutive_detections = 0

                    # Check if 10 seconds have elapsed or the motion is no longer detected
                    current_time = cv2.getTickCount()
                    elapsed_time = (current_time - start_time) / cv2.getTickFrequency()
                    if elapsed_time >= 10:
                        break

                # Release video capture and close windows
                video_capture.release()
import socket
import cv2
from ultralytics import YOLO
from twilio.rest import Client

# Initialize YOLO model
model = YOLO(model="C:/Users/swapn/Downloads/best (2).pt")
names = model.names

# Twilio API credentials
account_sid = 'twilio account sid'
auth_token = 'twilio auth token'
client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms(detected_class):
    message = client.messages.create(
        from_='twilio account number',
        body=f'{detected_class.title()} Detected',
        to='your number'
    )
    print("SMS sent:", message.sid)

# The server's hostname or IP address
HOST = 'server host ip address'
# The port used by the server
PORT = 12345

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port number
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print("Server is listening for incoming connections...")
    # Accept a connection
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Receive the data sent by the client
            data = conn.recv(1024)
            if not data:
                break
            # Print the message received from the client
            message = data.decode()
            print(f"Received message: {message}")
            if message == "Motion Detected!":
                # Perform object detection on the frame
                video_capture = cv2.VideoCapture(0)
                start_time = cv2.getTickCount()
                consecutive_detections = 0
                while True:
                    ret, frame = video_capture.read()
                    if not ret:
                        break

                    # Perform object detection on the frame
                    results = model.predict(frame, imgsz=512, conf=0.6)
                    for r in results:
                        for c in r.boxes.cls:
                            detected_class = names[int(c)]
                            print("Detected:", detected_class)
                            if detected_class in ['monkey', 'pig']:
                                consecutive_detections += 1
                                if consecutive_detections >= 5:
                                    print('sms sent')
                                    # send_sms(detected_class)
                                    consecutive_detections = 0
                            else:
                                consecutive_detections = 0

                    # Check if 10 seconds have elapsed or the motion is no longer detected
                    current_time = cv2.getTickCount()
                    elapsed_time = (current_time - start_time) / cv2.getTickFrequency()
                    if elapsed_time >= 10:
                        break

                # Release video capture and close windows
                video_capture.release()
                cv2.destroyAllWindows()