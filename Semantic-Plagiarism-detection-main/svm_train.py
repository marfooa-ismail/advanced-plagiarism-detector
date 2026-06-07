import pandas as pd
import numpy as np
import re, string
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load data
df = pd.read_csv("data/Dataset.txt", sep="\t", header=None)
df.columns = ["source_text", "plagiarized_text", "label"]

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\n", " ", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Preprocess
df.drop_duplicates(inplace=True)
df.fillna("", inplace=True)
df["source_text"] = df["source_text"].astype(str).apply(clean_text)
df["plagiarized_text"] = df["plagiarized_text"].astype(str).apply(clean_text)

# Encode with transformer
model = SentenceTransformer("all-MiniLM-L6-v2")
emb_source = model.encode(df["source_text"].tolist(), show_progress_bar=True)
emb_plag = model.encode(df["plagiarized_text"].tolist(), show_progress_bar=True)

# Feature engineering: concatenate and element‑wise operations
X = np.concatenate([emb_source, emb_plag, np.abs(emb_source - emb_plag), emb_source * emb_plag], axis=1)
y = df["label"].values

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Train SVM
svm_clf = SVC(kernel='linear', probability=True, class_weight='balanced')
svm_clf.fit(X_train, y_train)

# Save model and transformer
import os
os.makedirs("model", exist_ok=True)
joblib.dump(svm_clf, "model/svm_classifier.pkl")
model.save("model/transformer_svm")  # reuse transformer save method

print("✅ SVM training complete & model saved to model/svm_classifier.pkl")
