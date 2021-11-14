import numpy as np
import copy
import random
import datetime
import hashlib
huge=2147483647
amount=10000
elements=np.array([0]*amount)
indexed=np.array([0]*amount)
counter=0
minamt=0
maxamt=10000



def generate_1(min,max):
    global elements
    global amount
    i=0
    while i<amount:
        elements[i]=random.randint(min,max)
        i=i+1




def printArray(arr):
    i=0
    output_string=""
    while i<amount:
        output_string=output_string+str(arr[i])+", "
        i=i+1
    print(output_string)


#END OF INIT FUNCTIONS
######################################################################################################################################################
######################################################################################################################################################
#START OF INDEX 1


#this index method goes through everything in elements, and puts the smallest found element into 
#this method accesses the array amt^2 times
#not very optimized lol
def index_1(): 
    global elements
    global indexed
    global huge
    global counter
    i=0
    j=0
    minnum=huge
    minindex=-1
    while j<amount:
        i=0
        while i<amount:  
            current_element=elements[i]        
            if current_element<minnum:
               
               minnum=current_element
               minindex=i
            counter=counter+1  
            i=i+1    
        elements[minindex]=huge
        indexed[j]=minnum
        minnum=huge
        #comment this out if u dont want debug
        print(str(j)+"/"+str(amount))
        j=j+1


#END OF INDEX 1
######################################################################################################################################################
######################################################################################################################################################
#START OF INDEX 2


#this this index method goes through everything in elements,
#BUT it puts smallest AND largest amt into the sorted array
#it also remembers every element appended(might be slower?idk)
#THIS IS A BAD IDEA
#DONT USE UNLESS U CAN GET RID OF ISCHECKED FUNCTION
def index_2():
    global elements
    global indexed
    global counter
    global amount
    minnum=huge
    maxnum=0-huge
    i=0
    j=0
    k=0
    appended_index=np.array([-1]*amount)
    def isChecked(ind):
        
        
        i=0
        while i<amount:
            
            if appended_index[i]==ind:
                return True
                
            i=i+1
        return False


    minindex=-1
    maxindex=-1
    while j<amount/2:
        i=0
        
        while i<amount:
           
            if isChecked(i)==False: 
               current_element=elements[i]          

               if current_element<minnum:
               
                    minnum=current_element
                    minindex=i
                   
               if current_element>maxnum:

                    maxnum=current_element
                    maxindex=i  
                    
               counter=counter+1
            i=i+1
        appended_index[k]=minindex
        k=k+1
        appended_index[k]=maxindex
        k=k+1
        
        indexed[j]=minnum
        indexed[amount-1-j]=maxnum
        
        minnum=huge
        maxnum=0-huge
        #comment this out if u dont want debug
        print(str(j*2)+"/"+str(amount))
        j=j+1


#END OF INDEX 2
######################################################################################################################################################
######################################################################################################################################################
#START OF INDEX 3


#checks i and i+1 element, if i+1<i, swap places.
def index_3():
    global counter
    global indexed
    
   # inithash=hashlib.sha256()
   # inithash.update(indexed)
   # indexhash=inithash.hexdigest()
   # comparehash=0
   # while indexhash!=comparehash:
        #print("continuing since "+str(indexhash)+" is not equal to "+str(comparehash))
       # comparehash=indexhash

    #    i=0
    #    while i<amount-1:
    #        e1=indexed[i]
    #        e2=indexed[i+1]
    #        print("switched "+str(e1)+" and "+str(e2))
     #       if e1>e2:
    #           indexed[i]=e2
   #            indexed[i+1]=e1

               
               
     #       i=i+1
    #        counter=counter+2
       # inithash=hashlib.sha256()
       # inithash.update(indexed)
       # indexhash=inithash.hexdigest()
        
               



#END OF INDEX 3
######################################################################################################################################################
######################################################################################################################################################
#START OF USER INPUT AREA


start_time=datetime.datetime.now()
end_time=datetime.datetime.now()
print("Choose indexing mode:")
print("1: Goes through all elements every time")
print("2: Goes through all elements every time,BUT it puts smallest AND largest amt into the sorted array(pls use a even number for element amt btw)")
print("3: ")
mode=int(input())
amount=int(input("Enter amount of elements: "))
minamt=int(input("Enter minimum value for element generation: "))
maxamt=int(input("Enter maximum value for element generation: "))
generate_1(minamt,maxamt)
print("Generated array: ")
printArray(elements)
print("Indexing...")

if mode==1:
    start_time=datetime.datetime.now()
    index_1()
    end_time=datetime.datetime.now()
elif mode==2:
    start_time=datetime.datetime.now()
    index_2()
    end_time=datetime.datetime.now()
elif mode==3:
    indexed=copy.deepcopy(elements)
    start_time=datetime.datetime.now()
    index_3()
    end_time=datetime.datetime.now()
    
print("Indexing finished")
delta_time=end_time-start_time
print("Indexed:")
printArray(indexed)
print("Accessed array "+str(counter)+"times")
print("Time taken:")
print(delta_time)
input("Press Enter to continue...")
    



