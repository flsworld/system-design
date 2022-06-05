import json

from flask import Flask, request

app = Flask(__name__)

DATA_DIR = "data"
hashtable = {}


@app.route("/memory/<key>", methods=("GET", "POST"))
def memory_rw(key):
    if request.method == "GET":
        if key in hashtable:
            return hashtable[key], 200
        return "null", 400
    else:
        hashtable[key] = request.json
        return "", 204


@app.route("/disk/<key>", methods=("GET", "POST"))
def disk_rw(key):
    if request.method == "GET":
        try:
            destfile = f"{DATA_DIR}/{key}"
            with open(destfile, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "File not found", 404
    else:
        try:
            destfile = f"{DATA_DIR}/{key}"
        except FileNotFoundError:
            return "`data` directory not found", 500
        with open(destfile, "a") as file:
            file.write(json.dumps(request.json))
        return "", 204
