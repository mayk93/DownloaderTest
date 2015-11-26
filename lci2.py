#!/usr/local/bin/python3

import os, time, sys, json, pymongo

lci_to_dld = 'lci_to_dld'

def Connect():
    client = pymongo.MongoClient()
    dummyDB = client['dummyDB']
    collection = dummyDB['dummyCollection']
    return {'client':client,'db':dummyDB,'col':collection}

def Send(startFrom=5,volume=10):
    pipeout = os.open(lci_to_dld, os.O_WRONLY)
    counter = 0
    details = Connect()
    while True:
        time.sleep(1)
        toProcess = {'toProcess':[(record['url'],record['result']) for record in details['col'].find().skip(startFrom).limit(volume)],'flags':None}
        os.write(pipeout, (json.dumps(toProcess)).encode('utf-8'))

if not os.path.exists(lci_to_dld):
    os.mkfifo(lci_to_dld)

Send(15)
