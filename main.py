
columns = [] #columns is the locations for each of the queens
# columns[r] is a number c if a queen is placed at row r and column c.
size = 4
import random #hint -- you will need this for the following code: column=random.randrange(0,size)

def place_n_queens(size):
    columns.clear()
    row = 0
    while row < size:
        column=random.randrange(0,size-1)
        columns.append(column)
        row+=1

def display():
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


def place_in_next_row(column):
    columns.append(column)


def remove_in_current_row():
    if len(columns) > 0:
        return columns.pop()
    return -1


def next_row_is_safe(column):
    row = len(columns)
    # check column
    for queen_column in columns:
        if column == queen_column:
            return False

    # check diagonal
    for queen_row, queen_column in enumerate(columns):
        if queen_column - queen_row == column - row:
            return False

    # check other diagonal
    for queen_row, queen_column in enumerate(columns):
        if ((size - queen_column) - queen_row
                == (size - column) - row):
            return False
    return True


def solve_queen(size):
    columns.clear()
    number_of_moves = 0 #where do I change this so it counts the number of Queen moves?
    number_of_iterations = 0
    row = 0
    column = 0
    # iterate over rows of board
    while True:
        #place queen in next row
        ''''print(columns)
        print("I have ", row, " number of queens put down")
        display()
        print(number_of_moves)'''
        while column < size:
            number_of_iterations+=1
            if next_row_is_safe(column):
                place_in_next_row(column)
                number_of_moves += 1
                row += 1
                column = 0
                break
            else:
                column += 1
        # if I could not find an open column or if board is full
        if (column == size or row == size):
            number_of_iterations+=1
            # if board is full, we have a solution
            if row == size:
                print("I did it! Here is my solution")
                display()
                #print(number_of_moves)
                return number_of_iterations, number_of_moves
            # I couldn't find a solution so I now backtrack
            prev_column = remove_in_current_row()
            if (prev_column == -1): #I backtracked past column 1
                print("There are no solutions")
                #print(number_of_moves)
                return number_of_iterations, number_of_moves
            # try previous row again
            row -= 1
            number_of_moves += 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column

def britian_solve():

    number_of_iterations = 0
    #
    # while not good match:
    #    place_n_queens(size)
    # return answer


def main():
    size = int(input('Enter n: '))
    iter, sum = solve_queen(size)
    print("# of iterations:", iter)
    print("# of queens placed + backtracks:", sum)
    print(columns)
main()