import numpy as np
from pip._vendor.msgpack.fallback import xrange

n = 10
def createBoard(n):
    return np.zeros((n, n))


def placeQueen(board,column):
    #check if can place queen
    counter = 0#the row of placeing
    for i in xrange(n):
        if board[i][column] == 0: #if so return in which row
            return counter
        else:#else add one to row
            counter += 1
    return -1#if pass all rows with no place to place return mark -1

def markPlaceses(board,column,row):


    # check row & columns
    i=-1
    while i > -n:
        board[row][i] = 1
        board[i][column] = 1
        i-=1

    # check row
    for i in xrange(n):
        board[row][i] = 1

    i = 1
    # check diagonal
    while 0 <= column+i <= n-1 and 0 <= row+i <= n-1:
        board[row+i][column+i] = 1
        i += 1

    i = 1
    # check other diagonal
    while 0 <= column+i <= n-1 and 0 <= row-i <= n-1:
        board[row-i][column+i] = 1
        i += 1



def display(borad):
    #disply board
    for row in xrange(n):
        for column in xrange(n):
            if borad[row][column] == 2:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()



def main():
    columns = [] #for the place of queens
    board = createBoard(n) #our borad
    boardSaver = [] #state of the board before backtracking
    check = 0 #check if can place the queen and where to place it if can
    number_of_iterations = 0
    number_of_moves = 0

    for i in xrange(n): #initialize
        columns.append(0)

    i = 0#columns for checking
    while i < n:#while dont finish the borad
        number_of_iterations +=1
        check = placeQueen(board,i)#check where to place queen
        if check == -1:# queen cant be placed
            #do backwords
            board = boardSaver.pop()#take the old board
            i -= 1#go to prev column
            board[columns[i]][i] = 1 #replace mark of queen by 1
            number_of_moves +=1
        else:#queen can be placed in the row in check
            #place queen
            boardSaver.append(board.copy())#add the old board
            columns[i] = check #save the place of queen
            markPlaceses(board,i,columns[i])#mark the places cant set queen
            board[check][i] = 2 #mark place of queen by 2
            i += 1 #go to next column
            number_of_moves +=1

    display(board)#disply borad
    print(number_of_iterations,number_of_moves)#display num of iterators and moves



if __name__ == "__main__":
    main()
