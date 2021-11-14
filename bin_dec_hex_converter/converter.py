
fromUnit=10
inputNum=[]
dec=0
toUnit=16
output=[]
decArray=[]
formattedOutput=[]
formattedInput=[]
def outputFormat():
    global formattedOutput
    global output
    i = len(output)-1
    while i >=0:
        list.append(formattedOutput,output[i])
        i-=1
#lol thanks 3.10

def translate(inp):
    match inp:
        case 0:
            return("0")
        case 1:
            return("1")
        case 2:
            return("2")
        case 3:
            return("3")
        case 4:
            return("4")
        case 5:
            return("5")
        case 6:
            return("6")
        case 7:
            return("7")
        case 8:
            return("8")
        case 9:
            return("9")
        case 10:
            return("A")
        case 11:
            return("B")
        case 12:
            return("C")
        case 13:
            return("D")
        case 14:
            return("E")
        case 15:
            return("F")

def convert():
    outstr=""
    for i in range(len(formattedOutput)-1):
        outstr=outstr+translate(formattedOutput[i])
    return outstr


def inputFormat():
    global formattedInput
    global inputNum
    i = len(formattedInput)-1
    while i >=0:
        list.append(inputNum,formattedInput[i])
        i-=1
#converts input to dec
def toDec():
    global dec
    global inputNum
    #print("inputnum array is")
    #print(inputNum)
    i=0
    while i<len(inputNum):
        
        
        result=inputNum[i]*(fromUnit**i)
        #print("processing current digit which is "+str(inputNum[i])+ ",which results in "+str(result))
        dec=dec+result
        #print("this brings dec to "+ str(dec))
        i+=1


#outputs the num in desired format
def fromDec():
    global dec
    global output
    #gets the remainder, divides the dec number(repeat this)
    while dec>=toUnit:
        remainder=dec%toUnit
        dec=dec-remainder
        dec=dec/toUnit
        #print("dec is currently "+str(dec)+", appending remainder which is "+str(remainder))
        list.append(output,remainder)

    if dec!=0:
        list.append(output,dec)
fromUnit=int(input("Enter unit to convert from: "))
toUnit=int(input("Enter unit to convert to: "))
inpDigits=int(input("Enter input digits: "))
digCounter=1
formattedInput=[0]*inpDigits
while digCounter<=inpDigits:
    inputDig=int(input("Enter digit number " + str(digCounter)+": "))
    formattedInput[digCounter-1]=inputDig
    digCounter+=1


inputFormat()

toDec()

print("The number is "+str(dec)+" in denary")

fromDec()

outputFormat()
print("The output is:")
print(formattedOutput)
if int(input("Convert to string? Only works with <=16 units,input 1 for yes: "))==1:
    print(convert())

input("Press enter to continue...")

