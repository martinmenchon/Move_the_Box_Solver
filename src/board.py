import pandas as pd
import constants


class Board:
    def __init__(self, *args):
        # when 1 argument is passed
        if len(args) == 1:
            df = pd.read_csv(args[0], header=None, sep="\t")
            matrix = df.to_numpy()
            self.h = matrix.shape[0]
            self.w = matrix.shape[1]
            self.matrix = matrix.tolist()
            self.max_moves = int(args[0].split("-")[-1].split(".")[0])

        # when 2 arguments are passed
        elif len(args) == 3:
            self.h = args[0]
            self.w = args[1]
            self.matrix = [[0 for x in range(self.w)] for y in range(self.h)]
            self.max_moves = args[2]

    def insert_box(self, pos, color):
        self.matrix[pos[0]][pos[1]] = color

    def get_color(self,pos):
        return self.matrix[pos[0]][pos[1]]

    def get_boxes(self):
        list = []
        for x,row in enumerate(self.matrix):
            for y,element in enumerate(row):
                if element != constants.EMPTY:
                    list.append([x, y])
        return list

    def get_possible_moves(self, pos):
        possible_moves = []
        # up
        if pos[0] - 1 >= 0:
            possible_moves.append([pos[0]-1, pos[1]])
        # down
        if pos[0] + 1 < self.h:
            possible_moves.append([pos[0]+1, pos[1]])
        # left
        if pos[1] - 1 >= 0:
            possible_moves.append([pos[0], pos[1]-1])
        # right
        if pos[1] + 1 < self.w:
            possible_moves.append([pos[0], pos[1]+1])
        return possible_moves

    def print_board(self):
        for row in self.matrix:
            for element in row:
                if element is constants.GREEN:
                    print('\033[92m' + str(element) + '\033[0m', end='')
                elif element is constants.BLUE:
                    print('\033[34m' + str(element) + '\033[0m', end='')
                elif element is constants.RED:
                    print('\033[31m' + str(element) + '\033[0m', end='')
                elif element is constants.YELLOW:
                    print('\033[93m' + str(element) + '\033[0m', end='')
                elif element is constants.BROWN:
                    print('\033[38;5;94m' + str(element) + '\033[0m', end='')
                else:
                    print(element, end='')
            print()

    def __check_down(self, pos): #acomodar solo mandar pos[1]
        index=0
        l1=[]
        while index < self.h:
            if self.matrix[index][pos[1]] == constants.EMPTY:
                l1.insert(0, constants.EMPTY)
            else:
                l1.append(self.matrix[index][pos[1]])
            index+=1

        index=0
        while index < self.h:
            self.matrix[index][pos[1]] = l1[index]
            index+=1

    def __check_row(self, row, to_delete):
        lastNumber = constants.EMPTY
        init = 0
        list_to_review=[]
        while init < self.w:
            if self.matrix[row][init] != constants.EMPTY:
                if self.matrix[row][init] == lastNumber:
                    list_to_review.append([row,init]) #Guardar la pos en realidad
                else: #Si encuentra algo que no sea un EMPTY lo tiene que guardar entremedio
                    if len(list_to_review) >= 3:
                        for pos in list_to_review:
                            to_delete.append(pos)
                    list_to_review.clear()
                    list_to_review.append([row, init]) #Guardar la pos del nuevo nro
                    lastNumber = self.matrix[row][init]      
            else: #Si encuentra un EMPTY entremedio
                    if len(list_to_review) >= 3:
                        for pos in list_to_review:
                            to_delete.append(pos)
                    lastNumber = self.matrix[row][init]
                    list_to_review.clear()
            init+=1
        if len(list_to_review) >= 3:#porque llega al final
            for pos in list_to_review:
                if pos not in to_delete:
                    to_delete.append(pos)

    def __check_col(self, col, to_delete):
        lastNumber = constants.EMPTY
        init = 0
        list_to_review=[]
        while init < self.h:
            if self.matrix[init][col] != constants.EMPTY:
                if self.matrix[init][col] == lastNumber:
                    list_to_review.append([init, col]) #Guardar la pos en realidad
                else: #Si encuentra algo que no sea un EMPTY lo tiene que guardar entremedio
                    if len(list_to_review) >= 3:
                        for pos in list_to_review:
                            to_delete.append(pos)
                    list_to_review.clear()
                    list_to_review.append([init, col]) #Guardar la pos del nuevo nro
                    lastNumber = self.matrix[init][col]      
            else: #Si encuentra un EMPTY entremedio
                    if len(list_to_review) >= 3:
                        for pos in list_to_review:
                            to_delete.append(pos)
                    lastNumber = self.matrix[init][col]
                    list_to_review.clear()
            init+=1
        if len(list_to_review) >= 3:#porque llega al final
            for pos in list_to_review:
                if pos not in to_delete:
                    to_delete.append(pos)

    def execute_move(self,before,after):
        aux = self.matrix[before[0]][before[1]]
        self.matrix[before[0]][before[1]] = self.matrix[after[0]][after[1]]
        self.matrix[after[0]][after[1]] = aux
        self.__check_down(before)#mueve hacia abajo
        self.__check_down(after)#mueve hacia abajo
        #Puede ir en procedimiento chequear tablero
        repeat = True
        while repeat:
            to_delete=[]
            for row in range(0,self.h):
                self.__check_row(row, to_delete)
            for col in range(0, self.w):
                self.__check_col(col, to_delete)
            for pos in to_delete:
                self.matrix[pos[0]][pos[1]] = 0
            for pos in to_delete:
                self.__check_down([pos[0], pos[1]])# Tiene que ser en un for separado sino mueve mal
            if len(to_delete) == 0:
                repeat = False

    def board_to_csv(self):
        df = pd.DataFrame(self.matrix)
        return df

    def has_a_possible_solution(self):
        dict_colors = {}
        for x,row in enumerate(self.matrix):
            for y,element in enumerate(row):
                if element != 0:
                    if element not in dict_colors:
                        dict_colors[element] = 1
                    else:
                        dict_colors[element] += 1
        for cant_color in dict_colors.values():
            if cant_color <= 2:
                return False
        return True