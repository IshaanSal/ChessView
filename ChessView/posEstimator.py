import cv2
import InputValues
import coordDiv
import boardDiv
import pieceMatch
from pieceMatch import posX
from pieceMatch import posY
from pieceMatch import pieceNames
from InputValues import ParentImage

board = cv2.imread(ParentImage)

heightDiv = (board.shape[0])//8
widthDiv = (board.shape[1])//8
w = widthDiv
h = heightDiv
a = widthDiv//2
b = heightDiv//2

boardArrX = []
boardArrY = []
newPosX = []
newPosY = []

posArr = {'H1': [a,b], 'H2': [a+w,b], 'H3': [a+(2*w),b], 'H4': [a+(3*w),b],
          'H5': [a+(4*w),b], 'H6': [a+(5*w),b], 'H7': [a+(6*w),b], 'H8': [a+(7*w),b],
          'G1': [a,b+h], 'G2': [a+w,b+h], 'G3': [a+(2*w),b+h], 'G4': [a+(3*w),b+h],
          'G5': [a+(4*w),b+h], 'G6': [a+(5*w),b+h], 'G7': [a+(6*w),b+h], 'G8': [a+(7*w),b+h],
          'F1': [a,b+(2*h)], 'F2': [a+w,b+(2*h)], 'F3': [a+(2*w),b+(2*h)], 'F4': [a+(3*w),b+(2*h)],
          'F5': [a+(4*w),b+(2*h)], 'F6': [a+(5*w),b+(2*h)], 'F7': [a+(6*w),b+(2*h)], 'F8': [a+(7*w),b+(2*h)],
          'E1': [a,b+(3*h)], 'E2': [a+w,b+(3*h)], 'E3': [a+(2*w),b+(3*h)], 'E4': [a+(3*w),b+(3*h)],
          'E5': [a+(4*w),b+(3*h)], 'E6': [a+(5*w),b+(3*h)], 'E7': [a+(6*w),b+(3*h)], 'E8': [a+(7*w),b+(3*h)],
          'D1': [a,b+(4*h)], 'D2': [a+w,b+(4*h)], 'D3': [a+(2*w),b+(4*h)], 'D4': [a+(3*w),b+(4*h)],
          'D5': [a+(4*w),b+(4*h)], 'D6': [a+(5*w),b+(4*h)], 'D7': [a+(6*w),b+(4*h)], 'D8': [a+(7*w),b+(4*h)],
          'C1': [a,b+(5*h)], 'C2': [a+w,b+(5*h)], 'C3': [a+(2*w),b+(5*h)], 'C4': [a+(3*w),b+(5*h)],
          'C5': [a+(4*w),b+(5*h)], 'C6': [a+(5*w),b+(5*h)], 'C7': [a+(6*w),b+(5*h)], 'C8': [a+(7*w),b+(5*h)],
          'B1': [a,b+(6*h)], 'B2': [a+w,b+(6*h)], 'B3': [a+(2*w),b+(6*h)], 'B4': [a+(3*w),b+(6*h)],
          'B5': [a+(4*w),b+(6*h)], 'B6': [a+(5*w),b+(6*h)], 'B7': [a+(6*w),b+(6*h)], 'B8': [a+(7*w),b+(6*h)],
          'A1': [a,b+(7*h)], 'A2': [a+w,b+(7*h)], 'A3': [a+(2*w),b+(7*h)], 'A4': [a+(3*w),b+(7*h)],
          'A5': [a+(4*w),b+(7*h)], 'A6': [a+(5*w),b+(7*h)], 'A7': [a+(6*w),b+(7*h)], 'A8': [a+(7*w),b+(7*h)]}

'''
print(posArr)
print(posX)
print(posY)
'''

boardPosArr = []    #goes in order from WR1 to BR2
for i in range(32):
    for square in posArr:
        cond1 = posArr[square][0]
        cond2 = posArr[square][1]
        if (cond1-20 < posX[i] < cond1+20) and (cond2-20 < posY[i] < cond2+20):
            boardPosArr.append(square)

#print(boardPosArr)
print()

p1 = 0
for val in boardPosArr:
    print(pieceNames[p1] + "=" + val)
    p1 += 1

'''
cv2.imshow('Frame', board)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''