from flask import Flask, render_template, request
import json
from read_and_write import write_json
from wifi import search_wifi
app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def hello_world():
    return render_template('test.html')


@app.route('/data', methods=['POST'])
def data():
    if request.method == "POST":
        data = request.get_json()

        print(data, "data")
    
    return json.dumps({'status':'OK'})


@app.route('/getConnections', methods=['POST'])
def getConnections():
    if request.method == "POST":
        connection, wifi_list = search_wifi()
        write_json('connections', wifi_list)
        write_json('connected', connection)
    
    return json.dumps({'status':'OK'})


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=False)