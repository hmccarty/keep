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
        if gnote.title == '' and gnote.text == '':
            continue
        try:
            items = map(lambda x: (x.text, x.checked), gnote.items)
            note = keep.createList(gnote.title, items)
        except AttributeError:
            note = keep.createNote(gnote.title, gnote.text)
        finally:
            for glabel in gnote.labels.all():
                label = keep.findLabel(glabel.name)
                if label is None:
                    label = keep.createLabel(glabel.name)
                note.labels.add(label)
                
            note.labels.add(tmpLabel)

    keep.sync()



