import copy
from Board import Board

###Constants###
EMPTY = 0
#Boxes
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4

##############################
#Game
#Depends on the scenary
MAX_MOVES=3
number_of_moves = 0

# Creates a board
h = 5 #filas
w = 7 #columnas
board = Board(h,w)

#notacion fila columna, x,y
board.insertBox([4,1],GREEN)
board.insertBox([4,2],GREEN)
board.insertBox([4,3],BLUE)
board.insertBox([4,4],GREEN)
board.insertBox([4,5],BLUE)
board.insertBox([4,6],BLUE)

board.insertBox([3,1],BLUE)
board.insertBox([3,2],RED)
board.insertBox([3,3],GREEN)
board.insertBox([3,4],RED)
board.insertBox([3,5],RED)

board.insertBox([2,2],BLUE)
board.insertBox([2,3],GREEN)
board.insertBox([2,4],YELLOW)
board.insertBox([2,5],GREEN)

board.insertBox([1,3],GREEN)
board.insertBox([1,4],GREEN)

board.insertBox([0,3],YELLOW)
##############################

board.print_board()
listOfBoxes = board.getBoxes()

print()
possible_moves = board.get_possible_moves([4,1])
print("possible moves", possible_moves)

board.execute_move([4,4],[4,3])
print()
board.print_board()

#if len(list_of_GetBoxes) == 0 terminó
#copy va a servir para el backtracking
