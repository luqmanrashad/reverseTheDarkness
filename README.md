The program is a game called reverseTheDarkness. The objective is to select a location to flip, which will cause adjacent boxes to flip as well. The game has an AI and a difficulty range to make it challenging. 

# Feel free to download and run these python files individually and check out the differences. Below is an explanation of the program and some statistics

The program uses the turtle module to create a graphical interface for the game. The game class has various methods to modify the game board and keep track of the score. The game board is a 9x9 grid with each cell with an initial number of 0 and black color, but as you flip them, this makes the box yellow and increases the number to 1. Bonus moves are also possible with some low chance so as to give the user or program a slight extra chance of winning. Bonus moves also add to the score instead of converting it to 1, having a special effect of increasing the score to even more than 1.

UserInput wins in an average of 150 moves. Requires user brainpower

RandomIput keeps using random input for an infinite amount of time and never wins. Automatic computer selections

RandomSmart wins usually between 300 and 4,000 moves, with the fastest being 277 moves. Automatic computer selections based on location of black boxes

SmartInput wins usually between 60 and 200 moves, with the fastest being 38 moves. Automatic computer selections prioritized to make smarter choices that flips more boxes

AIInput: The AI Portion is still being worked on, but as of right now, a minimax algorithm seems like a good way to proceed. For now, it is just a smart flipper
