topL = []
bottomR = []

Arow1xy = []
Arow2xy = []
Arow7xy = []
Arow8xy = []

Brow1xy = []
Brow2xy = []
Brow7xy = []
Brow8xy = []


class coords():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def topLCoords(self, x, y):
        for i in range(8):
            val = i * x
            Arow1xy.append(val)
            Arow1xy.append(0)
        for i in range(8):
            val = i * x
            Arow2xy.append(val)
            Arow2xy.append(y)
        for i in range(8):
            val = i * x
            Arow7xy.append(val)
            Arow7xy.append(6 * int(y))
        for i in range(8):
            val = i * x
            Arow8xy.append(val)
            Arow8xy.append(7 * int(y))
        topL.append(Arow1xy)
        topL.append(Arow2xy)
        topL.append(Arow7xy)
        topL.append(Arow8xy)

    def bottomRCoords(self, x, y):
        for i in range(8):
            val = (i * x) + x
            Brow1xy.append(val)
            Brow1xy.append(y)
        for i in range(8):
            val = (i * x) + x
            Brow2xy.append(val)
            Brow2xy.append(2 * int(y))
        for i in range(8):
            val = (i * x) + x
            Brow7xy.append(val)
            Brow7xy.append(7 * int(y))
        for i in range(8):
            val = (i * x) + x
            Brow8xy.append(val)
            Brow8xy.append(8 * int(y))
        bottomR.append(Brow1xy)
        bottomR.append(Brow2xy)
        bottomR.append(Brow7xy)
        bottomR.append(Brow8xy)

    def returnC1(self, e1: int, e2: int):
        v = topL[e1][e2]
        return v

    def returnC2(self, e1, e2):
        v = bottomR[e1][e2]
        return v