from flask import Flask, request, jsonify, render_template,url_for
import os
import requests
import json
from wit import Wit
import json

access_token = "DXRQXBGEAYGVY5PKLUELZW4BFQWWPWXW"

app = Flask(__name__)

with open("everything.txt",'r') as f:
    everything_text = f.read()

with open("computer.txt",'r') as f:
    computer_text = f.read()

with open("c_quiz.txt",'r') as f:
    c_quiz = f.read()

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
    everything = first_entity_value(entities,'fest_question')
    computer = first_entity_value(entities,'computer')

    if creator:
        return ("Created by Sneh Mehta and Beautify by Nimit Patel",'text')
    elif greeting:
        return ("Hi, how can I help you",'text')
    elif everything:
        return (everything_text,'text')
    elif computer:
        if computer == 'general':
            return (computer_text,'text')
        else:
            return ('c_quiz','iframe')

    else:
        return ("I am under Construction",'text')


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
        # print(answer,type(answer))
        # print(answer[0])
        reply = {
            "message": answer[0],
            "display" : answer[1]
        }

        return jsonify(reply)

@app.route('/c_quiz')
def c_quiz():
    return render_template('c_quiz.html') 

# run Flask app
if __name__ == "__main__":
    app.run(debug=True)