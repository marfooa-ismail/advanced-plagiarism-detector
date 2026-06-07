# Plagiarism Detection API

A production-ready REST API that detects plagiarism between two text inputs using semantic similarity. Built with Sentence Transformers and Logistic Regression, deployed via FastAPI and Docker.

---

## Features

- Semantic text comparison using state-of-the-art sentence embeddings
- Returns a plagiarism verdict (`Plagiarized` / `Original`) with a confidence score
- Clean text preprocessing pipeline (URL removal, emoji stripping, normalization)
- REST API with JSON input/output via FastAPI
- Dockerized and ready for deployment on Hugging Face Spaces

---

## Tech Stack

| Layer | Technology |
|---|---|
| Embedding Model | `all-MiniLM-L6-v2` (Sentence Transformers) |
| Classifier | Logistic Regression (scikit-learn) |
| API Framework | FastAPI + Uvicorn |
| Containerization | Docker |
| Deployment Target | Hugging Face Spaces |

---

## Model Performance

Trained on ~365,000 labeled text pairs.

| Metric | Score |
|---|---|
| Accuracy | **89.6%** |
| Precision (Plagiarized) | 0.88 |
| Recall (Plagiarized) | 0.91 |
| F1-Score | 0.90 |
| ROC AUC | ~0.97 |

---

## Project Structure

```
plagiarism-detection-api/
├── app.py              # FastAPI application & route definitions
├── inference.py        # Prediction logic and text preprocessing
├── train.py            # Model training pipeline
├── model/
│   ├── classifier.pkl  # Trained Logistic Regression model
│   └── transformer/    # SentenceTransformer config files
├── requirements.txt
├── Dockerfile
└── .gitignore
```

---

## Installation

### Prerequisites
- Python 3.9+
- pip

### Setup

```bash
# Clone the repository
git clone https://github.com/Maryam-1017/plagiarism-detection-api.git
cd plagiarism-detection-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

The `all-MiniLM-L6-v2` transformer model is downloaded automatically from Hugging Face on first run.

---

## Running the API

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Visit the interactive docs at: `http://localhost:8000/docs`

---

## API Usage

### Endpoint

```
POST /check
```

### Request

```json
{
  "text1": "Artificial intelligence helps machines learn from data.",
  "text2": "AI enables computers to learn patterns from information."
}
```

### Response

```json
{
  "status": "Plagiarized",
  "similarity_score": "87.43%",
  "label": 1
}
```

| Field | Type | Description |
|---|---|---|
| `status` | string | `"Plagiarized"` or `"Original"` |
| `similarity_score` | string | Confidence as a percentage |
| `label` | int | `1` = Plagiarized, `0` = Original |

### Example with `curl`

```bash
curl -X POST "http://localhost:8000/check" \
     -H "Content-Type: application/json" \
     -d '{"text1": "Climate change is causing global warming.", "text2": "Global warming is a result of climate change."}'
```

---

## Docker

### Build

```bash
docker build -t plagiarism-api .
```

### Run

```bash
docker run -p 7860:7860 plagiarism-api
```

The API will be available at `http://localhost:7860`.

---

## Retraining the Model

To retrain on your own dataset, place a tab-separated file at `data/Dataset.txt` with columns:

```
source_text    plagiarized_text    label
```

where `label` is `1` (plagiarized) or `0` (original). Then run:

```bash
python train.py
```

The trained classifier will be saved to `model/classifier.pkl`.

---

## How It Works

1. **Text Cleaning** — lowercase, remove URLs, strip emojis and punctuation, normalize whitespace
2. **Embedding** — both texts are encoded into 384-dimensional vectors using `all-MiniLM-L6-v2`
3. **Feature Engineering** — concatenate `[e1, e2, |e1−e2|, e1⊙e2]` into a 1536-dimensional feature vector
4. **Classification** — Logistic Regression predicts plagiarism probability from the feature vector

---

## License

MIT License. See [LICENSE](LICENSE) for details.
