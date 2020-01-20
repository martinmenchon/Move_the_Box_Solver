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
    #cv.imwrite('images/res.png',img_rgb)

    return board
