from flask import Flask, request
import json
import os

app = Flask(__name__)
print("Current Folder:", os.getcwd())

USER_FILE = "users.txt"

def save_user(user_id):

    if not os.path.exists(USER_FILE):
        open(USER_FILE, "w").close()

    with open(USER_FILE, "r", encoding="utf-8") as f:
        users = [u.strip() for u in f.readlines()]

    if user_id not in users:

        with open(USER_FILE, "a", encoding="utf-8") as f:
            f.write(user_id + "\n")

        print("New User :", user_id)

    else:
        print(f"Already Exists : {user_id}")


@app.route("/webhook", methods=["POST"])
def webhook():
    print(">>> Webhook called <<<")
    body = request.json

    print(json.dumps(body, indent=4, ensure_ascii=False))

    events = body.get("events", [])

    for event in events:

        source = event.get("source", {})

        user_id = source.get("userId")

        print("User ID =", user_id)

        if user_id:
            save_user(user_id)

    return "OK", 200


if __name__ == "__main__":
    app.run(port=5000)