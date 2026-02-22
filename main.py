from core.detector import analyze_link
from core.auto_block import take_action
from core.predictive import predict_threat
import json

def save_log(link, status, risk):
    """
    Save scanned link, status, and risk score into database.json
    """
    try:
        with open("database.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append({"link": link, "status": status, "risk": risk})

    with open("database.json", "w") as f:
        json.dump(logs, f, indent=4)

# ========================
# CLI Run System
# ========================
link = input("Enter a link: ")

# 1️⃣ Analyze link
status = analyze_link(link)

# 2️⃣ Take action (BLOCK / WARNING / SAFE)
take_action(status, link)

# 3️⃣ Predict threat score
risk = predict_threat(link)

# 4️⃣ Save to database.json
save_log(link, status, risk)

# 5️⃣ Print threat score
print(f"Threat Score: {risk}")
