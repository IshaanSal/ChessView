import cv2

class dB:
    board = cv2.imread('chessPics/chessBoard.png')
    board = cv2.resize(board, (0,0), fx=0.5, fy=0.5)
    print(board.shape) #height, width, channels

    heightDiv = (board.shape[0])//8
    widthDiv = (board.shape[1])//8

    font = cv2.FONT_HERSHEY_SIMPLEX

    BlackRow1 = ['BR1', 'BN1', 'BB1', 'BK', 'BQ', 'BB2', 'BN2', 'BR2']
    BlackRow2 = ['BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BP8']
    WhiteRow1 = ['WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6', 'WP7', 'WP8']
    WhiteRow2 = ['WR1', 'WN1', 'WB1', 'WK', 'WQ', 'WB2', 'WN2', 'WR2']
    c1 = 0
    for i in BlackRow1:
        board = cv2.putText(board, BlackRow1[c1], ((widthDiv//4)+c1*int(widthDiv),heightDiv), font, 0.5, (0,0,0), 1, cv2.LINE_AA)
        c1 += 1

    c2 = 0
    for i in BlackRow2:
        board = cv2.putText(board, BlackRow2[c2], ((widthDiv//4)+c2*int(widthDiv),2*int(heightDiv)), font, 0.5, (0,0,0), 1, cv2.LINE_AA)
        c2 += 1

    c3 = 0
    for i in WhiteRow1:
        board = cv2.putText(board, WhiteRow1[c3], ((widthDiv//4)+c3*int(widthDiv),7*int(heightDiv)), font, 0.5, (0,0,0), 1, cv2.LINE_AA)
        c3 += 1

    c4 = 0
    for i in WhiteRow2:
        board = cv2.putText(board, WhiteRow2[c4], ((widthDiv//4)+c4*int(widthDiv),8*int(heightDiv)), font, 0.5, (0,0,0), 1, cv2.LINE_AA)
        c4 += 1

    cv2.imshow('Board', board)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #make separate class storing width and height coefficients for every piece