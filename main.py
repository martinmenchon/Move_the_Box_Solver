import copy
from Board import Board
import UI

#Game
MAX_MOVES = 3 #Depends on the level
board = UI.buildBoard('level_1.png')

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
                            if new_board not in visited: #otra poda es fijarse que haya colores 0 o >=3 HACER
                                new_steps_list = copy.deepcopy(steps_list)
                                new_steps_list.append([box, move])
                                game_states.append([new_board, new_steps_list])

copy_board = copy.deepcopy(board)
game_states = []
game_states.append([board, []])

print("Inicia BFS:\n")
moves_list = bfs(game_states)
if len(moves_list) > 0:
    print("Se encontro solucion:")
    for move in moves_list:
        print(move)
else:
    print("No se encontro solucion")


for i, move in enumerate(moves_list):
    UI.draw_board(copy_board, i, move)
    copy_board.execute_move(move[0], move[1])
