#!/usr/local/bin/python3

import os, time, sys, json
pipe_name = 'pipe_test'

def child( ):
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    while True:
        time.sleep(1)
        os.write(pipeout, 'Number %03d\n' % counter)
        counter = (counter+1) % 5

def parent( ):
    pipein = open(pipe_name, 'r')
    while True:
        line = pipein.readline()[:-1]
        #line = pipein.readline()
        #print 'Parent %d got "%s" at %s' % (os.getpid(), line, time.time( ))
        print(line)
        #jsonDLD = json.loads(line)
        #print(jsonDLD)
        #print(type(jsonDLD))
        #print("\n")

if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
parent()

'''
import os
import sys
import json
import pymongo
import twisted

OUT = 0
IN = 1

inp = 'lci_to_dld'
outp = 'dld_to_lci'

def Connect():
    client = pymongo.MongoClient()
    dummyDB = client['dummyDB']
    collection = dummyDB['dummyCollection']
    return {'client':client,'db':dummyDB,'col':collection}

def CreatePipes(outp,inp):
    print("3")
    print(os.path.exists(outp))
    if not os.path.exists(outp):
        os.mkfifo(outp)
    print("4")
    print(os.path.exists(outp))
    pipe_out = os.open(outp, os.O_WRONLY)
    if not os.path.exists(inp):
        os.mkfifo(inp)
    pipe_in = os.open(outp, os.O_RDONLY)
    return pipe_out,pipe_in

def Main():
    print("2")
    pipeout,pipein = CreatePipes(outp,inp)
    while True:
        line = pipein.readline()[:-1]
        #print 'Parent %d got "%s" at %s' % (os.getpid(), line, time.time( ))
        print("Parent "+str(os.getpid())+" got "+str(line)+" at "+str(time.time()))

if __name__=='__main__':
    print("1")
    Main()
'''
