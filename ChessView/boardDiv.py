import cv2
import numpy as np
import coordDiv
from PIL import Image
from InputValues import OriginalSetup

board: object = cv2.imread(OriginalSetup)
#print(board.shape)

heightDiv = (board.shape[0])//8
widthDiv = (board.shape[1])//8

c1 = coordDiv.coords(widthDiv, heightDiv)
c1.topLCoords(widthDiv,heightDiv)
c1.bottomRCoords(widthDiv,heightDiv)

pieceNames = ['BR1', 'BN1', 'BB1', 'BK', 'BQ', 'BB2', 'BN2', 'BR2',
            'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8',
            'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6', 'WP7', 'WP8',
            'WR1', 'WN1', 'WB1', 'WK', 'WQ', 'WB2', 'WN2', 'WR2']

by1, by2, ax1, ax2 = 1,1,0,0
arrC = 0
t1 = 0
for i in range(4):
    for j in range(8):
        if by1<16 and by2<16 and ax1<16 and ax2<16:
            b1 = coordDiv.topL[t1][by1]
            print(b1)
            b2 = coordDiv.bottomR[t1][by2]
            print(b2)
            a1 = coordDiv.topL[t1][ax1]
            print(a1)
            a2 = coordDiv.bottomR[t1][ax2]
            print(a2)

        v = board[b1:b2, a1:a2]
        array = np.array(v, dtype=np.uint8)
        new_img = Image.fromarray(array)
        new_img.save('piecePics/' + pieceNames[arrC] + '.png')

        by1 += 2
        by2 += 2
        ax1 += 2
        ax2 += 2
        arrC += 1
    t1 += 1
    by1, by2, ax1, ax2 = 1, 1, 0, 0

'''
cv2.imshow('Board', board)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''