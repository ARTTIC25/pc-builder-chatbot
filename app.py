from recommendations import recommend
from componet_detecter import detecter
from intent import purpose
from compatibiltiy_test import compact
from flask import Flask,render_template,request
import json
import re

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods=["POST"])
def chat():
    message= request.form["message"]
    numbers = re.findall(r"\d+", message)

    if not numbers:
        return "Please provide a budget."

    budget = int(numbers[0])

    user_purpose = purpose(message)

    preferred_gpu = detecter(message)

    build = recommend(
        budget,
        user_purpose,
        preferred_gpu
    )

    total_price = (
        build["cpu"]["price"] +
        build["gpus"]["price"] +
        build["ram"]["price"] +
        build["motherboard"]["price"]
    )

    compatible = compact(
        build["cpu"],
        build["motherboard"],
        build["ram"]
    )

    reply = f"""
CPU: {build['cpu']['name']}

GPU: {build['gpus']['name']}

RAM: {build['ram']['name']}

Motherboard: {build['motherboard']['name']}

Total Price: ₹{total_price}

Compatibility: {"Compatible " if compatible else "Not Compatible "}
"""

    return reply
if __name__=="__main__":
    app.run(debug=True)

