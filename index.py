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

with open("chemical_text.txt",'r') as f:
    chemical_text = f.read()

with open("mech_text.txt",'r') as f:
    mech_text = f.read()

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
    mechanical = first_entity_value(entities,'mechanical')
    civil = first_entity_value(entities,'civil')
    chemical = first_entity_value(entities,'chemical')

    if creator:
        return ("BrainChild of Sneh Mehta and Beautify by Nimit Patel",'text')
    elif greeting:
        return (everything_text,'text')
    elif everything:
        return (everything_text,'text')
    elif computer:
        if computer == 'general':
            return (computer_text,'text')
        elif computer == 'c quiz':
            return ('c_quiz','iframe')
        elif computer == 'relay coding':
            return ('relay_coding','iframe')
        elif computer == 'web tricks':
            return ('web_tricks','iframe')
        elif computer == 'cyber hunt':
            return ('cyber_hunt','iframe')
        
    elif mechanical:
        if mechanical == 'general':
            return (mech_text, 'text')
        elif mechanical == 'robo race':
            return ('robo_race','iframe')
        elif mechanical == 'lathe war':
            return ('lathe_war','iframe')
        elif mechanical == 'cad champs':
            return ('cad_champs','iframe')
        elif mechanical == 'mech quiz':
            return ('mech_quizs','iframe')

    elif chemical:
        if chemical == 'general':
            return (chemical_text,'text')
        elif chemical == 'chem-o-quiz':
            return ('chem-o-quiz','iframe')
        elif chemical == 'chem-o-flow':
            return ('chem-o-flow','iframe')
        elif chemical == 'chem-o-car':
            return ('chem-o-car','iframe')
        
    else:
        return ("Sorry I dont get, what you are saying",'text')


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

@app.route('/cyber_hunt')
def cyber_hunt():
    return render_template('cyber_hunt.html') 

@app.route('/web_tricks')
def web_tricks():
    return render_template('web_tricks.html') 

@app.route('/relay_coding')
def relay_coding():
    return render_template('relay_coding.html') 

@app.route('/mech_quiz')
def mech_quiz():
    return render_template('mech_quiz.html') 

@app.route('/robo_race')
def robo_race():
    return render_template('robo_race.html') 

@app.route('/lathe_war')
def lathe_war():
    return render_template('robo_race.html') 

@app.route('/cad_champs')
def cad_champs():
    return render_template('cad_champs.html') 

@app.route('/chem-o-car')
def chem_o_car():
    return render_template('chem-o-car.html') 

@app.route('/chem-o-flow')
def chem_o_flow():
    return render_template('chem-o-flow.html') 

@app.route('/chem-o-quiz')
def chem_o_quiz():
    return render_template('chem-o-quiz.html') 

# run Flask app
if __name__ == "__main__":
    app.run(debug=True)