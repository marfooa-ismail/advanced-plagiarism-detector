import pandas as pd
import numpy as np
import re, string
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# ---------- LOAD DATA ----------
df = pd.read_csv("data/Dataset.txt", sep="\t", header=None)
df.columns = ["source_text", "plagiarized_text", "label"]

# ---------- CLEAN FUNCTION ----------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\n", " ", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


df.drop_duplicates(inplace=True)
df.fillna("", inplace=True) #missing values handle

df["source_text"] = df["source_text"].astype(str).apply(clean_text)
df["plagiarized_text"] = df["plagiarized_text"].astype(str).apply(clean_text)

# # ---------- TRANSFORMER ----------
model = SentenceTransformer("all-MiniLM-L6-v2")

e1 = model.encode(df["source_text"].tolist(), show_progress_bar=True)
e2 = model.encode(df["plagiarized_text"].tolist(), show_progress_bar=True)

#feature engineering 
X = np.concatenate([e1, e2, np.abs(e1 - e2), e1 * e2], axis=1)
y = df["label"].values

# # ---------- TRAIN ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

clf = LogisticRegression(max_iter=1000, class_weight="balanced")
clf.fit(X_train, y_train)

# # ---------- SAVE ----------
import os
os.makedirs("model", exist_ok=True)

joblib.dump(clf, "model/classifier.pkl")
model.save("model/transformer")

print("✅ Model training complete & saved")

from sklearn.metrics import accuracy_score, classification_report

y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.metrics import confusion_matrix, roc_auc_score

print("ROC AUC:", roc_auc_score(y_test, clf.predict_proba(X_test)[:,1]))
print(confusion_matrix(y_test, y_pred))

# Batches: 100%|████████████████████████████████████| 11467/11467 [40:42<00:00,  4.69it/s]
# Batches: 100%|████████████████████████████████████| 11467/11467 [23:18<00:00,  8.20it/s]
# ✅ Model training complete & saved
# Accuracy: 0.895726588902213
#               precision    recall  f1-score   support

#            0       0.91      0.88      0.89     36775
#            1       0.88      0.91      0.90     36609

#     accuracy                           0.90     73384
#    macro avg       0.90      0.90      0.90     73384
# weighted avg       0.90      0.90      0.90     73384
