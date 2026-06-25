from recommendations import recommend
from componet_detecter import detecter
from intent import purpose
from compatibiltiy_test import compact
from flask import Flask,render_template
import json
import re

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)

