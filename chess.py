import numpy as np


# define Chess
class Chess:

    # Constructor
    def __init__(self, board):
        # default dictionary to store graph
        self.chessboard = np.zeros((8, 8), dtype=int)
        self.board = []
        self.encodeArray(board)

    def encodeArray(self, board):
        for i in range(8):
            for j in range(8):
                if board[j][i] == 'Q':
                    break
            self.board.append(j)

    # Calculate estimated cost value
    def heuristicCalculate(self, collumn, value):
        count = 0
        board = self.board.copy()
        board[collumn] = value
        for i in range(8):
            for j in range(i + 1, 8):
                if board[i] == board[j] or board[i] == board[j] - (j - i) or board[i] == board[j] + (j - i):
                    count += 1
        return count

    def calculateAllHeuristic(self):
        for i in range(8):
            for j in range(8):
                if self.board[i] != j:
                    self.chessboard[j][i] = self.heuristicCalculate(i, j)
                else:
                    self.chessboard[j][i] = -1


# Create a chess given in the above diagram
# Read from input file
with open('input.txt') as f:
    array = [[x for x in line.split()] for line in f]

chess = Chess(board=array)

chess.calculateAllHeuristic()

print(chess.chessboard)

# Write into output file
strResult = ""
f = open("output.txt", "a")
for line in chess.chessboard:
    for elem in line:
        if elem == -1:
            strResult += "Q" + " "
        else:
            strResult += str(elem) + " "
    strResult += '\n'

f.write(strResult)
f.close()


