from flask import Flask, render_template, request
from core.detector import analyze_link
from core.auto_block import take_action
from core.predictive import predict_threat
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    status = None
    risk_score = None
    link = None

    if request.method == "POST":
        link = request.form.get("link")
        result = analyze_link(link)
        status = take_action(result, link)
        risk_score = predict_threat(link)

        # Save log
        try:
            with open("../database.json", "r") as file:
                logs = json.load(file)
        except:
            logs = []

        logs.append({"link": link, "status": status, "risk": risk_score})
        with open("../database.json", "w") as file:
            json.dump(logs, file, indent=4)

    return render_template("index.html", status=status, link=link, risk=risk_score)

if __name__ == "__main__":
    app.run(debug=True)
