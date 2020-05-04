# SUDOKU
Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contain all of the digits from 1 to 9. 
In this repo i have used backtracking algorithm to solve a sudoku puzzle when the initiaal unsolved but solvable state is given as an input. The user can then play the game by trying to fill up the grid in the interface designed using the pygame library

## Backtracking
Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
In this particular example we try filling digits one by one. Whenever we find that current digit cannot lead to a solution, we remove it (backtrack) and try next digit. This is better than naive approach (generating all possible combinations of digits and then trying every combination one by one) as it drops a set of permutations whenever it backtracks.
A good example of backtracking and recursive function is given [here](https://youtu.be/8lhxIOAfDss)

## PyGame
Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language. To install pygame check out the instructions given [here](https://www.pygame.org/wiki/GettingStarted).
To learn more aboot the various features and functionalities of pygame check out the documentation [here](https://www.pygame.org/docs/)

### sudoku.py
This file consist of the **display()** function to display the grid and the **solve()** which calls itself recursively and uses backtracking to solve the sudoku puzzle

### gui.py
This python files consists of the code used to build the pygame window and takes the user input and allows the user to play the game.Whenever the user enters a number onto a selected square if the number is correct it accepts it or else it rejects
 it. If the user enters 5 incorrect tries he loses the game and in order to win he must fill up the grid within that limitation.
