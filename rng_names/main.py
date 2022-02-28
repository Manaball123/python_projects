import random
import json
import time
names = []
lb = []
scores = []

dbName = "namesdb.txt"
elements = 1182
lbName = "lb.txt"
scoreName = "scores.txt"

maxLim = 999999999
seed = int(time.time())

def loadNames():

        global names
        with open(dbName,"r") as namesdb:
            for i in range(elements):

                names.append(namesdb.readline().strip())

def loadLeaderboards():
    global lb
    global scores
    with open(lbName,"r") as lbdb:
        lb = json.loads(lbdb.read())
    with open(scoreName,"r") as scoresdb:
        scores = json.loads(scoresdb.read())


def saveLeaderboards():
    global lb
    global scores
    with open(lbName,"w") as lbdb:
        lbdb.write(json.dumps(lb))
    with open(scoreName,"w") as scoresdb:
        scoresdb.write(json.dumps(scores))



def genNewName(times):
    "inserts name at ranking position"
    global lb
    global scores
    global seed
    lblen = len(lb)
    for i in range(times):
        doInsert = False
        seed += i * 99
        random.seed(seed)

        endstr = str(random.randint(0,1000))

        seed += i * 99
        random.seed(seed)

        name = names[random.randint(0,lblen)] + endstr

        seed += i * 99
        random.seed(seed)
        
        score = random.randint(0,maxLim)

        for i in range(lblen):
            if(scores[i] <= score):
                scores.insert(i,score)
                lb.insert(i,name)
                doInsert = True
                break

        if(doInsert == False):
            scores.append(score)
            lb.append(name)

def printLeaderboards():
    lblen = len(lb)
    for i in range(lblen):
        print(str(i + 1) + ". " + lb[i] + " : " + str(scores[i]))
        
        


loadNames()

loadLeaderboards()
genNewName(1000)
printLeaderboards()

saveLeaderboards()
input()