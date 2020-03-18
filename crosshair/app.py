from flask import Flask, render_template, request
import json

app = Flask(__name__)



app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def json_parse(data):
    data = json.dumps(data)
    data = json.loads(data)
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



@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/add_profile", methods=["POST"])
def add_profile():
    if request.method == "POST":
        data = request.get_json()
        data = json_parse(data)
        write_json(data)
    return "nothing"

@app.route("/delete_profile", methods=["POST"])
def delete_profile():
    print("called", request.method)
    if request.method == "POST":
        print("yeet")
        data = request.get_json()
        print(data)
        data = json_parse(data)
        delete_json(data)
    return "nothing"
if __name__ == '__main__':
    app.run()
