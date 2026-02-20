from core.detector import analyze_link
from core.auto_block import take_action
import json

def save_log(link, status):
    data = {
        "link": link,
        "status": status
    }

    try:
        with open("database.json", "r") as file:
            logs = json.load(file)
    except:
        logs = []

    logs.append(data)

    with open("database.json", "w") as file:
        json.dump(logs, file, indent=4)

# Run system
link = input("Enter a link: ")

result = analyze_link(link)
status = take_action(result, link)

save_log(link, status)
