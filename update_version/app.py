from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html')


@app.route('/data', methods=['POST'])
def signUpUser():
    if request.method == "POST":
        data = request.get_json()

        print(data, "data")
    password = data['password']
    return json.dumps({'status':'OK','pass':password})


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=False)