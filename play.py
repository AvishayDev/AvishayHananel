import alphaBeta
import game

board=game.game()
game.create(board)
print("Initial Game")
game.printState(board)
game.decideWhoIsFirst(board)
comp_count = 0
average = 0
for i in range(10):
    for i in range(0,100):#This loops takes about 15 seconds on my computer
    #for i in range(0,50):
        while not game.isFinished(board):
            if game.isHumTurn(board):
                game.inputRandom(board)
                #game.inputMove(board)
            else:
                board=alphaBeta.go(board)
            #game.printState(board)
        if game.value(board)==10**20: #the computer (or smart agent) won
            comp_count+=1
        #print("Start another game")
        game.create(board)
    average += comp_count
    print("The agent beat you:", comp_count, " out of ", i + 1)
    comp_count = 0
print("the Average of 10 sets of 100 games is:", average/10)
print("Your grade in this section would be ", max((average/10)-80,0), " out of 20 ")
#print("Your grade in this section would be ", max(comp_count-40,0)*2, " out of 20 ")

