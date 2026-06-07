import joblib
from sentence_transformers import SentenceTransformer
import numpy as np
import string
import re
import os
# Load model & transformer


import joblib

# ROOT me file hone ki wajah se
clf = joblib.load("plagiarism_clf.pkl")



print("Model loaded successfully")
model = SentenceTransformer('all-MiniLM-L6-v2')



def clean_text(text):
    # 1. Lowercase karna
    text = text.lower()
    
    # 2. URLs aur Links ko remove karna (http, https, www)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # 3. New lines aur extra spaces khatam karna
    text = re.sub(r"\n", " ", text)
    
    # 4. Emojis aur non-ASCII characters ko remove karna
    text = text.encode('ascii', 'ignore').decode('ascii')
    
    # 5. Punctuation (!, @, #, etc.) hatana
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # 6. Extra white spaces ko single space mein badalna
    text = re.sub(r'\s+', ' ', text).strip() 
    #strip removes starting and ending spaces
    
    return text


def check_plagiarism(text1, text2):
    # 1. Text Cleaning
    t1 = clean_text(text1)
    t2 = clean_text(text2)

    # 2. Embedding Generation
    e1 = model.encode([t1])
    e2 = model.encode([t2])

    # 3. Feature Engineering (Difference and Product)
    features = np.concatenate([
        e1, 
        e2, 
        np.abs(e1 - e2), 
        e1 * e2
    ], axis=1)

    # 4. Prediction and Percentage Calculation
    pred = clf.predict(features)[0]
    
    # predict_proba returns [prob_0, prob_1]
    # prob_1 is the probability of being plagiarized
    prob_score = clf.predict_proba(features)[0][1] 
    similarity_percentage = round(prob_score * 100, 2)

    status = "Plagiarized" if pred == 1 else "Original"
    
    return {
        "status": status,
        "similarity_score": f"{similarity_percentage}%",
        "label": int(pred)
    }

print(clean_text("""Check this! 🌟 https://ai.com. It's GREAT!!\n
                Artificial Intelligence is 🚀..."""))

if __name__ == "__main__":
    result = check_plagiarism(
        "Artificial intelligence helps machines learn from data.",
        "Artificial intelligence helps to learn patterns from information."
        # "Check this! 🌟 https://ai.com. It's GREAT!! \n",
        # "Artificial Intelligence is 🚀..."
    )
    print(result)
 

