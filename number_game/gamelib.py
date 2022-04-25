import numpy as np


#special addition rule for the game
def Addition(num1, num2):
    return (num1 + num2) % 10


class Player:
    def __init__(self, numbers_count):
        self.numbers = np.array([1] * numbers_count)
    
    def Add(self, self_index, target_player, target_index):
        #if the self or target doesnt have a zeroed out number
        if(self.numbers[self_index] != 0 and target_player.numbers[target_index] != 0):
            self.numbers[self_index] = Addition(self.numbers[self_index], target_player.numbers[target_index])
            #success
            return 1
        #error code thing
        else:
            return 0
    
class Game:
    def __init__(self, numbers_count, players):
        self.players = []
        self.numbers_count = numbers_count
        self.players_count = players
        for i in range(players):
            self.players.append(Player(numbers_count))

        self.players = np.array(self.players)
    
    def PrintBoard(self):
        for i in range(len(self.players)):
            print("PLAYER " + str(i) + ": " + str(self.players[i].numbers))

    #runs the game loop once
    def Run(self):
        print("START OF GAME")
        
        #iterates through all players
        
        for i in range(len(self.players)):
            success = False
            self_player = self.players[i]
            print("CURRENT BOARD: ")
            self.PrintBoard()
            print("PLAYER " + str(i) + "'s turn: ")
            #listen for user input here
            while not success:
                try:
                    target_player_index = int(input("Enter target player's index: "))
                    self_index = int(input("Enter number of index from self to add to: ") - 1)
                    target_index = int(input("Enter number of index of target to add from: ") - 1)
                    target_player = self.players[target_player_index]
                    if(self_player.Add(self_index, target_player, target_index) != 0 ):
                        print("Addition success")
                        success = True
                except:
                    print("Invalid input")
        print("END OF TURN")



