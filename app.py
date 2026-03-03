import os
from flask import Flask,send_from_directory 
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
FRONT_DIR = os.path.join(BASE_DIR, "front-end")
STATIC_DIR = os.path.join(BASE_DIR,"static")
app = Flask(__name__,static_folder=STATIC_DIR,static_url_path="/"+STATIC_DIR)
@app.route('/')
def home ():
    return "hello word!"
app.run(debug=True)