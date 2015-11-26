#!/usr/local/bin/python3

import os, time, sys, json

lci_to_dld = 'lci_to_dld'

def Receive( ):
    pipein = open(lci_to_dld, 'r')
    while True:
        line = pipein.readline()[:-1]
        print(line)

if not os.path.exists(lci_to_dld):
    os.mkfifo(lci_to_dld)
    
Receive()
