#!/usr/bin/env python
import argparse
import zmq
from zmq.eventloop import ioloop, zmqstream
import json

HIDER_IP = '0.0.0.0'
HIDER_PORT = '5557'

io_loop = ioloop.IOLoop()

context = zmq.Context()

socket = context.socket(zmq.ROUTER)

CITIES = {'Ubatuba'}

stream = zmqstream.ZMQStream(socket, io_loop=io_loop)

def check_city_guess(stream, message):
    print "Got connection"
    _, city = message
    if city in CITIES:
        reply = 'CORRECT'
    elif:
        reply = 'INCORRECT'

    stream.send_multipart([identifier, reply])

stream.on_recv_stream(check_city_guess)

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bind-address', default='tcp://{}:{}'.format(HIDER_IP, HIDER_PORT))

args = parser.parse_args()

socket.bind(args.bind_address)
io_loop.start()