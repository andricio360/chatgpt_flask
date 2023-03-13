import os

import openai
from flask import Flask, redirect, render_template, request, url_for,jsonify
import requests


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

"""
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)
"""
@app.route('/')
def hello_world():
    return 'Hello, World!'
# Your ChatGPT code goes here
def generate_response(message):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message,
            temperature=0.6,
        )
    try:
        return response.choices[0].text
    except:
        return "Error generating response"

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = generate_response(message)
    print(response)
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
