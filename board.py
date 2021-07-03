import numpy as np

class board:
    def __init__(self, plr1p:str='X', plr2p:str='O'):
        self.plr1p = plr1p
        self.plr2p = plr2p
        self.matrix = np.zeros((6,7))

    def PrintBoard(self, showbase:bool=True):
        horizontal = ' ═════════════════════════════'
        vertical = '║'
        empty_space = '   '
        base = '╔╩╗                         ╔╩╗'
        #go through board and print correct things, if not empty space print player piece
        for x in range(0, 6):
            print(horizontal)
            print(vertical)
            for y in range(0, 7):
                print(empty_space); print(vertical)
        if showbase == True:
            print(horizontal)
            print(base)
        else:
            print(horizontal)

    def InsertPiece(self, plr:int=1, col:int=0):
        success = False
        #check to make sure the selected column isn't filled
        row = 0
        #go through rows until there is an empty space
        self.matrix[row][col] = plr
        return success

    
