

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



def run_server():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--source',
                        help='/dev/videoN:FMT:WxH:N/D or .mp4 file or image file',
                        default='/dev/video1:YUY2:640x480:30/1')
    parser.add_argument('--bitrate', type=int, default=1000000,
                        help='Video streaming bitrate (bit/s)')
   

    
    args = parser.parse_args()

  
    camera = Camera()

    with StreamingServer(camera, args.bitrate) as server:
        
        signal.pause()

def main():
    

    run_server()
    # t1 = threading.Thread(target=run_server, name=run_server, args=(q,))

    # t1.start()
    
    
       
if __name__ == '__main__':
    main()
