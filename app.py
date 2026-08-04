from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello from PaaS Lab! Student: Eshika Pratheesh, Roll No:24MIC0061"
