import copy

def bfs(game_states):
    visited = []
    while len(game_states) != 0:
        state = game_states.pop(0)
        actual_board = state["board"]
        steps_list = state["steps"]
        visited.append(actual_board)
        list_of_boxes = actual_board.get_boxes()
        if len(list_of_boxes) == 0 and len(steps_list) <= actual_board.max_moves:
            return steps_list
        else:
            if len(steps_list) < actual_board.max_moves:
                for box in list_of_boxes:
                    possible_moves = actual_board.get_possible_moves(box)
                    for move in possible_moves:
                        if actual_board.get_color(box) != actual_board.get_color(move): #Bound
                            new_board = copy.deepcopy(actual_board)
                            new_board.execute_move(box, move)
                            if new_board not in visited: #otra posible Bound es fijarse que haya colores 0 o >=3 HACER
                                new_steps_list = copy.deepcopy(steps_list)
                                new_steps_list.append([box, move])
                                game_states.append({"board": new_board, "steps": new_steps_list})
