import cv2 as cv
import numpy as np
import constants
from Board import Board

def buildBoard(level):
    # Creates a board
    # h = 10 #row
    # w = 7 #col
    board = Board(10,7)
    ##############################
    #Boxes
    boxes = [[constants.RED,"red_box.png"],[constants.GREEN,'green_box.png'],[constants.YELLOW,'yellow_box.png'],[constants.BLUE,'blue_box.png'],[constants.BROWN,'brown_box.png'],[constants.BLACK,'black_box.png']]

    img_rgb = cv.imread('images/levels/'+level)
    img_rgb = img_rgb[177:1727, 0:1080]
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    for box in boxes:
        template = cv.imread('images/boxes/'+box[1],0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            #usar el punto del medio del rect y ver donde cae
            x = int(pt[1] + h / 2)
            x = int(x / 155)
            y = int(pt[0] + w/2)
            y = int(y / 155)

            board.insert_box([x,y], box[0])
            #cv.circle(img_rgb, (int(pt[0] + w/2), int(pt[1] + h/2)), 25, (0,0,255), thickness=2, lineType=8, shift=0)
            #cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    #board.print_board()
    cv.imwrite('images/res.png',img_rgb)

    return board


def find_color(box):
    # Boxes
    boxes = [[constants.RED, "red_box.png"], [constants.GREEN, 'green_box.png'], [constants.YELLOW, 'yellow_box.png'],
             [constants.BLUE, 'blue_box.png'], [constants.BROWN, 'brown_box.png'], [constants.BLACK, 'black_box.png']]
    box_name = ""
    for element in boxes:
        if box == element[0]:
            box_name = element[1]
    return box_name

def draw_board(board,step, move):
    img_rgb = cv.imread('images/backgrounds/miami.png')
    img_rgb = img_rgb[177:1727, 0:1080]

    list_of_boxes = board.get_boxes()
    for box in list_of_boxes:
        color = board.get_color(box)
        box_name = find_color(color)

        x = box[0] * 155
        y = box[1] * 155
        template = cv.imread('images/boxes/' + box_name)
        img_rgb[x:x + 155, y:y + 155] = template

    y1 = move[0][0] * 155
    x1 = move[0][1] * 155

    y2 = move[1][0] * 155
    x2 = move[1][1] * 155

    cv.rectangle(img_rgb, (x1, y1), (x1 + 155, y1 + 155), (0, 0, 255), 2)
    cv.rectangle(img_rgb, (x2, y2), (x2 + 155, y2 + 155), (0, 0, 255), 2)

    cv.imwrite('images/res_'+str(step)+'.png', img_rgb)