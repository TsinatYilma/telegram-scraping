import json, os

STATE_FILE = "scrape_state.json"

def load_last_id(channel):
    if not os.path.exists(STATE_FILE):
        return 0
    with open(STATE_FILE, "r") as f:
        return json.load(f).get(channel, 0)

def save_last_id(channel, last_id):
    data = {}
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
    data[channel] = last_id
    with open(STATE_FILE, "w") as f:
        json.dump(data, f)
