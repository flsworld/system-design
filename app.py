from flask import Flask, request


app = Flask(__name__)


@app.get("/hello")
def hello():
    print(request.headers)
    print(request.method)
    return "Received GET request!"


@app.post("/hello")
def hello_world():
    print(request.headers)
    print(request.method)
    print(request.json)
    return "Received POST request!"
