import os
import sys
import joblib
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.feature_extraction import extract_features

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "phishing_model.joblib"
)

if len(sys.argv) != 2:
    print('Usage: python src/predict.py "https://example.com"')
    sys.exit(1)

url = sys.argv[1]

if not os.path.exists(MODEL_PATH):
    print("Model not found. Run: python src/train_model.py")
    sys.exit(1)

model = joblib.load(MODEL_PATH)

features = pd.DataFrame([extract_features(url)])
prediction = model.predict(features)[0]

if prediction == 1:
    result = "Potentially Phishing"
else:
    result = "Legitimate"

print(f"URL: {url}")
print(f"Prediction: {result}")
