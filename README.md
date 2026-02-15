# Medilens: Pill Identification System
**Project for PBL-2 | CSE Section F | Manipal University Jaipur**

## 📊 Performance
The model achieves high precision as shown in the Confusion Matrix. Real-world testing shows a confidence level of **98.78%** on unseen images.

- **Top-1 Accuracy:** 98.7%
- **Inference Speed:** ~228ms per image

## 🛠️ Technical Specifications
- **Model Architecture:** YOLOv8n-cls (Classification)
- **Dataset:** 15 Classes of Indian Pills (Dolo 650, Nimulid MD, etc.)
- **Training Duration:** 50 Epochs (Stabilized at 98.7%)
- **Input Resolution:** 224x224 pixels

## ⚙️ Data Augmentation & Robustness
To ensure reliability across various pharmacy lighting conditions and mobile camera qualities, the following hyperparameters were implemented in `training_model.py`:

* **Rotation:** ±15.0° (Handles various hand angles during photography).
* **HSV Value (Brightness):** `0.4` (Accounts for low-light environments).
* **HSV Saturation:** `0.3` (Standardizes colors across different camera sensors).

 
