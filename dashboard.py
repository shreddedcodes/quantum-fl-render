from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess
import os

app = FastAPI()

processes = []

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Quantum Federated Learning</title>
            <style>
                body { font-family: Arial; text-align: center; margin-top: 100px; }
                button { padding: 15px; font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>Quantum Federated Learning Dashboard</h1>
            <form action="/start">
                <button type="submit">Start Federated Training</button>
            </form>
        </body>
    </html>
    """

@app.get("/start")
def start_training():
    global processes

    if processes:
        return {"status": "Already running"}

    server = subprocess.Popen(["python", "server.py"])
    client1 = subprocess.Popen(["python", "client_1.py"])
    client2 = subprocess.Popen(["python", "client_2.py"])

    processes = [server, client1, client2]

    return {"status": "Federated Training Started"}
