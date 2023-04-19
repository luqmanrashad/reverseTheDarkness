# objective of game is to select location to drop a 1, causing adjacent numbers to become 1 as well
# create AI and difficulty range to make it challenging

import random
import turtle

wn = turtle.Screen()  # window screen using turtle
wn.title("reverseTheDarkness")  # title of window
wn.bgcolor("white")  # background color
wn.setup(800, 600)  # screen size
wn.tracer(0)  # lets us speed up games and doesn't let screen update

font = ("Arial", 14, "bold")
colors = ["black", "yellow", "green", "blue", "purple", "pink", "red", "orange", "white"]


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
            print(x + 1, self.board[x])
        self.scoreKeeper()
        print("Score: ", self.score)

        for x in range(9):  # block maker and color
            for y in range(9):
                boardVal = self.board[x][y]
                boardBlock = turtle.Turtle()
                boardBlock.speed(0)
                boardBlock.shape("square")
                if boardVal <= 7:
                    boardBlock.color(colors[boardVal])  # sets color based on colors array and board value
                else:
                    boardBlock.color(colors[8])  # sets color to white to represent a high value
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
                else:
                    print("Hit")
                self.board[rowNum - 1][colNum - 1] = value
            elif x >= 1 and value == 0:
                self.board[rowNum - 1][colNum - 1] -= 1
                print("Hit")

    def makeMove(self, rowNum, colNum, value):
        self.modifyBoard(rowNum, colNum, value)
        if rowNum < 9:
            self.modifyBoard(rowNum + 1, colNum, value)
        if colNum < 9:
            self.modifyBoard(rowNum, colNum + 1, value)
        if rowNum > 1:
            self.modifyBoard(rowNum - 1, colNum, value)
        if colNum > 1:
            self.modifyBoard(rowNum, colNum - 1, value)

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

    def missingBlocks(self):
        for x in range(9):
            for y in range(9):
                value = self.board[x][y]
                if value == 0:
                    return [x + 1, y + 1]

        return [random.randrange(1, 10), random.randrange(1, 10)]

    def maxMissingBlocks(self):
        listMissing = []
        for x in range(9):
            for y in range(9):
                value = self.board[x][y]
                countMissing = 1  # priority counter that gets inverse in sort key function
                # checks if selected block is 0 to add priority
                if value == 0:
                    countMissing += 1
                # check and count missing adjacent blocks. if adjacent blocks are 0, add priority
                if x > 0:
                    if self.board[x - 1][y] == 0:
                        countMissing += 1
                if y > 0:
                    if self.board[x][y - 1] == 0:
                        countMissing += 1
                if y < 8:
                    if self.board[x][y + 1] == 0:
                        countMissing += 1
                if x < 8:
                    if self.board[x + 1][y] == 0:
                        countMissing += 1
                listMissing.append([x + 1, y + 1, countMissing])

        # function takes in the array n from listMissing and returns the inverse of countMissing to sort list based on best choices for next move
        # n[2] is the count missing variable
        def sortMaxMissing(n):
            return 1 / n[2]

        # sort list Missing and then make a copy that has the x and y indices of the subarray returned
        listMissing.sort(key=sortMaxMissing)
        newList = listMissing.copy()
        print("List: ", newList)
        return (newList[0][0], newList[0][1])


board1 = game()
rounds = 0
moves = 0
board1.printBoard()
# main game loop
# runs till all blocks have a value of 1
# use smart input to choose next move and bonus move
# bonus move will add an extra +1 to the block
while board1.enemyScore != 0:
    rounds += 1
    # wn.update() # updates screen whenever loop is parsed, moved to somewhere more useful
    x1 = random.randrange(1, 10)
    y1 = random.randrange(1, 10)
    x2 = random.randrange(1, 10)
    y2 = random.randrange(1, 10)
    print("Computer chose coordinate", x1, ",", y1)
    board1.modifyBoard(x1, y1, 0)
    print("Computer chose coordinate", x2, ",", y2)
    board1.modifyBoard(x2, y2, 0)
    board1.printBoard()

    smartMissing = board1.maxMissingBlocks()
    board1.makeMove(smartMissing[0], smartMissing[1], 1)
    moves += 1

    if random.randrange(1, 10) == random.randrange(1, 10):
        board1.bonusTag = 1
        print("Bonus Move (increases value instead of making it 1, giving those coordinates a second life)")
        smartMissing = board1.maxMissingBlocks()
        board1.makeMove(smartMissing[0], smartMissing[1], 1)
        board1.bonusTag = 0
        moves += 1
    board1.printBoard()
    # wait = input()
    wn.clear()
    wn.tracer(0)

# end game results and summary
board1.printBoard()
print("Game Finished!")
print(rounds, "rounds")
print(moves - (moves - rounds), "moves and", moves - rounds, "bonus moves")
print(board1.score, "final score")
wait = input()