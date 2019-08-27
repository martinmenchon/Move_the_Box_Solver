import copy

EMPTY = 0
#Boxes
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4

####################################################################
# #Depends on the scenary
# Creates a board
MAX_MOVES=3
h = 5 #filas
w = 7 #columnas
Matrix = [[0 for x in range(w)] for y in range(h)]

#notacion fila columna, x,y
Matrix[4][1]= GREEN
Matrix[4][2]= GREEN
Matrix[4][3]= BLUE
Matrix[4][4]= GREEN
Matrix[4][5]= BLUE
Matrix[4][6]= BLUE

Matrix[3][1]= BLUE
Matrix[3][2]= RED
Matrix[3][3]= GREEN
Matrix[3][4]= RED
Matrix[3][5]= RED

Matrix[2][2]= BLUE
Matrix[2][3]= GREEN
Matrix[2][4]= YELLOW
Matrix[2][5]= GREEN

Matrix[1][3]= GREEN
Matrix[1][4]= GREEN

Matrix[0][3]= YELLOW
###################################################################

#Resolucion
def __getBoxes():
    list= []
    for x,row in enumerate(Matrix):
        for y,element in enumerate(row):
            if element != 0:
                list.append([x, y])
    return list

def __print_board(board):
    for row in board:
        for element in row:
            if element is GREEN:
                print('\033[92m' + str(element) + '\033[0m', end='')
            elif element is BLUE:
                print('\033[34m' + str(element) + '\033[0m', end='')
            elif element is RED:
                print('\033[31m' + str(element) + '\033[0m', end='')
            elif element is YELLOW:
                print('\033[93m' + str(element) + '\033[0m', end='')
            else:
                print(element, end='')
        print()

def __get_possible_moves(pos):
    possible_moves = []
    # up
    if pos[0] - 1 >= 0:
        possible_moves.append([pos[0]-1, pos[1]])
    # down
    if pos[0] + 1 < h:
        print(pos)
        possible_moves.append([pos[0]+1, pos[1]])
    # left
    if pos[1] - 1 >= 0:
        possible_moves.append([pos[0], pos[1]-1])
    # right
    if pos[1] + 1 < w:
        possible_moves.append([pos[0], pos[1]+1])

    return possible_moves

def __check_down(pos):#acomodar solo mandar pos[1]
    index=0
    l1=[]
    while index < h:
        if Matrix[index][pos[1]] == 0:
            l1.insert(0,0)
        else:
            l1.append(Matrix[index][pos[1]])
        index+=1

    index=0
    while index < h:
        Matrix[index][pos[1]] = l1[index]
        index+=1

def __check_row(row,a_eliminar):
    lastNumber = 0
    init = 0
    list_a_revisar=[]
    while init < w:
        if Matrix[row][init] !=0:
            if Matrix[row][init] == lastNumber:
                list_a_revisar.append([row,init]) #Guardar la pos en realidad
            else: #Si encuentra algo que no sea un 0 lo tiene que guardar entremedio
                if len(list_a_revisar) >= 3:
                    for pos in list_a_revisar:
                        a_eliminar.append(pos)
                list_a_revisar.clear()
                list_a_revisar.append([row, init]) #Guardar la pos del nuevo nro
                lastNumber = Matrix[row][init]      
        else: #Si encuentra un 0 entremedio
                if len(list_a_revisar) >= 3:
                    for pos in list_a_revisar:
                        a_eliminar.append(pos)
                lastNumber = Matrix[row][init]
                list_a_revisar.clear()
        init+=1
    if len(list_a_revisar) >= 3:#porque llega al final
        for pos in list_a_revisar:
            if pos not in a_eliminar:
                a_eliminar.append(pos)

def __check_col(col,a_eliminar):
    lastNumber = 0
    init = 0
    list_a_revisar=[]
    while init < h:
        if Matrix[init][col] !=0:
            if Matrix[init][col] == lastNumber:
                list_a_revisar.append([init, col]) #Guardar la pos en realidad
            else: #Si encuentra algo que no sea un 0 lo tiene que guardar entremedio
                if len(list_a_revisar) >= 3:
                    for pos in list_a_revisar:
                        a_eliminar.append(pos)
                list_a_revisar.clear()
                list_a_revisar.append([init, col]) #Guardar la pos del nuevo nro
                lastNumber = Matrix[init][col]      
        else: #Si encuentra un 0 entremedio
                if len(list_a_revisar) >= 3:
                    for pos in list_a_revisar:
                        a_eliminar.append(pos)
                lastNumber = Matrix[init][col]
                list_a_revisar.clear()
        init+=1
    if len(list_a_revisar) >= 3:#porque llega al final
        for pos in list_a_revisar:
            if pos not in a_eliminar:
                a_eliminar.append(pos)

def __execute_move(before,after):
    global number_of_moves
    number_of_moves +=1
    aux = Matrix[before[0]][before[1]]
    Matrix[before[0]][before[1]] = Matrix[after[0]][after[1]]
    Matrix[after[0]][after[1]] = aux
    __check_down(before)#mueve hacia abajo
    __check_down(after)#mueve hacia abajo
    #Puede ir en procedimiento chequear tablero
    repetir = True
    while repetir:
        a_eliminar=[]
        for row in range(0,h):
            __check_row(row,a_eliminar)
        for col in range(0,w):
            __check_col(col,a_eliminar)
        for pos in a_eliminar:
            Matrix[pos[0]][pos[1]] = 0
        for pos in a_eliminar:
            __check_down([pos[0],pos[1]])# Tiene que ser en un for separado sino mueve mal
        if len(a_eliminar) == 0:
            repetir = False



#Game
number_of_moves = 0
listOfBoxes = __getBoxes()

__print_board(Matrix)
print()
possible_moves = __get_possible_moves([4,1])
print("possible moves", possible_moves)

__execute_move([4,4],[4,3])
print()
__print_board(Matrix)

#if len(list_of_GetBoxes) == 0 terminó
