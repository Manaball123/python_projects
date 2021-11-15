#sorry i cba writing docs so ill just run through the concept here
#the ai should be able to learn your based on the most recent decision, idk how to make complex stuff rn so i wont
#generate random numbers first, use the results to modify the weights

#BRANCHES:
#1.calibration lasts 10 rounds. still uses rng for making decisions and does 
#minor adjustments to weights after every round(does not scale over time)

#2.calibiration lasts 30 rounds. DOES NOT USE RNG, instead uses the behavior formed from weights.

#HOW WEIGHTS WORK:
#if human win/lose/draw last round, do x action accordingly


#EXAMPLE OF LEARNING:
#round 1:human chooses ROCK and bot chooses SCISSORS(NO WEIGHT CHANGE FOR INITIAL ROUND)
#round 2:human chooses PAPER and bot chooses ROCK(use "LOSE ARRAY" for deciding, increase "LOSING DECISION" weight,in "LOSE ARRAY")
#round 3:human chooses SCISSORS and bot chooses ROCK(use "LOSE ARRAY" for deciding, further increase "LOSING DECISION" weight, in "LOSE ARRAY")
#IMPORTANT: since BOT WON this round, use "WIN ARRAY" for next round)
#round 4:human chooses PAPER, bot chooses PAPER(use "WIN ARRAY" for deciding, increase "SAME DECISION" weight, in "WIN ARRAY")
#round 5:human chooses ROCK, bot chooses PAPER,(use "DRAW ARRAY" for deciding, increase "SAME DECISION" weight, in "DRAW ARRAY")


#0=rock, 1=paper 2=scissors

#0=bot, 1=human

#-1=bot lose, 0=draw, 1=bot win


#(relative to opponent,last round)
#0=losing decision
#1=draw decision
#2=winning decision


#weight arrays

from math import radians
import random 
loseArray=[100/3]*3
drawArray=[100/3]*3
winArray=[100/3]*3

def ResultChecker(botInput,humanInput):
    if botInput==0:
        
        if humanInput==0:
            return(0)
        elif humanInput==1:
            return(-1)
        else:
            return(1)

    elif botInput==1:
        
        if humanInput==0:
            return(1)
        elif humanInput==1:
            return(0)
        else:
            return(-1)

    else:
        
        if humanInput==0:
            return(-1)
        elif humanInput==1:
            return(1)
        else:
            return(0)
    


def RandomDecider(weight_array,last_human_input):
    bot_decision=0
    #sec 1 is lose decision's weight
    sec1=weight_array[0]
    #sec 2 is draw decision's weight
    sec2=weight_array[1]+sec1
    #sec 3(doesnt exist to save memory)is win decision's weight
    #again these are all relative to last human input
    seed=random.randint(1,100)
    if seed<=sec1:
       bot_decision=0
    elif seed<=sec2:
       bot_decision=1
    else:
       bot_decision=2

    if last_human_input==0:
        if bot_decision==0:
            return(2)
        elif bot_decision==1:
            return(0)
        else:
            return(1)

    elif last_human_input==1:
        if bot_decision==0:
            return(0)
        elif bot_decision==1:
            return(1)
        else:
            return(2)

    else:
        if bot_decision==0:
            return(1)
        elif bot_decision==1:
            return(2)
        else:
            return(0)
        
#FUNCTION BELOW IS FOR BRANCH 2, AFTER CALIBRATION
def BehaviorBuilder():
    #im sure there's better ways to do this but im lazy
    global winArray
    global loseArray
    global drawArray
    if winArray[0]>winArray[1] and winArray[0]>winArray[2]:
        winArray[0]=100
        winArray[1]=0
        winArray[2]=0
    elif winArray[1]>winArray[0] and winArray[1]>winArray[2]:
        winArray[0]=0
        winArray[1]=100
        winArray[2]=0
    else:
        winArray[0]=0
        winArray[1]=0
        winArray[2]=100

    if loseArray[0]>loseArray[1] and loseArray[0]>loseArray[2]:
        loseArray[0]=100
        loseArray[1]=0
        loseArray[2]=0
    elif loseArray[1]>loseArray[0] and loseArray[1]>loseArray[2]:
        loseArray[0]=0
        loseArray[1]=100
        loseArray[2]=0
    else:
        loseArray[0]=0
        loseArray[1]=0
        loseArray[2]=100

    if drawArray[0]>drawArray[1] and drawArray[0]>drawArray[2]:
        drawArray[0]=100
        drawArray[1]=0
        drawArray[2]=0
    elif drawArray[1]>drawArray[0] and drawArray[1]>drawArray[2]:
        drawArray[0]=0
        drawArray[1]=100
        drawArray[2]=0
    else:
        drawArray[0]=0
        drawArray[1]=0
        drawArray[2]=100


