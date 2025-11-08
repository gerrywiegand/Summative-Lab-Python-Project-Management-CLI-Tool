import json


def save_data(data, filename="data/data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_data(filename="data/data.json"):
    with open(filename) as f:
        data = json.load(f)
    return data
