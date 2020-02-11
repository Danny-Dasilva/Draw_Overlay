from flask import Flask, render_template, render_template
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask_sockets import Sockets
import json
from time import sleep
app = Flask(__name__)
app.debug = True

sockets = Sockets(app)

connections = []
messages = []
usernames = {}

@sockets.route("/chat")
def chat_socket(web_socket):
    print("connefc")
    global connections, usernames
    connections = add_socket(web_socket, connections)
    #data = json.loads(web_socket.receive())
    print(web_socket.receive())
    while not web_socket.closed:
        
        connections = remove_closed_sockets(connections)
        msg = 6
        sleep(.5)
        send_message(msg, connections)

def add_socket(web_socket, connections):
    return connections + [web_socket]

def remove_closed_sockets(connections):
    return [c for c in connections if not c.closed]

def send_message(message, connections):
    for socket in connections:
        socket.send(message)

@app.route('/')
def hello():
    return render_template('ss.html')
@app.route('/eee')
def eee():
    print("requestr")
    return 'eee'


if __name__ == '__main__':
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()