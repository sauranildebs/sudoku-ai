import numpy as np

#function to print the board
def print_board(board):

    ROW_SIZE = len(board[0])
    COLUMN_SIZE = len(board[1])
    for i in range(ROW_SIZE):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -", end = "\n")
        for j in range(COLUMN_SIZE):
            if j % 3 == 0 and j != 0:
                print('|', end = " ")
            if j == 8:
                print(board[i][j], end='\n')
            else:
                print(board[i][j], end = " ")

#function to find empty spaces on the board
def find_empty(board):

    ROW_SIZE = len(board[0])
    COLUMN_SIZE = len(board[1])
    for row_idx in range(ROW_SIZE):
        for col_idx in range(COLUMN_SIZE):
            if board[row_idx][col_idx] == 0:
                return (row_idx, col_idx)    #return the position of empty space 
    return False

#function to check if the value is valid or not
def check_valid(board, value, position):

    ROW_SIZE = len(board[0])
    COLUMN_SIZE = len(board[1])
    #Checking the row for validity
    for row_idx in range(ROW_SIZE):  
        if board[position[0]][row_idx] == value and row_idx != position[1]:
            return False
        
    #Checking the column for validity
    for col_idx in range(COLUMN_SIZE):
        if board[col_idx][position[1]] == value and col_idx != position[0]:
            return False

    #checking the 3x3 box for validity
    row_box = position[0] // 3
    col_box = position[1] // 3
    for row_idx in range(row_box * 3, row_box * 3 + 3):         
        for col_idx in range(col_box * 3, col_box * 3 + 3):
            if board[row_idx][col_idx] == value and position != (row_idx, col_idx):
                return False

    return True

#function to update the domain of the board based on the current board state
def update_domain(board):

    new_domain = np.zeros((9,9)).tolist()  #initializing the domain of all variables to be 0
    for row_idx in range(len(board)):
        for col_idx in range(len(board[0])):
            #stores the domains of variables in the row_idx row, col_idx column, and 3x3 box
            list_row = set()   
            list_col = set()   
            list_box = set()   

            #if position is not empty and has a value, the domain contains only that value
            if board[row_idx][col_idx] != 0:
                new_domain[row_idx][col_idx] = [board[row_idx][col_idx]]

            #if empty position, domain is the possible values (1-9) that are not in the row/column/box
            else:
                #checking the row
                for k in range(len(board[0])):
                    if board[row_idx][k] != 0:
                        list_row.add(board[row_idx][k])

                #checking the column
                for k in range(len(board[0])):
                    if board[k][col_idx] != 0:
                        list_col.add(board[k][col_idx])

                #checking the 3x3 box
                row_box = row_idx // 3
                column_box = col_idx // 3
                for k in range(row_box * 3, row_box * 3 + 3):
                    for l in range(column_box * 3, column_box * 3 + 3):
                        if board[k][l] != 0:
                            list_box.add(board[k][l])

                domain_all = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
                domain_row = set()   #stores the possible values in the row
                domain_column = set()   #stores the possible values in the column
                domain_box = set()   #stores the possible values in the 3x3 box

                #Subtracting from the entire domain set will give the possible values (domain) for each variable
                domain_row = domain_all - list_row
                domain_column = domain_all - list_col
                domain_box = domain_all - list_box

                x = list(domain_row & domain_column & domain_box)
                # Intersection of all the lists to find the updated domains
                new_domain[row_idx][col_idx] = x

    return new_domain    #returs the updated domains