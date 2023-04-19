# objective of game is to select location to drop a 1, causing adjacent numbers to become 1 as well
# create AI and difficulty range to make it challenging

import random
import turtle
wn = turtle.Screen() # window screen using turtle
wn.title("reverseTheDarkness") # title of window
wn.bgcolor("white") # background color
wn.setup(800, 600) # screen size
wn.tracer(0) # lets us speed up games and doesn't let screen update


class game:
    def __init__(self):
        self.board = [[], [], [], [], [], [], [], [], []]
        for x in range(9):
            self.board[x] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.score = 0
        self.enemyScore = 0
        self.bonusTag = 0

    def printBoard(self):
        print("-----")
        print("   1  2  3  4  5  6  7  8  9")
        for x in range(9):
            print(x+1, self.board[x])
        self.scoreKeeper()
        print("Score: ", self.score)

        '''
        boardDisplay = turtle.Turtle()
        for x in range(4): # big boundry
            boardDisplay.forward(270)
            boardDisplay.right(90)
        for x in range(9): # grid squares
            for y in range(9):
                for z in range(4):
                    boardDisplay.forward(30)
                    boardDisplay.right(90)
                boardDisplay.forward(30)
            boardDisplay.back(270)
            boardDisplay.right(90)
            boardDisplay.forward(30)
            boardDisplay.left(90)
        '''

        for x in range(9): #block maker and color
            for y in range(9):
                boardVal = self.board[x][y]
                boardBlock = turtle.Turtle()
                boardBlock.speed(0)
                boardBlock.shape("square")
                if boardVal == 0:
                    boardBlock.color("black")
                elif boardVal > 1:
                    boardBlock.color("green")
                else:
                    boardBlock.color("yellow")
                boardBlock.shapesize(1.5, 1.5)  # sets length to 30 and width to 30
                boardBlock.penup()
                boardBlock.goto((30 * y) + 15, 0 - (x * 30) - 15)
        wn.update()



    def clearRow(self, rowNum):
        self.board[rowNum - 1] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def clearBoard(self):
        for x in range(9):
            self.board[x] = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def modifyBoard(self, rowNum, colNum, value):
        if self.bonusTag == 1:
            self.board[rowNum - 1][colNum - 1] += value
        else:
            x = self.board[rowNum - 1][colNum - 1]
            if x == 1 or x == 0:
                if x == value and value == 0:
                    print("Miss")
                self.board[rowNum - 1][colNum - 1] = value
            elif x >= 1 and value == 0:
                self.board[rowNum - 1][colNum - 1] -= 1

    def makeMove(self, rowNum, colNum, value):
        self.modifyBoard(rowNum, colNum, value)
        if rowNum < 9:
            self.modifyBoard(rowNum+1, colNum, value)
        if colNum < 9:
            self.modifyBoard(rowNum, colNum+1, value)
        if rowNum > 1:
            self.modifyBoard(rowNum-1, colNum, value)
        if colNum > 1:
            self.modifyBoard(rowNum, colNum-1, value)

    def scoreKeeper(self):
        count = 0
        countEnemy = 0
        for x in range(9):
            for y in range(9):
                value = self.board[x][y]
                if value >= 1:
                    count += 1
                elif value == 0:
                    countEnemy += 1
        self.score = count
        self.enemyScore = countEnemy


board1 = game()
rounds = 0
moves = 0
board1.printBoard()
# main game loop
while board1.enemyScore != 0:
    rounds += 1
    #wn.update() # updates screen whenever loop is parsed
    x1 = random.randrange(1, 10)
    y1 = random.randrange(1, 10)
    x2 = random.randrange(1, 10)
    y2 = random.randrange(1, 10)
    print("Computer chose coordinate", x1, ",", y1)
    board1.modifyBoard(x1, y1, 0)
    print("Computer chose coordinate", x2, ",", y2)
    board1.modifyBoard(x2, y2, 0)
    board1.printBoard()

    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
    board1.makeMove(row, col, 1)
    moves += 1

    if random.randrange(1,10) == random.randrange(1,10):
        board1.bonusTag = 1
        print("Bonus Move (increases value instead of making it 1, giving those coordinates a second life)")
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        board1.makeMove(row, col, 1)
        board1.bonusTag = 0
        moves += 1
    board1.printBoard()
    wn.clear()
    wn.tracer(0)


print("Game Finished!")
print(rounds, "rounds")
print(moves, "moves")
print(board1.score, "final score")

