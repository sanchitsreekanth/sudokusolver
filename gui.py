import pygame
import sys
import sudoku
from sudoku import ret, board, solve
import time

#initialisation
black = (0,0,0)
grey = (128,128,128)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green  = (0,255,0)
cell = 60

#save solved board to variable grid using ret function
solve(board)
grid = sudoku.ret()


class Sudoku:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600,600))
        pygame.display.set_caption('SUDOKU')
        self.running = True
        self.mousepos = None
        self.selected = None
        self.font = pygame.font.SysFont('arial', 30)
        self.fontnew = pygame.font.SysFont('comicsans', 60)
        self.fontn = pygame.font.SysFont('comicsans', 60)
        self.board = board
        self.count = 0
        self.chances = 5
        self.runtime = 0
    #main function in the class
    def run(self):
        start = time.time()
        while self.running:
            self.runtime = round(time.time()-start)
            self.events()
            self.draw()
        pygame.quit()
        sys.exit()


    #function to manipulate the sudoku grid and get user input
    def events(self):

        for event in pygame.event.get():    #quit the program 
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:     #check when a key is pressed
                self.mousepos = pygame.mouse.get_pos()
                (x,y) = self.mousepos
                if x in range(30,570) and y in range(5,545) and self.board[self.selected[1]][self.selected[0]] == 0:    #checks if selected space is in grid and selected cube is empty
                    if str.isdigit(event.unicode):
    
                        if int(event.unicode) == grid[self.selected[1]][self.selected[0]] :
                            self.board[self.selected[1]][self.selected[0]] = int(event.unicode)   #checks with 'grid' and fills square if correct
                            self.running = self.isfinished(self.board)
                        else:
                            print('wrong')
                            self.count = self.count + 1     #if number entered wrong number rejected 
                            if self.count == 5:              #if 5 wrong tries then program exits
                                self.running =  False

                #to check for arrow key pressed and move the slected square accordingly
                if event.key == pygame.K_LEFT:
                    [x,y] = self.selected
                    [a,b] = [x-1,y]
                    if a in range(0,9) and b in range(0,9):
                        self.selected = [a,b]
                    else:
                        self.selected = [x,y] 

                if event.key == pygame.K_RIGHT:
                    [x,y] = self.selected
                    [a,b] = [x+1,y]
                    if a in range(0,9) and b in range(0,9):
                        self.selected = [a,b]
                    else:
                        self.selected = [x,y] 

                if event.key == pygame.K_UP:
                    [x,y] = self.selected
                    [a,b] = [x,y-1]
                    if a in range(0,9) and b in range(0,9):
                        self.selected = [a,b]
                    else:
                        self.selected = [x,y]     

                if event.key == pygame.K_DOWN:
                    [x,y] = self.selected
                    [a,b] = [x,y+1]
                    if a in range(0,9) and b in range(0,9):
                        self.selected = [a,b]
                    else:
                        self.selected = [x,y]             
                        
                            

            if event.type == pygame.MOUSEBUTTONDOWN:             #to obtain which square is selected
                self.mousepos = pygame.mouse.get_pos()
                (x,y) = self.mousepos
                if x in range(30,570) and y in range(5,545):
                    self.selected = [(x-30)//cell,(y-5)//cell]
                    
                else:
                    self.selected = None
    #fucntion to draw all the required stuff in the pygame window
    def draw(self):          
        self.window.fill(black)    #creates window
        self.drawtime(self.window, self.clocktime(self.runtime))  #clock
        if self.selected != None:
            self.drawselection(self.window, self.selected)   
        self.drawnumbers(self.window)    
        self.mistake(self.window, self.count)   #mistake 
        self.drawgrid(self.window)   
        pygame.display.update()

    
    #draws sudoku 9x9 grid
    def drawgrid(self,window):
        pygame.draw.rect(window, white, (30,5,540,540),2)
        for i in range(9):
            pygame.draw.line(window, white,(30 + (cell*i), 5), (30+(cell*i), 545), 2 if i==3 or i==6 else 1)
            pygame.draw.line(window, white,(30, 5+(cell*i)), (570, 5+(cell*i)), 2 if i==3 or i==6 else 1)

    #selects a square 
    def drawselection(self, window, pos):
            [i,j] = [(pos[0]*cell)+30,(pos[1]*cell)+5]
            pygame.draw.rect(self.window, grey,(i,j,cell,cell))

    #draws numbers in selected square
    def drawnumbers(self, window):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    pos = [(j*cell)+30,(i*cell)+5]
                    self.text(pos, str(self.board[i][j]), self.window)

    #text initialisation
    def text(self, pos, num, window):
        font = self.font.render(num, True, white)
        h = font.get_height()
        w = font.get_width()
        pos[0] = pos[0] + (cell-w)//2
        pos[1] = pos[1] + (cell-h)//2
        window.blit(font, pos)
    
    #draw an X for mistake
    def mistake(self, window,count):
        font = self.font.render('X', True, red)
        y = 555
        for i in range(self.count):
            x = 30 + (i*20)
            window.blit(font, [x,y])

    #function to return the time since game has started      
    def clocktime(self, time):
        sec = time%60
        min = time//60
        hour = min//60
        if sec<10:
            seconds = '0'+str(sec)
        else:
            seconds = str(sec)
        clock = ' '+str(min)+':'+seconds
        return clock

    #draw the clock
    def drawtime(self, window, time):
        font = self.fontnew.render(time, True, blue)
        pos = [500,555]
        window.blit(font, pos)

    #check if board is finished
    def isfinished(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return True
        return False



if __name__ == '__main__':
    a = Sudoku()
    a.run()


