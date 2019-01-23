from flask import Flask, request, jsonify, render_template
import os
import requests
import json
from wit import Wit

access_token = "DXRQXBGEAYGVY5PKLUELZW4BFQWWPWXW"

app = Flask(__name__)

def first_entity_value(entities, entity):
    if entity not in entities:
        return None 
    val = entities[entity][0]['value']
    if not val:
        return None
    return val

def handle_message(response):
    entities = response['entities']
    greeting = first_entity_value(entities,'intent')
    creator = first_entity_value(entities,'personality')
    if creator:
        return ("Sneh Mehta")
    elif greeting:
        return ("Hi, how can I help you")
    else:
        return ("Sorry I don't understand can you be more specific")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def get_message():
    message = request.form['message']
    if message:
        client = Wit(access_token)
        resp = client.message(message)
        answer = handle_message(resp)
        reply = {
            "message": answer
        }

        return jsonify(reply)

# run Flask app
if __name__ == "__main__":
    app.run(debug=True)