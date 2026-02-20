from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from core.detector import analyze_link
from core.auto_block import take_action

app = Flask(__name__)
CORS(app)

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.get_json()
    link = data.get("link")
    
    result = analyze_link(link)
    status = take_action(result, link)

    try:
        with open("database.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append({"device": data.get("device"), "link": link, "status": status})
    with open("database.json", "w") as f:
        json.dump(logs, f, indent=4)

    return jsonify({"result": result, "status": status})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
