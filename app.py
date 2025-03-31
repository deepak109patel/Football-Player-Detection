import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("best.pt")  # Ensure best.pt is in the same directory

# Streamlit UI
st.title("⚽ Football Player Detection with YOLOv8")
st.write("Upload an image, and the model will detect players!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert file to OpenCV format
    image = Image.open(uploaded_file)
    img_cv2 = np.array(image)
    img_cv2 = cv2.cvtColor(img_cv2, cv2.COLOR_RGB2BGR)

    # Run YOLO inference
    results = model(img_cv2)

    # Draw bounding boxes
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get box coordinates
            conf = box.conf[0]  # Confidence score
            label = model.names[int(box.cls[0])]  # Get class label

            # Draw rectangle and label
            cv2.rectangle(img_cv2, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(img_cv2, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Convert back to PIL image
    result_img = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
    st.image(result_img, caption="Detected Players", use_column_width=True)