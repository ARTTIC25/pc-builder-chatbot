from recommendations import recommend
from componet_detecter import detecter
from intent import purpose
from compatibiltiy_test import compact
from flask import Flask, render_template, request, jsonify
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
<b>CPU:</b> {build["cpu"]["name"]} - ₹{build["cpu"]["price"]}<br>

<b>GPU:</b> {build["gpus"]["name"]} - ₹{build["gpus"]["price"]}<br>

<b>RAM:</b> {build["ram"]["name"]} - ₹{build["ram"]["price"]}<br>

<b>Motherboard:</b> {build["motherboard"]["name"]} - ₹{build["motherboard"]["price"]}<br><br>

<b>Total Price:</b> ₹{total_price}<br><br>

<b>Compatibility:</b> {"✅ Compatible" if compatible else "❌ Not Compatible"}
"""

    return jsonify({

    "cpu": build["cpu"]["name"],
    "gpus": build["gpus"]["name"],
    "ram": build["ram"]["name"],
    "motherboard": build["motherboard"]["name"],
    "total": total_price,
    "compatible": compatible

})
    
if __name__=="__main__":
    app.run(debug=True)

