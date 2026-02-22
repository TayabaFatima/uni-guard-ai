# core/predictive.py
def predict_threat(url):
    """
    Simple predictive threat scoring
    """
    patterns = ["login", "bank", "secure", "update", "account"]
    score = sum(1 for p in patterns if p in url.lower())
    if score >= 3:
        return "HIGH RISK 🔥"
    elif score == 2:
        return "MEDIUM RISK ⚠️"
    else:
        return "LOW RISK ✅"
