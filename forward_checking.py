from helper import update_domain

def forward_check(board, position, value):
    """Performs forward checking on the board given the position of empty space and value to add.
    
    Input: current board, position of empty space and value of empty space.
    Output: Boolean, True if forward checking is true otherwise false
    """
    
    board[position[0]][position[1]] = value  #adding the value to the board at the given position
    updated_domain = update_domain(board)  #updating domain based on current board state

    #checking if domain size of unassigned variables in the row == 0
    for row_idx in range(len(updated_domain[0])):
        if len(updated_domain[position[0]][row_idx]) == 0:
            return False    #return False if size 0 -> no valid assignment left

    #checking if domain size of unassigned variables in the column == 0
    for col_idx in range(len(updated_domain[0])):
        if len(updated_domain[col_idx][position[1]]) == 0:
            return False

    #checking if domain size of variables in the block == 0
    row_box = position[0] // 3
    col_box = position[1] // 3
    for row_idx in range(row_box * 3, row_box * 3 + 3):
        for col_idx in range(col_box * 3, col_box * 3 + 3):
            if len(updated_domain[row_idx][col_idx]) == 0:
                return False

    return True   #return True if current assignment is valid if no domains become empty