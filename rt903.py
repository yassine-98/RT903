from ast import While
from asyncio.constants import DEBUG_STACK_DEPTH
from email.mime import image
from tkinter import image_names
from flask import Flask
from flask import jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello() :
     return jsonify({"Message":os.environ.get('message')})

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get('Port'))