#NO behavior here yet
def WeightTweaker(weightArray,delta,weightNumber):
    global loseArray
    global winArray
    global drawArray
    halfDelta=delta/2
    print("EDITING WEIGHT NUMBER: " + str(weightNumber))
    if weightArray==-1:
        print("LOSE ARRAY TWEAKED.")
        
        if weightNumber==0:
            loseArray[0]=loseArray[0]+delta
            loseArray[1]=loseArray[1]-halfDelta
            loseArray[2]=loseArray[2]-halfDelta
        elif weightNumber==1:
            loseArray[0]=loseArray[0]-halfDelta
            loseArray[1]=loseArray[1]+delta
            loseArray[2]=loseArray[2]-halfDelta
        else:
            loseArray[0]=loseArray[0]-halfDelta
            loseArray[1]=loseArray[1]-halfDelta
            loseArray[2]=loseArray[2]+delta
    


    
    elif weightArray==0:
        print("DRAW ARRAY TWEAKED.")
        if weightNumber==0:
            drawArray[0]=drawArray[0]+delta
            drawArray[1]=drawArray[1]-halfDelta
            drawArray[2]=drawArray[2]-halfDelta
        elif weightNumber==1:
            drawArray[0]=drawArray[0]-halfDelta
            drawArray[1]=drawArray[1]+delta
            drawArray[2]=drawArray[2]-halfDelta
        else:
            drawArray[0]=drawArray[0]-halfDelta
            drawArray[1]=drawArray[1]-halfDelta
            drawArray[2]=drawArray[2]+delta
    else:
        print("WIN ARRAY TWEAKED.")
        if weightNumber==0:
            winArray[0]=winArray[0]+delta
            winArray[1]=winArray[1]-halfDelta
            winArray[2]=winArray[2]-halfDelta
        elif weightNumber==1:
            winArray[0]=winArray[0]-halfDelta
            winArray[1]=winArray[1]+delta
            winArray[2]=winArray[2]-halfDelta
        else:
            winArray[0]=winArray[0]-halfDelta
            winArray[1]=winArray[1]-halfDelta
            winArray[2]=winArray[2]+delta
        

def DeltaCalculator(round_num):
    #hardcoded cuz lazy stay mad
    if round_num<=10:
        return(10)
    elif round_num<=30:
        return(5)
    else:
        return(100/round_num)

#this is scuffed but idgaf
def ResultAnalyzer(last_humanInput,humanInput):
    if last_humanInput==0:
        if humanInput==0:
            return(2)
        elif humanInput==1:
            return(0)
        else:
            return(1)
    elif last_humanInput==1:
        if humanInput==0:
            return(1)
        elif humanInput==1:
            return(2)
        else:
            return(0)
    else:
        if humanInput==0:
            return(0)
        elif humanInput==1:
            return(1)
        else:
            return(2)

    

#now for interactive part maybe
human_input=0
last_human_input=0
bot_input=0
programState=1
roundNum=1
print("0=rock, 1=paper 2=scissors")

print("Starting Round Number 1")
human_input=int(input("Enter Your Decision Here:  "))
bot_input=random.randint(0,2)
results=ResultChecker(bot_input,human_input)
if results==-1:
    print("You Won!")
    print("Bot Chose:"+str(bot_input))
if results==0:
    print("Draw!")
    print("Bot Chose:"+str(bot_input))
if results==1:
    print("You Lost!")
    print("Bot Chose:"+str(bot_input))

roundNum=roundNum+1
last_result=results
last_human_input=human_input


while programState==1:
    #WE NEED A FUNC TO FIND OUT WHAT THE BOT IS SUPPOSED TO DO 
    #REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    print("Starting Round Number"+str(roundNum))
    
    human_input=int(input("Enter Your Decision Here:  "))
    if results==-1:       
        bot_input=RandomDecider(loseArray,last_human_input)

    elif results==0:  
        bot_input=RandomDecider(drawArray,last_human_input)

    else:
        bot_input=RandomDecider(winArray,last_human_input)

    results=ResultChecker(bot_input,human_input)
    
    if results==-1:
        print("You Won!")
        print("Bot Chose: "+str(bot_input))
    elif results==0:
        print("Draw!")
        print("Bot Chose: "+str(bot_input))
    else:
        print("You Lost!")
        print("Bot Chose: "+str(bot_input))

    if results==-1:
        WeightTweaker(last_result,DeltaCalculator(roundNum),ResultAnalyzer(last_human_input,human_input))
        
    elif results==0:
        WeightTweaker(last_result,DeltaCalculator(roundNum),ResultAnalyzer(last_human_input,human_input))

    else:
        WeightTweaker(last_result,DeltaCalculator(roundNum),ResultAnalyzer(last_human_input,human_input))
    
    last_result=results
    last_human_input=human_input
    print("DEBUG: ")
    print("LOSE: "+str(loseArray))
    print("DRAW: "+str(drawArray))
    print("WIN: "+str(winArray))
    roundNum=roundNum+1

    
  

    
    


