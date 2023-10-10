def lcv_heuristic(domain, position):
    """Returns the value in the position's domain with the least constraining value (LCV) heuristic.
    
    Input: current domain of the board and position where domain needs to be checked
    Output: Dictionary with the values that is least constraining in ascending order
    """

    if len(domain[position[0]][position[1]]) == 1:
        return domain[position[0]][position[1]]   #if domain size == 1, return the value itself

    lcv = {}    #for counting the number of domains
    list = domain[position[0]][position[1]]  #selecting the row of the given position
    for i in list:
        lcv[i] = 0

    #checking how many times that domain value appears in other unassigned variable's domain of row and storing in lcv
    for row_idx in range(len(domain[0])):
        for j in list:
            if j in (domain[position[0]][row_idx]) and row_idx != position[1]:
                lcv[j] += 1   #increment count whenever it appears

    #checking how many times that domain value appears in other unassigned variable's domain of column and storing in lcv
    for col_idx in range(len(domain[0])):
        for j in list:
            if j in domain[col_idx][position[1]] and col_idx != position[0]:
                lcv[j] += 1

    #check how many times that domain value appears in other unassigned variable's domain of that 3x3 box and store in lcv
    row_box = position[0] // 3
    column_box = position[1] // 3
    for row_idx in range(row_box * 3, row_box * 3 + 3):
        for col_idx in range(column_box * 3, column_box * 3 + 3):
            for j in list:
            #exclude the row and column corresponding to the position
                if row_idx!= position[0] and col_idx!= position[1] and j in domain[row_idx][col_idx]:
                    lcv[j] += 1

    return sorted(lcv, key = lcv.get)   #return domains in ascending order