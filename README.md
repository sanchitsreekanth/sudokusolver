# SUDOKU
Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contain all of the digits from 1 to 9. 
In this repo i have used **Webscraping** that directly scrapes a sudoku puzzle from the website http://nine.websudoku.com/ depending the level of difficulty which can be chosen by the user . The user can then play the game by trying to fill up the grid in the interface designed using the pygame library. The solution of the chosen sudoku puzzle is determinde using a backtracking algorithm that recursively solves the board

## Backtracking
Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
In this particular example we try filling digits one by one. Whenever we find that current digit cannot lead to a solution, we remove it (backtrack) and try next digit. This is better than naive approach (generating all possible combinations of digits and then trying every combination one by one) as it drops a set of permutations whenever it backtracks.
A good example of backtracking and recursive function is given [here](https://youtu.be/8lhxIOAfDss).

## Webscraping

Webscraping also called web data extraction, is the process of extracting or scraping data from websites. In this particular project the python library called BeautifulSoup is used for scraping the data from the sudoku website. It is a quick and easy way to parse data from HTML and XML files. More about BeautifulSoup can be found in the official documentation [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).


## PyGame
Pygame is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language. To install pygame check out the instructions given [here](https://www.pygame.org/wiki/GettingStarted).
To learn more aboot the various features and functionalities of pygame check out the documentation [here](https://www.pygame.org/docs/)

### sudoku.py
This file consist of the **display()** function to display the grid and the **solve()** which calls itself recursively and uses backtracking to solve the sudoku puzzle. Here the board is initialsed by taking the data scraped from the sudoku website using the **web.py** file

### gui.py
This python files consists of the code used to build the pygame window and takes the user input and allows the user to play the game.Whenever the user enters a number onto a selected square if the number is correct it accepts it or else it rejects
 it. If the user enters 5 incorrect tries he loses the game and in order to win he must fill up the grid within that limitation.
 
### web.py
This python file consists of the function **getboard()** used to scrape the sudoku puzzle of the website http://nine.websudoku.com/ using BeautifulSoup.
