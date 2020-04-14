#check whether the sudoku board is complete or not
def isfull(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

#print the sudoku grid
def display(board):
    for i in range(9):      #iterate through rows
        if i%3 == 0 and i!=0:
            print('- - - - - - - - - - - ')

        for j in range(9):    #iterate through every element in a row
            if j%3 == 0 and j!=0:
                print('| ',end = '')
            
            if j == 8:     #if last number of a row
                print(board[i][j])
            else:
                print(str(board[i][j])+' ',end = '')


#to get the possible numbers that can be put in a particular square
def possiblities(board, i, j):
    q = []
    w = []
    for n in range(10):
        q.append(0)
    
    

    #check horizontally
    for n in range(9):
        if board[i][n] != 0:
            q[board[i][n]] = 1
    
    #check vertically
    for n in range(9):
        if board[n][j] != 0:
            q[board[n][j]] = 1
    
    #check every grid of 3x3
    a = (i // 3)*3
    b = (j // 3)*3
    for x in range(a,a+3):
        for y in range(b,b+3):
            if board[x][y] != 0:
                q[board[x][y]] = 1
    
    #generate list of possiblities
    for j in range(10): 
        if q[j] == 0:
            w.append(j)
    
    return w

#solve the board
def solve(board):
    i = 0
    j = 0
    #check if board is full
    if isfull(board):
        print('Sudoku solved successfully')
        display(board)
        return
    else:
        for x in range(9):    #check for an empty square
            for y in range(9):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
          
        #get all possiblities in i,j
        w = possiblities(board, i, j)
        for x in range (len(w)):
            if not w[x] == 0:
                board[i][j] = w[x]
                solve(board)
        # backtrack
        board[i][j] = 0                


def main():
    board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ]

    display(board)
    print('              ')
    print('              ')
    solve(board)
    

if __name__ == "__main__":
    main()   

