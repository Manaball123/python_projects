import json




class test1:
    def __init__(self):
        self.a=1
        self.b="hi"
        self.c=[1,"hello"]

    def hi():
        print("hello")

with open("test.json","r+") as f:
    var=json.decoder.JSONDecoder.decode(f.read())
    print(var)

