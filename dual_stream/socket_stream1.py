

import argparse
import logging
from flask import Flask, render_template, url_for, Response, request
import signal
import threading
import queue
from camera import Camera
from streaming.server import StreamingServer
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)

q = queue.Queue(maxsize=150)
qu = queue.Queue(maxsize=150)
def svg(q):
    while True:  
        c = q.get()
        yield c
@app.route('/')
def init():
    return render_template('test.html')

@app.route('/stream')
def stream():
    return render_template('index.html')

@sockets.route('/stream')
def yeet(socket):
    t = svg(q)
    for buffer in t:
        if buffer:
            
            socket.send(buffer)


def run_server(q):
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--source',
                        help='/dev/videoN:FMT:WxH:N/D or .mp4 file or image file',
                        default='/dev/video1:YUY2:640x480:30/1')
    parser.add_argument('--bitrate', type=int, default=1000000,
                        help='Video streaming bitrate (bit/s)')
   

    
    args = parser.parse_args()

  
    camera = Camera()

    with StreamingServer(camera, q, qu, args.bitrate) as server:
        
        signal.pause()

def main():
    

    
    t1 = threading.Thread(target=run_server, name=run_server, args=(q,))

    t1.start()
    t1.deamon = True
    http_server = WSGIServer(('',5000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
   
    #app.run(host="0.0.0.0", debug=False)
    
    
       
if __name__ == '__main__':
    main()
