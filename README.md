# ⚽ Football Player Detection using YOLOv8 & Streamlit

## 📌 Project Overview
This project uses **YOLOv8** to detect football players, goalkeepers, referees, and balls in images. The model is trained on a dataset of football images and deployed using **Streamlit** to provide a user-friendly interface for uploading images and running inference.

## 🚀 Features
- Detects **players, goalkeepers, referees, and footballs**.
- Uses **YOLOv8** for object detection.
- Streamlit-based **web interface** for easy image uploads.
- Supports **local deployment** and **cloud deployment**.

---

## 📂 Dataset Structure
The dataset is organized as follows:
```
/football
   ├── train
   │   ├── images
   │   ├── labels
   ├── valid
   │   ├── images
   │   ├── labels
   ├── test
   │   ├── images
   │   ├── labels
   ├── data.yaml
   ├── README.dataset
   ├── README.roboflow
```
The **data.yaml** file contains dataset information:
```yaml
train: ../train/images
val: ../valid/images
test: ../test/images

nc: 4
names: ['ball', 'goalkeeper', 'player', 'referee']
```

---

## 🛠 Installation & Setup
### 1️⃣ Install Dependencies
```bash
pip install ultralytics streamlit opencv-python
```

### 2️⃣ Download the Trained Model
Ensure your trained model (`best.pt`) is available in the project directory.

```bash
# If using Google Colab, download it
from google.colab import files
files.download('/content/runs/detect/train/weights/best.pt')
```

---

## 📸 Running the Streamlit App
### **1️⃣ Running the App Locally**
The application code is in the `app.py` file. To run it, use the following command:
```bash
streamlit run app.py
```

---

## 🌐 Deploy on Streamlit Cloud
1. Upload your `app.py` and `best.pt` to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and connect your repo.
3. Deploy your app!

---

## 📊 Model Performance
| Class       | Precision | Recall | mAP50 | mAP50-95 |
|------------|------------|--------|--------|----------|
| All        | 0.893      | 0.582  | 0.64   | 0.399    |
| Ball       | 1.0        | 0.0    | 0.025  | 0.008    |
| Goalkeeper | 0.875      | 0.781  | 0.86   | 0.538    |
| Player     | 0.893      | 0.933  | 0.962  | 0.646    |
| Referee    | 0.805      | 0.614  | 0.712  | 0.404    |

---

## 🎯 Next Steps
- Improve dataset with more diverse images.
- Train a larger model (e.g., YOLOv8m or YOLOv8l) for better accuracy.
- Extend the app to **detect players in videos**.

---

## 📌 Author
Developed by **[Your Name]** as part of a Computer Vision project.

Feel free to contribute and improve this project! 🚀

