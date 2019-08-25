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
max_moves=3
h = 5 #filas
w = 7 #columnas
Matrix = [[0 for x in range(w)] for y in range(h)]
#notacion fila columna, y,x
Matrix[4][1]= GREEN
Matrix[4][2]= GREEN
Matrix[4][3]= BLUE
Matrix[4][4]= GREEN
Matrix[4][5]= BLUE
Matrix[4][6]= BLUE

Matrix[3][1]= BLUE
Matrix[3][2]= RED
Matrix[3][3]= YELLOW
Matrix[3][4]= RED
Matrix[3][5]= RED

Matrix[2][2]= BLUE
Matrix[2][3]= BLUE
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

def __check_down(pos):
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

listOfBoxes = __getBoxes()
#print(listOfBoxes)

__print_board(Matrix)
print()
possible_moves = __get_possible_moves([4,1])
print(possible_moves)



# if is a valid move()
#     executeMove(antes, despues) => while baja en caso de que quede un 0 y arriba cosas y desp y chequea arriba abajo y a los costados y vuelve a chequear los 0!


def __detectH(row):
    #deleteList=[[posx,posy],[posx,posy],[posx,posy]]
    if num == 0:
        #check size
        deleteList.clear()




    for i in range(1,w):
        print(i)

    if len(listABorrar)>=3: #lista a borrar tiene las pos a borrar
        #borrar



aRevisar=[]
print()
def __execute_move(before,after):
    value = Matrix[after[0]][after[1]]
    aux = Matrix[before[0]][before[1]]
    Matrix[before[0]][before[1]] = Matrix[after[0]][after[1]]
    Matrix[after[0]][after[1]] = aux
    __check_down(before)
    __check_down(after)
    #A revisar
    #arriba abajo
    #



##############################
__execute_move([4,4],[4,3])
__print_board(Matrix)
#__detectH(0)


#__getBoxes()

#if len(list_of_GetBoxes) == 0 terminó
