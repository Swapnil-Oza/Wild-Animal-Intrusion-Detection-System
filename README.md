# 🐒 Wildlife Intrusion Detection System

A real-time wildlife intrusion detection system that uses **YOLOv8** object detection to identify animals (monkeys and pigs) from live camera feeds and instantly alerts farmers or property owners via **SMS** using the Twilio API. The system integrates a **motion sensor trigger** over a TCP socket connection, activating the camera and detection pipeline only when motion is detected — making it efficient and power-friendly.

---

## 📌 Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model](#model)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

---

## 🧠 Overview

Wildlife intrusion into farmland causes significant crop damage. This system provides an automated, low-cost solution by:

1. **Listening** for a motion detection signal from a connected sensor/client over a local TCP network
2. **Activating** a live camera feed upon motion detection
3. **Running YOLOv8** inference on each frame to detect monkeys or pigs
4. **Sending an SMS alert** via Twilio if the animal is detected in 5 or more consecutive frames (to avoid false positives)

---

## ⚙️ How It Works

```
Motion Sensor (client device)
        │
        │  TCP Socket ("Motion Detected!")
        ▼
Server (final.py / main.ipynb)
        │
        ▼
OpenCV — Live Camera Feed (Webcam / IP Camera)
        │
        ▼
YOLOv8 Inference (best.pt — custom trained)
        │
        ├── Monkey or Pig detected for 5+ consecutive frames?
        │         │
        │         ▼
        │   Twilio SMS Alert sent to farmer
        │
        └── No animal / other object → continue monitoring
```

- Detection runs for **10 seconds** per motion trigger
- **Confidence threshold:** 0.6 (filters out weak/uncertain detections)
- **Image size for inference:** 512×512

---

## 📁 Project Structure

```
Wildlife-Intrusion-Detection/
│
├── Dataset/
│   ├── images/
│   │   ├── train/               # Training images
│   │   └── val/                 # Validation images
│   ├── labels/
│   │   ├── train/               # YOLO-format labels for training
│   │   └── val/                 # YOLO-format labels for validation
│   ├── train.cache              # Cached training data
│   ├── val.cache                # Cached validation data
│   └── custom_data.yaml         # Dataset config (inside Dataset/)
│
├── custom_data.yaml             # Dataset config (root — used for training)
├── best.pt                      # Trained YOLOv8 model weights
├── final.py                     # Main server script (production)
├── main.ipynb                   # Development notebook (prototyping)
├── toy.png                      # Sample test image
└── README.md
```

---

## 📊 Dataset

- **Classes:** 2 — `monkey`, `pig`
- **Format:** YOLO annotation format (bounding boxes in `.txt` files)
- **Split:** `train/` and `val/` directories for images and labels
- **Config:** `custom_data.yaml` defines class names, paths, and number of classes

The dataset contains diverse real-world images of monkeys and pigs in outdoor/farmland environments, labeled with bounding boxes for both classes.

---

## 🤖 Model

- **Architecture:** [YOLOv8](https://github.com/ultralytics/ultralytics) (Ultralytics)
- **Weights:** `best.pt` — custom-trained on the monkey/pig dataset
- **Inference confidence threshold:** 0.6
- **Input image size:** 512×512
- **Runtime:** CPU (Intel Core i5-10300H tested); GPU supported

The model was trained using the Ultralytics YOLOv8 framework on a custom labeled dataset of wildlife images, achieving reliable detection of monkeys and pigs in varied outdoor conditions.

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Wildlife-Intrusion-Detection.git
   cd Wildlife-Intrusion-Detection
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install ultralytics opencv-python twilio
   ```

---

## 🔧 Configuration

Before running, update the following placeholders in `final.py` (or `main.ipynb`):

### Twilio SMS Credentials
```python
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token  = 'YOUR_TWILIO_AUTH_TOKEN'

# In send_sms():
from_= 'YOUR_TWILIO_PHONE_NUMBER'   # e.g. '+1XXXXXXXXXX'
to=    'RECIPIENT_PHONE_NUMBER'      # e.g. '+91XXXXXXXXXX'
```

### Network (TCP Socket)
```python
HOST = 'YOUR_SERVER_IP_ADDRESS'     # IP of the machine running final.py
PORT = 12345                        # Must match the client/sensor device port
```

### Model Path
```python
model = YOLO(model="path/to/best.pt")
```

> ⚠️ **Keep your Twilio credentials private.** Use environment variables or a `.env` file in production and add them to `.gitignore`.

---

## 🚀 Usage

### 1. Run the Detection Server

Start the server on the machine connected to the camera:

```bash
python final.py
```

The server will listen on the configured `HOST:PORT` for an incoming TCP connection.

### 2. Trigger from Motion Sensor / Client Device

From the client (motion sensor device), connect to the server and send:

```
Motion Detected!
```

The server will activate the camera, run YOLOv8 inference for 10 seconds, and send an SMS if an animal is confirmed.

### 3. Run Notebook (Development / Testing)

```bash
jupyter notebook main.ipynb
```

Use this to prototype or test detection on a local webcam without the socket trigger.

---

## 🛠️ Technologies

| Category          | Tools / Libraries                          |
|-------------------|--------------------------------------------|
| Language          | Python 3.10+                               |
| Object Detection  | YOLOv8 (`ultralytics`)                     |
| Computer Vision   | OpenCV (`cv2`)                             |
| SMS Alerts        | Twilio REST API (`twilio`)                 |
| Networking        | Python `socket` (TCP/IP)                   |
| Development       | Jupyter Notebook                           |

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Swapnil Oza**
GitHub: [@Swapnil-Oza](https://github.com/Swapnil-Oza)

---

> ⭐ If you found this project helpful, please give it a star on GitHub!
