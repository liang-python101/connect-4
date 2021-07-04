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
        num_rows, num_cols = self.matrix.shape
        for row in range(0,num_rows):
            newline = ' ' + vertical
            for col in range(0,num_cols):
                loc_status = self.matrix[row][col]
                if loc_status == 0:
                    newline += empty_space
                elif loc_status == 1:
                    newline = newline + ' ' + self.plr1p + ' '
                elif loc_status == 2:
                    newline = newline + ' ' + self.plr2p + ' '
                newline += vertical
            print(horizontal)
            print(newline)
        print(horizontal)
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

    
