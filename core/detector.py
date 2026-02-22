
 # core/detector.py

def analyze_link(url):
    """
    Detect if the link is safe, warning, or phishing
    """

    suspicious_keywords = [
        "login", "verify", "bank", "secure",
        "account", "update", "password", "phishing",
        "signin", "confirm", "credit", "debit"
    ]

    # Check for suspicious words
    for word in suspicious_keywords:
        if word in url.lower():
            return "BLOCKED ⚠️ Phishing Detected"

    # Check if HTTP (not secure)
    if url.startswith("http://"):
        return "WARNING ⚠️ Not Secure (HTTP)"

    # Default safe
    return "SAFE ✅"
