# Wildlife Animal Intrusion Detection System 🐾

A real-time security solution designed to detect and alert users of wildlife intrusions (specifically monkeys and pigs) using **YOLOv8** computer vision and **Twilio** SMS integration.

## 📌 Project Overview
This system operates on a Server-Client architecture. It remains in a low-power "listening" mode until a motion sensor (via network socket) triggers the camera. Once triggered, the system performs high-accuracy object detection and sends an instant mobile alert if a target animal is confirmed.

## 📂 Directory Structure
The repository is organized as follows:
* **`Dataset/`**: Contains the training and validation images and labels.
* **`best.pt`**: The custom-trained YOLOv8 model weights for animal detection.
* **`final.py`**: The main production script handling the socket server and detection logic.
* **`main.ipynb`**: A Jupyter Notebook used for environment setup and initial testing.
* **`custom_data.yaml`**: Configuration file for the YOLO dataset classes and paths.

## 🛠️ Features
* **Socket Triggering**: The system waits for a `"Motion Detected!"` message over TCP/IP before activating the camera.
* **Smart Validation**: Requires **5 consecutive frames** of a 'monkey' or 'pig' to trigger an alert, drastically reducing false positives from shadows or wind.
* **Automated Alerts**: Sends SMS notifications via Twilio including the name of the detected animal.
* **Efficient Processing**: The camera automatically releases after 10 seconds of scanning if no further motion is detected.

## 🚀 Setup & Installation

### 1. Requirements
Ensure you have Python installed, then run:
```bash
pip install ultralytics opencv-python twilio
