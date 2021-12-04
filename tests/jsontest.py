import json

class test1:
    def __init__(self):
        self.interger=1
        self.float=1.1
        self.boolean=True
        self.string="string"
        self.array=["thing1","thing2"]



object1=test1()
def saveobj():
    with open("test.json","w") as f:
        var=json.dumps(object1)
        print(var)
        f.write(var)

def loadobj():
    with open("test.json","r") as f:
        var=f.read()
        object2=json.loads(var)
        print(object2)


saveobj()
loadobj()
