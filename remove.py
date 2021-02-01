import gkeepapi
import os 
import sys
from decouple import config

def removeFromLabel(label):
    gnotes = keep.find(labels=[keep.findLabel(label)])
    for gnote in gnotes:
        gnote.delete()
    keep.sync()

if __name__ == '__main__':
    gkeepapi.node.DEBUG = True
    keep = gkeepapi.Keep()
    keep.login(config('GMAIL'), config('PWORD'))

    action = sys.argv[1]
    if action == 'label':
        label = sys.argv[2]
        removeFromLabel(label)