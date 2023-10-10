import tkinter as tk
import pandas as pd
from helper import find_empty, check_valid, update_domain
from mrv import mrv_heuristic
from lcv import lcv_heuristic
from forward_checking import forward_check

#reading the sudoku puzzle from a csv file and converting it into a list
df = pd.read_csv('sudoku_easy', header = None)  
#df = pd.read_csv('sudoku_hard', header = None)  
sudoku_puzzle = df.values.tolist()
is_FC = False     #Flag to check if Forward Checking is to be used or not
is_MRV = False  #Flag to check if MRV is to be used or not
is_LCV = False   #Flag to check if LCV is to be used or not

#function to solve the sudoku puzzle using backtracking search algorithm
def backtracking_search():
    global is_FC, is_MRV, is_LCV, domain  
    empty_pos = find_empty(sudoku_grid)   #check for empty space on the board
    if empty_pos == False:
        return True       #board solved

    if is_MRV:
        mrv_list = mrv_heuristic(sudoku_grid, domain)   #calling the MRV function to get the next variable to be assigned
        row_idx = mrv_list[0]
        column_idx = mrv_list[1]
    else:
        row_idx = empty_pos[0]     #row index of empty space
        column_idx = empty_pos[1]     #column index of empty space

    if is_FC:
        val_range = domain[row_idx][column_idx]
    elif is_LCV:
        val_range = lcv_heuristic(domain, mrv_list)  #calling LCV for which value to check
    else:
        val_range = range(1, 10)    #otherwise check all values from 1 to 9

    for num in val_range:    
        if is_FC:
            is_valid = forward_check(sudoku_grid, [row_idx, column_idx], num)  #forward checking
            if is_valid:
                sudoku_grid[row_idx][column_idx] = num      #assign value to board if valid forward check
                domain = update_domain(sudoku_grid)       #updating domains if assignment is valid
                update_cell(row_idx, column_idx, num)  #updating the GUI cell
                root.update_idletasks() 
                root.after(10)  #animation delay
                if backtracking_search():      
                    return True
                
            sudoku_grid[row_idx][column_idx] = 0
            update_cell(row_idx, column_idx, 0)  #clearing the GUI cell
            root.update_idletasks() 
            root.after(10)  
        else:
            if check_valid(sudoku_grid, num, [row_idx, column_idx]):  #check validity of current assignment
                sudoku_grid[row_idx][column_idx] = num    #if valid, assign to empty space
                update_cell(row_idx, column_idx, num)  
                root.update_idletasks()  
                root.after(10)  
                if backtracking_search():    
                    return True     
                  
                sudoku_grid[row_idx][column_idx] = 0    
                update_cell(row_idx, column_idx, 0)
                root.update_idletasks() 
                root.after(10)
    return False

#function to update a cell in the GUI
def update_cell(row, col, num):
    cell_labels[row][col]['text'] = str(num) if num != 0 else ""

#function to display the Sudoku grid
def display_sudoku():
    for i in range(9):
        for j in range(9):
            cell_value = sudoku_grid[i][j]
            cell_labels[i][j]['text'] = str(cell_value) if cell_value != 0 else ""

#switch to toggle forward checking, MRV and LCV
def toggle_FC():
    global is_FC
    is_FC = not is_FC

def toggle_MRV():
    global is_MRV
    is_MRV = not is_MRV

def toggle_LCV():
    global is_LCV
    is_LCV = not is_LCV

#main GUI window
root = tk.Tk()
root.title("SudokuAI")

#creating a subwindow for the Sudoku board using grid layout
board_frame = tk.Frame(root)
board_frame.grid(row=0, column=0, padx=10, pady=10)

#creating a 9x9 grid of Label widgets to display the Sudoku cells
cell_labels = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        cell_labels[i][j] = tk.Label(board_frame, text = "", font = ('Helvetica', 16), justify = 'center', width = 2, height = 1, borderwidth = 1, relief = 'solid')
        cell_labels[i][j].grid(row = i, column = j)

#creating a subwindow for the options using grid layout
options_frame = tk.Frame(root)
options_frame.grid(row = 0, column = 1, padx = 10, pady = 10)

fc_button = tk.Checkbutton(options_frame, text = "Forward Checking", command = toggle_FC)
fc_button.grid(row = 0, column = 0)

mrv_button = tk.Checkbutton(options_frame, text = "Minimum Remaining Value", command = toggle_MRV)
mrv_button.grid(row = 1, column = 0)

lcv_button = tk.Checkbutton(options_frame, text = "Least Constraining Value", command = toggle_LCV)
lcv_button.grid(row = 2, column = 0)

solve_button = tk.Button(options_frame, text = "Solve", command = backtracking_search)
solve_button.grid(row = 3, column = 0)

#initializing the Sudoku grid as a global variable
sudoku_grid = [[sudoku_puzzle[i][j] for j in range(9)] for i in range(9)]
domain = update_domain(sudoku_grid)

#displaying the Sudoku grid
display_sudoku()
#starting the GUI
root.mainloop()
