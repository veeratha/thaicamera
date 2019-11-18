from flask import Flask,render_template
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask on AZURE!"


@app.route("/upload")
def upload():
    dt = datetime.now()
    return "หน้าอัพโหลดรูป "+dt.strftime("%Y-%m-%d %H:%M")
