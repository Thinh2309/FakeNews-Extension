import torch
from transformers import AutoModel, AutoTokenizer
import numpy as np
import joblib
import os
from flask import Flask, request, jsonify
from flask_cors import CORS  
from scipy.special import expit  # Sigmoid function

# Khởi tạo Flask app
app = Flask(__name__)
CORS(app)

# Định nghĩa đường dẫn tuyệt đối
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

SVM_MODEL_PATH = os.path.join(MODEL_DIR, "svm_model.pkl")
PHOBERT_MODEL_PATH = os.path.join(MODEL_DIR, "phobert_model.pt")
TOKENIZER_PATH = "vinai/phobert-base"  # PhoBERT mặc định

# Load PhoBERT tokenizer và model
print("Đang load tokenizer và mô hình PhoBERT...")

try:
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
    phobert = AutoModel.from_pretrained(TOKENIZER_PATH)
    print("PhoBERT loaded successfully!")
except Exception as e:
    print(f"Lỗi khi load PhoBERT: {e}")
    exit(1)

# Load mô hình SVM
print("Đang load mô hình SVM...")
try:
    svm_model = joblib.load(SVM_MODEL_PATH) 
    print("SVM model loaded successfully!")
except Exception as e:
    print(f"Lỗi khi load mô hình SVM: {e}")
    exit(1)

# Hàm trích xuất đặc trưng từ PhoBERT
def extract_features(text, max_length=256):
    """Trích xuất vector đặc trưng từ PhoBERT."""
    inputs = tokenizer(
        text,
        padding="max_length",
        truncation=True,
        max_length=max_length,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = phobert(**inputs)

    embedding = torch.mean(outputs.last_hidden_state, dim=1).squeeze().numpy()
    return embedding.reshape(1, -1)  # Định dạng phù hợp cho SVM

# Hàm dự đoán tin giả

def predict_fake_news(text):
    """Dự đoán văn bản có phải tin giả hay không và tính độ tin cậy."""
    features = extract_features(text).reshape(1, -1)  # Vector hóa dữ liệu đầu vào

    prob = svm_model.predict_proba(features)[0]  # Xác suất của từng lớp
    confidence_percent = round(max(prob) * 100, 2)  # Lấy xác suất cao nhất

    prediction = "Tin giả" if svm_model.predict(features)[0] == 1 else "Tin thật"

    return {
        "label": prediction,
        "confidence": confidence_percent
    }

#  API Flask cho Chrome Extension
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Thiếu dữ liệu văn bản"}), 400

    result = predict_fake_news(text)
    return jsonify(result)

#  Chạy Flask server
if __name__ == "__main__":
    app.run(debug=True, port=5001)
