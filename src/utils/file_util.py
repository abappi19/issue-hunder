import json


def load_file(path):
    with open(path) as f:
        return json.load(f)


def write_file(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
