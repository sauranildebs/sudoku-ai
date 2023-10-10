# Sudoku Solver with Constraint Satisfaction Problem (CSP)

This Sudoku solver is implemented using the Constraint Satisfaction Problem (CSP) framework. We'll discuss what CSP is and how it can be used to solve Sudoku puzzles. We'll also explore some key techniques employed in this solver.

## 1. What is CSP and why it can be used to solve a Sudoku board

Constraint Satisfaction Problem (CSP) is a mathematical framework for solving problems where variables must satisfy certain constraints. In the case of Sudoku, CSP is used because it provides an elegant way to represent and solve the puzzle.

**Sudoku CSP:**
- **Variables:** Each cell in the Sudoku grid is a variable.
- **Domains:** The domain of each variable is the set of possible values (1-9 for traditional Sudoku).
- **Constraints:** The constraints are the Sudoku rules: no repeated values in rows, columns, and 3x3 boxes.

CSP solvers, like this one, systematically explore the solution space by assigning values to variables while respecting the constraints until a solution is found.

## 2. Backtracking Search

Backtracking search is a common technique for solving CSPs like Sudoku. It works as follows:
- Choose an unassigned variable.
- Try assigning a value from its domain.
- If it violates any constraints, backtrack (undo the assignment) and try the next value.
- Repeat this process until a solution is found or it's determined that no solution exists.

This solver employs backtracking to explore the Sudoku puzzle's solution space.

## 3. Forward Checking

Forward Checking is an optimization technique used with backtracking in CSP solving. It keeps track of remaining legal values for unassigned variables and helps prune the search space more quickly.

In Sudoku:
- When a value is assigned to a cell, the domains of its peers (cells in the same row, column, and box) are updated.
- If a peer has no legal values left, it means the current assignment is invalid, and we backtrack.

Forward Checking helps reduce the number of invalid assignments, making the Sudoku solver more efficient.

## 4. Minimum Remaining Variable (MRV)

MRV is a heuristic used to select the most constrained variable in a CSP. In Sudoku solving, MRV chooses the variable (cell) with the fewest remaining legal values.

By selecting the variable with MRV, we focus on the cells that are likely to cause conflicts early in the search, which can help find a solution faster.

## 5. Least Constraining Value

LCV is a heuristic used to select the value that minimizes constraints on other variables when assigning a value to a variable. In Sudoku solving, LCV chooses the value that minimizes the impact on its peers (cells in the same row, column, and box).

LCV helps make better decisions during variable assignment, reducing the likelihood of backtracking and potentially speeding up the solving process.

## 6. GUI

It includes a GUI built using the tkinter library. The GUI provides a visually appealing way to solve Sudoku puzzles and has options for choosing different CSP heuristics.

![Sudoku Solver GUI](gui_img)

## 7. Usage

To use this Sudoku solver with CSP:
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Save your Sudoku problem in the sudoku_easy or sudoku_hard file (empty cells represented as 0s).
4. Run the GUI using python3 Sudoku.py.
5. Select the heuristics you want to use in th GUI and then click Solve.
