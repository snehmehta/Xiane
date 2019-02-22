from flask import Flask, request, jsonify, render_template,url_for
import os
import requests
import json
from wit import Wit
import json

access_token = "DXRQXBGEAYGVY5PKLUELZW4BFQWWPWXW"

app = Flask(__name__)

# with open("everything.txt",'r') as f:
#     everything_text = f.read()

with open("computer.txt",'r') as f:
    computer_text = f.read()

with open("chemical_text.txt",'r') as f:
    chemical_text = f.read()

with open("mech_text.txt",'r') as f:
    mech_text = f.read()

with open("civil_text.txt",'r') as f:
    civil_text = f.read()

with open("electrical_text.txt",'r') as f:
    electrical_text = f.read()

with open("general_text.txt",'r') as f:
    general_text = f.read()

with open("gaming_text.txt",'r') as f:
    gaming_text = f.read()


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
    electrical = first_entity_value(entities,'electrical')
    gaming = first_entity_value(entities,'gaming')
    general = first_entity_value(entities,'general')    
    invalid = first_entity_value(entities,'invalid')    


    if creator:
        return ("BrainChild of Sneh Mehta and Beautify by Nimit Patel",'text')
    elif greeting:
        return ('everything','iframe')
    elif everything:
        return ('everything','iframe')
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
        
    elif civil:
        if civil == 'general':
            return (civil_text, 'text')
        elif civil == 'sustainable planning':
            return ('sustainable_planning','iframe')
        elif civil == 'sarjan setu':
            return ('sarjan_setu','iframe')
        elif civil == 'civil quiz':
            return ('civil_quiz','iframe')
        elif civil == 'aakruti':
            return ('aakruti','iframe')
        
    elif electrical:
        if electrical == 'general':
            return (electrical_text, 'text')
        elif electrical == 'magnetic labyrinth':
            return ('magnetic_labyrinth','iframe')
        elif electrical == 'circuitrix':
            return ('circuitrix','iframe')
        elif electrical == 'laser maze':
            return ('laser_maze','iframe')
        elif electrical == 'electrical quiz':
            return ('electrical_quiz','iframe')
        elif electrical == 'electrical analogy':
            return ('electrical_analogy','iframe')
        
    elif general:
        if general == 'general':
            return (general_text, 'text')
        elif general == 'treasure hunt':
            return ('treasure_hunt','iframe')
        elif general == 'mock placement':
            return ('mock_placement','iframe')
        elif general == 'paper presentation':
            return ('paper_presentation','iframe')
        elif general == 'poster presentation':
            return ('poster_presentation','iframe')

    elif gaming:
        if gaming == 'general':
            return (gaming_text, 'text')
        elif gaming == 'gully cricket':
            return ('gully_cricket','iframe')
        elif gaming == 'cs go':
            return ('cs_go','iframe')
        elif gaming == 'pubg':
            return ('pubg','iframe')

    elif invalid:
        return ('I can only anwser questions related to TekXianze')

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

@app.route('/everything')
def everything():
    return render_template('everything.html') 

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
    return render_template('lathe_war.html') 

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

@app.route('/sustainable_planning')
def sustainable_planning():
    return render_template('sustainable_planning.html')

@app.route('/sarjan_setu')
def sarjan_setu():
    return render_template('sarjan_setu.html')

@app.route('/civil_quiz')
def civil_quiz():
    return render_template('civil_quiz.html') 

@app.route('/aakruti')
def aakruti():
    return render_template('aakruti.html') 

@app.route('/laser_maze')
def laser_maze():
    return render_template('laser_maze.html') 

@app.route('/electrical_analogy')
def electrical_analogy():
    return render_template('electrical_analogy.html') 

@app.route('/magnetic_labyrinth')
def magnetic_labyrinth():
    return render_template('magnetic_labyrinth.html') 

@app.route('/electrical_quiz')
def electrical_quiz():
    return render_template('electrical_quiz.html') 

@app.route('/poster_presentation')
def poster_presentation():
    return render_template('poster_presentation.html') 

@app.route('/paper_presentation')
def paper_presentation():
    return render_template('paper_presentation.html') 

@app.route('/mock_placement')
def mock_placement():
    return render_template('mock_placement.html') 

@app.route('/treasure_hunt')
def treasure_hunt():
    return render_template('treasure_hunt.html') 

@app.route('/gully_cricket')
def gully_cricket():
    return render_template('gully_cricket.html') 

@app.route('/cs_go')
def cs_go():
    return render_template('cs_go.html') 

@app.route('/pubg')
def pubg():
    return render_template('pubg.html') 


# run Flask app
if __name__ == "__main__":
    app.run(debug=True)
