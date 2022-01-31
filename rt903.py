from ast import While
from asyncio.constants import DEBUG_STACK_DEPTH
from email.mime import image
from tkinter import image_names
from flask import Flask , render_template
import random
import datetime
from flask import jsonify

app = Flask(__name__)

@app.route("/")

def hello() :

    
    return jsonify("MESSAGE="Hello World!"")

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
