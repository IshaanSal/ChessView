import cv2
from InputValues import ParentImage

pieceNames = ['BR1', 'BN1', 'BB1', 'BK', 'BQ', 'BB2', 'BN2', 'BR2',
            'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8',
            'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6', 'WP7', 'WP8',
            'WR1', 'WN1', 'WB1', 'WK', 'WQ', 'WB2', 'WN2', 'WR2']
posX = []
posY = []

og = cv2.imread(ParentImage)
img = cv2.cvtColor(og, cv2.COLOR_BGR2GRAY)
c = 0

while c < len(pieceNames):
    template = cv2.imread('piecePics/' + pieceNames[c] + '.png', 0)
    h, w, = template.shape

    methods = [cv2.TM_SQDIFF]

    for method in methods:
        img2 = img.copy()

        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc

        bottom_right = (location[0] + w, location[1] + h)
        heightDiv = (img2.shape[0]) // 8
        widthDiv = (img2.shape[1]) // 8
        newX = location[0] + int(0.5 * widthDiv)
        newY = location[1] + int(0.5 * heightDiv)
        posX.append(newX)
        posY.append(newY)
        print(pieceNames[c] + " = " + str(posX[c]) + "," + str(posY[c]))

        '''
        img2 = cv2.circle(img2, (posX[c],posY[c]), 10, 255, 5)
        cv2.imshow('Frame', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''

    c += 1

'''
cv2.imshow('Frame', og)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''