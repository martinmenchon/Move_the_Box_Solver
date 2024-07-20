import copy
import UI
from board import Board
from bfs import bfs
import logging

#TODO pydoc
#TODO docker
#TODO pre-commit
#TODO add logs

if __name__ == "__main__":
    #Game
    board = UI.buildBoard(level='level_1.png', max_moves=3)
    board.print_board()

    #or try just with the .csv data
    # board = Board("data/levels/North_America/Miami/level_22-3.csv")
    # board.print_board()

    print()
    game_states = []
    game_states.append({"board":board, "steps": []})

    print("Start BFS:\n")
    moves_list = bfs(game_states)
    if len(moves_list) > 0:
        print("Solution found:")
        for move in moves_list:
            print(move)
    else:
        print("No solution was found")

    for i, move in enumerate(moves_list):
        UI.draw_board(board, i, move)
        board.execute_move(move[0], move[1])

#change name to step_list #box, move