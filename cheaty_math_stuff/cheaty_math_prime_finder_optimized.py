#bad optimization cuz lazy
#this shit goes though all numbers wtf so gay tbh
#if x cannot be divided by all primes in list(ie:has remainder in every number tested)
#x=prime
#SO EZ ITS SO MUCH FASTER 
#LESS GOOOOO
primes=[1,2]

def checkForRemainder(x,y):
    if x%y==0:
        return(False)
    else:
        return(True)

def isprime(x):
    j=1
    notprime=False
    limit=len(primes)
    
    while j<limit and notprime==False:

        if checkForRemainder(x,primes[j])==False:
            notprime=True
            break
        else:
            j=j+1
        
    if notprime==False:
        print(str(x)+" is a prime number")
        list.append(primes,x)

limit=int(input("Enter Search Range: "))

current_num=3
while current_num<=limit:    
    isprime(current_num)
    current_num=current_num+1

input("press enter to end program")








