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


@sockets.route("/chat")
def chat_socket(web_socket):
    print("ahhh")
    global connections
    connections = add_socket(web_socket, connections)
    #data = json.loads(web_socket.receive())
    
    
        
    while not web_socket.closed:
        
        connections = remove_closed_sockets(connections)
        msg = [2, 2, 2, 2, 2,3 ,4 ,6]
        for value in msg:
            if value == 6:
                print("web_socket.close()")
            send_message(value, connections)
            

def add_socket(web_socket, connections):
    return connections + [web_socket]

def close_all():
    connections = []

def remove_closed_sockets(connections):
    print("removed")
    return [c for c in connections if not c.closed]

def send_message(message, connections):
    for socket in connections:
        socket.send(message)

@app.route('/')
def hello():
    return render_template('ss.html')
@app.route('/eee')
def eee():
    close_all()
    print("requestr")
    return 'eee'


if __name__ == '__main__':
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()