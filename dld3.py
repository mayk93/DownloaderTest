#!/usr/local/bin/python3

import os, time, sys, json

pipe_name = 'pipe_test'

def Receive( ):
    pipein = open(pipe_name, 'r')
    while True:
        line = pipein.readline()[:-1]
        print(line)

if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)

Receive()
