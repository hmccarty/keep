import gkeepapi
import os 
import sys
from decouple import config

if __name__ == '__main__':
    gkeepapi.node.DEBUG = True
    keep = gkeepapi.Keep()

    fromAcc = sys.argv[1]
    fromPass = sys.argv[2]

    toAcc = config('GMAIL')
    toPass = config('PWORD')

    keep.login(fromAcc, fromPass)
    gnotes = keep.all()
    keep.login(toAcc, toPass)

    tmpLabel = keep.findLabel('tmp')
    if tmpLabel is None: 
        tmpLabel = keep.createLabel('tmp')
    for gnote in gnotes:
        note = keep.createNote(gnote.title, gnote.text)
        note.labels = gnote.labels
        note.labels.add(tmpLabel)
        break

    keep.sync()



