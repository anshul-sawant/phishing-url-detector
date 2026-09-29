# Phishing URL Detector

An educational AI/ML-based project that analyzes URL characteristics and classifies URLs as potentially **phishing** or **legitimate**.

## Project Objective

The goal is to demonstrate how URL-based features can be used with a machine-learning classifier to identify suspicious URLs.

> This project is for educational and defensive cybersecurity purposes. It is not a replacement for a production phishing-detection service.

## Features Used

The model extracts simple characteristics from a URL:

- URL length
- Number of dots
- Number of hyphens
- Number of digits
- Number of special characters
- Whether the URL uses HTTPS
- Whether an IP address is used instead of a domain
- Presence of suspicious words such as `login`, `verify`, `secure`, and `account`

## Technology

- Python
- pandas
- scikit-learn
- joblib
- Regular expressions

## Project Structure

```text
phishing-url-detector/
├── README.md
├── requirements.txt
├── data/
│   └── sample_urls.csv
├── models/
├── src/
│   ├── feature_extraction.py
│   ├── train_model.py
│   └── predict.py
└── screenshots/
```

## Installation

```bash
git clone https://github.com/anshul-sawant/phishing-url-detector.git
cd phishing-url-detector
python -m venv venv
```

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
python src/train_model.py
```

The trained model is saved inside the `models/` folder.

## Test a URL

```bash
python src/predict.py "https://example.com"
```

Example:

```text
Prediction: Legitimate
```

Try an educationally suspicious example:

```bash
python src/predict.py "http://secure-login-example.com/verify/account"
```

## Important Note

The included dataset is a small demonstration dataset created for this portfolio project. A real-world system should be trained and tested using a large, diverse, validated dataset and should use proper train/test separation and security evaluation.

## Future Improvements

- Use a larger real-world dataset
- Add more URL and domain features
- Compare multiple ML algorithms
- Add precision, recall, F1-score and confusion matrix
- Build a web interface
- Add model explainability
- Evaluate the model on unseen datasets

## Author

**Anshul Sawant**

B.Sc. Cyber & Digital Science | Cybersecurity
