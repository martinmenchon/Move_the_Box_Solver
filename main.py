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
h = 6 #row
w = 7 #col
board = Board(h,w)

# Row x, Col y
board.insert_box([5,2],GREEN)
board.insert_box([4,2],GREEN)
board.insert_box([3,2],RED)
board.insert_box([2,2],GREEN)
board.insert_box([1,2],GREEN)

board.insert_box([5,4],RED)
board.insert_box([4,4],RED)
board.insert_box([3,4],GREEN)
board.insert_box([2,4],RED)
board.insert_box([1,4],RED)
board.insert_box([0,4],GREEN)
##############################

board.print_board()
print()

def bfs(game_states):
    visited = []
    while len(game_states) != 0:
        state = game_states.pop(0)
        actual_board = state[0]
        steps_list = state[1]
        visited.append(actual_board)
        list_of_boxes = actual_board.get_boxes()
        if len(list_of_boxes) == 0 and len(steps_list) <= MAX_MOVES:
            return steps_list
        else:
            if len(steps_list) < MAX_MOVES:
                for box in list_of_boxes:
                    possible_moves = actual_board.get_possible_moves(box)
                    for move in possible_moves:
                        if actual_board.get_color(box) != actual_board.get_color(move): #Poda
                            new_board = copy.deepcopy(actual_board)
                            new_board.execute_move(box,move)
                            if new_board not in visited: #otra poda es fijarse que haya colores de todo o 0 o >=3 HACER
                                new_steps_list = copy.deepcopy(steps_list)
                                new_steps_list.append([box,move])
                                game_states.append([new_board,new_steps_list])

game_states=[]
game_states.append([board,[]])
moves_list = []

print("Inicia BFS:\n")
moves_list = bfs(game_states)
if len(moves_list) > 0:
    print("Se encontró solucion:")
    for move in moves_list:
        print(move)
else:
    print("No se encontró solución")