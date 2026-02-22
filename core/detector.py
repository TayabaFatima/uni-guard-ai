
   def analyze_link(url):
    suspicious_keywords = [
        "login", "verify", "bank", "secure",
        "account", "update", "password", "phishing"
    ]

    for word in suspicious_keywords:
        if word in url.lower():
            return "BLOCKED"

    if url.startswith("http://"):
        return "WARNING"

    return "SAFE"
