# core/predictive.py

from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Dummy training data
X = np.array([
    [1, 1],  # phishing
    [0, 1],  # suspicious
    [0, 0],  # safe
    [1, 0]   # malware
])

y = [2, 1, 0, 2]  # 0=safe, 1=warning, 2=danger

model = RandomForestClassifier()
model.fit(X, y)

def predict_threat(link):
    score1 = int("http" in link)
    score2 = int(any(word in link for word in ["login","bank","verify"]))

    prediction = model.predict([[score1, score2]])[0]

    if prediction == 2:
        return "HIGH RISK 🚨"
    elif prediction == 1:
        return "MEDIUM RISK ⚠️"
    else:
        return "LOW RISK ✅"
