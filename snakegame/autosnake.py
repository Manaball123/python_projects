import keyboard as key
import time
import numpy as np
"""
V < V <
V ^ < ^ <
V > > > ^
V ^ < < <
> > > > ^
or
V < V < <
V ^ <   ^
V > > > ^
V ^ < < <
> > > > ^
finish last segment manually


down: y-1
right: x-1
up: 1
::repeat::
    
    left: x-2
    up: 1
    right: x-2
    up: 1

(y-3)/2 times

EITHER:
    left: 1 
    up: 1
    left: 1


OR:
    up: 1
    left: 2


::repeat::
    down: 1
    left: 1
    up: 1
    left: 1

(x-3)/2 times

"""

unitDelay = 0.1
halt = True
x = 15
y = 15

halt_key = "f5"


class instructions:
    def __init__(self,keys,delays,loops):
        self.keys = keys
        self.delays = delays
        self.loops = loops 

    def execute(self):
        global halt
        i = 0
        currentTime = time.time()
        while i < self.loops and halt != True:
            j = 0 
            while j < len(self.keys) and halt != True:
                #break if halted
                if key.is_pressed(halt_key) or halt == True:
                    halt = True
                    return
                #if time is sufficient
                elif currentTime + self.delays[j] < time.time():
                    currentTime = time.time()
                    key.press_and_release(self.keys[j])
                    j += 1
            i += 1
                
        #extra delay after end of exec
        while currentTime + self.delays[len(self.delays) - 1] > time.time():
            #sleep
            pass

        return


#initial
keys1 = np.array(["s","d","w"])
del1 = np.array([0,y-1,x-1,1])


#loop1
keys2 = np.array(["a","w","d","w"])
del2 = np.array([0,x-2,1,x-2,1])

#init2, instance 1
keys3 = np.array(["a","w","a"])
del3 = np.array([0,1,1,1])

#init2, instance 2
keys4 = np.array(["w","a"])
del4 = np.array([0,1,2])

#loop 2
keys5 = np.array(["s","a","w","a"])
del5 = np.array([0,1,1,1,1])



inst1 = instructions(keys1,del1,1)
inst2 = instructions(keys2,del2,(y-3)/2)
inst31 = instructions(keys3,del3,1)
inst32 = instructions(keys4,del4,1)
inst4 = instructions(keys5,del5,(x-3)/2)


while halt != True:
    inst1.execute()
    inst2.execute()
    inst31.execute()
    inst4.execute()

    inst1.execute()
    inst2.execute()
    inst32.execute()
    inst4.execute()



    

        
        



