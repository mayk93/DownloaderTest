#!/usr/local/bin/python3

import os, time, sys, json, pymongo
pipe_name = 'pipe_test'

def Connect():
    client = pymongo.MongoClient()
    dummyDB = client['dummyDB']
    collection = dummyDB['dummyCollection']
    return {'client':client,'db':dummyDB,'col':collection}

def child(startFrom=5,volume=10):
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    details = Connect()
    collection = details['col']
    while True:
        time.sleep(1)
        toProcess = {'toProcess':[(record['url'],record['result']) for record in collection.find().skip(startFrom).limit(volume)],'flags':None}
        os.write(pipeout, ("Number-"+str(counter)+"\n"+json.dumps(toProcess)+"\n\n").encode('utf-8'))
        counter = (counter+1) % 5

def parent( ):
    pipein = open(pipe_name, 'r')
    while True:
        line = pipein.readline()[:-1]
        #line = pipein.readline()
        #print 'Parent %d got "%s" at %s' % (os.getpid(), line, time.time( ))
        print(line)

if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)
child(15)
#pid = os.fork()
#if pid != 0:
#    parent()
#else:
#    child()


"""
import os
import sys
import json
import pymongo

OUT = 0
IN = 1

outp = 'lci_to_dld'
inp = 'dld_to_lci'

def Connect():
    client = pymongo.MongoClient()
    dummyDB = client['dummyDB']
    collection = dummyDB['dummyCollection']
    return {'client':client,'db':dummyDB,'col':collection}

def CreatePipes(outp,inp):
    if not os.path.exists(outp):
        os.mkfifo(outp)
    pipe_out = os.open(outp, os.O_WRONLY)
    if not os.path.exists(inp):
        os.mkfifo(inp)
    pipe_in = os.open(outp, os.O_RDONLY)
    return pipe_out,pipe_in

class LCInterface(object):
    def __init__(self,connectionDetails={}):
        self.client = connectionDetails['client']
        self.dataBase = connectionDetails['db']
        self.collection = connectionDetails['col']
        self.lci_to_dld, self.dld_to_lci = CreatePipes(outp,inp)
    def SendLinks(self,startFrom=0,volume=10):
        # Note! skip is bad.
        toProcess = {'toProcess':[(record['url'],record['result']) for record in self.collection.find().skip(startFrom).limit(volume)],'flags':None}
        for linkNumber in range(0,volume):
            print(json.dumps(toProcess))
            os.write(self.lci_to_dld,json.dumps(toProcess))

def Main():
    lci = LCInterface(Connect())
    for startFrom in range(0,100,10):
        lci.SendLinks(startFrom=startFrom)

if __name__=='__main__':
    Main()
"""
