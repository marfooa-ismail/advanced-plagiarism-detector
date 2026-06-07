# Advanced Plagiarism Detection System

## Overview
This repository implements an advanced plagiarism detection system using transformer-based sentence embeddings combined with classic machine‑learning classifiers. It now includes support for both **Logistic Regression** (original) and an **SVM** model for improved classification flexibility.

## Quick Setup
```bash
# Clone the repo
git clone https://github.com/marfooa-ismail/advanced-plagiarism-detector.git
cd advanced-plagiarism-detector

# Install dependencies
pip install -r requirements.txt
```

## Data Preparation & Feature Engineering
The scripts `train.py` and `svm_train.py` share the same preprocessing pipeline:
1. Load `data/Dataset.txt` (tab‑separated `source_text`, `plagiarized_text`, `label`).
2. Clean text (lower‑casing, remove newlines & punctuation).
3. Encode sentences using **SentenceTransformer** (`all-MiniLM-L6-v2`).
4. Build features by concatenating embeddings of source and plagiarized texts together with their absolute difference and element‑wise product.

## Training Models
### Logistic Regression (existing)
Run:
```bash
python train.py
```
The model is saved as `model/classifier.pkl`.

### Support Vector Machine (new)
Run:
```bash
python svm_train.py
```
The SVM model is saved as `model/svm_classifier.pkl`.

Both scripts will create the `model/` directory if it does not exist.

## Inference
Use `inference.py` to load either classifier and predict plagiarism:
```python
from inference import predict

# Load Logistic Regression model
pred = predict("model/classifier.pkl", source_text, plag_text)

# Load SVM model
pred = predict("model/svm_classifier.pkl", source_text, plag_text)
```

## Evaluation
Both training scripts print accuracy, classification report, ROC‑AUC and the confusion matrix after training.

## License
MIT License – see the LICENSE file.
