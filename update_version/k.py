from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html')


@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username']
    password = request.form['password']
    print(user, password)
    return json.dumps({'status':'OK','user':user,'pass':password})


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=False)