#!/usr/local/bin/python3

import pymongo

def Connect():
    client = pymongo.MongoClient()
    client.drop_database('dummyDB')
    dummyDB = client['dummyDB']
    collection = dummyDB['dummyCollection']
    return {'client':client,'db':dummyDB,'col':collection}

def Populate(connectionDetails = {}):
    if connectionDetails == {}:
        return
    collection = connectionDetails['col']
    for number in range(0,1000):
        entry = {'url':'www.'+str(number)+".com","result":str(-1)}
        collection.insert_one(entry)

def Main():
    connectionDetails = Connect()
    Populate(connectionDetails)

if __name__=='__main__':
    Main()
