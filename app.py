import os
from flask import Flask, render_template, request
import json


app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def read_json(selector):
    with open('static/data.json') as json_file:

        read = json.load(json_file)
        data = read[selector]
    json_file.close()
    return(data)
        

def write_json(nput):
    with open('static/data.json') as f:
        
        try:
            data = json.load(f)
            data.update(nput)
        except:
            data = nput
       
        

    with open('static/data.json', 'w') as f:
        json.dump(data, f)
    f.close()


def delete_json(nput):
    with open('static/data.json') as f:
        
        
        data = json.load(f)
        print(data, "input", nput)
        del data[nput] 

    with open('static/data.json', 'w') as f:
        json.dump(data, f)
    f.close()



def json_parse(data):
    data = json.dumps(data)
    data = json.loads(data)
    return(data)

@app.route('/')
def index():
    return render_template('key_combo_write.html')

@app.route("/add_profile", methods=["POST"])
def add_profile():
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        write_json(data)
    return "nothing"

@app.route("/delete_profile", methods=["POST"])
def delete_profile():
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        delete_json(data)
    return "nothing"

if __name__ == '__main__':
    app.run()
