#!/usr/local/bin/python3

import os, time, sys, json, pymongo

pipe_name = 'pipe_test'

def Connect():
    client = pymongo.MongoClient()
    dummyDB = client['dummyDB']
    collection = dummyDB['dummyCollection']
    return {'client':client,'db':dummyDB,'col':collection}

def Send(startFrom=5,volume=10):
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    details = Connect()
    while True:
        time.sleep(1)
        toProcess = {'toProcess':[(record['url'],record['result']) for record in details['col'].find().skip(startFrom).limit(volume)],'flags':None}
        os.write(pipeout, ("Number-"+str(counter)+"\n"+json.dumps(toProcess)+"\n\n").encode('utf-8'))
        counter = (counter+1) % 5

if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)

Send(15)
