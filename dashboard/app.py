@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    threat = None
    logs = load_logs()

    if request.method == "POST":
        link = request.form.get("link")

        result_type = analyze_link(link)
        result = take_action(result_type, link)
        threat = predict_threat(link)

        save_log(link, result)
        logs = load_logs()

    return render_template("index.html", result=result, threat=threat, logs=logs)
    def load_logs()
    try:
        with open("database.json", "r") as f:
            return json.load(f)
    except:
        return []
