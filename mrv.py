def mrv_heuristic(board, domain):
    """Returns the position of the variable with the minimum remaining values (MRV) heuristic.
    
    Input: 9x9 matrix containing the domains of the current state of the board
    Output: [row, column] containing the position of a variable with minimum domain size
    """

    ROW_SIZE = len(board[0])
    COLUMN_SIZE = len(board[1])
    empty_space = []  #stores the empty spaces
    min_dom_position = []   #stores the positions of vars with minimum domain size

    #finding all the unassigned variables and storing their postions in the empty_space list
    for i in range(ROW_SIZE):
        for j in range(COLUMN_SIZE):
            if board[i][j] == 0:
                empty_space.append([domain[i][j],[i,j]])

    #finding the minumum length of domains in the empty_space list
    min_domain = len(empty_space[0][0])
    for k in range(1,len(empty_space)):
        if len(empty_space[k][0]) < min_domain:
            min_domain = len(empty_space[k][0])

    #storing the positions of variables with the minimum domain size in the min_dom_position list
    for l in range(len(empty_space)):
        if len(empty_space[l][0]) == min_domain:
            min_dom_position.append(empty_space[l][1])

    return min_dom_position[0]  #return one of the positions with minimum domain size