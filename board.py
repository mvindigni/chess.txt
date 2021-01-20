import numpy as np
import pandas as pd
import pieces as p
import eyesore as e

# globals
files = ["A", "B", "C", "D", "E", "F", "G", "H"]
ranks = [8, 7, 6, 5, 4, 3, 2, 1]

def initBoard():
    global files, ranks 
    board = pd.DataFrame(np.zeros((8,8)), columns = files, index = ranks)
    e.populate(board)
    
    return board


def printBoard(board):
    global files, ranks
    
    for r in ranks:
        print(str(r) + "        ", end = "")
        for f in files:
            if board.loc[r, f] != 0.0:
                print(str(board.loc[r, f]) + "    ", end = "")
            else:
                print("--    ", end = "")
        print('\n')
    print("\n         ", end = "")
   
    for f in files:
        print(f + "     ", end = "")








"""           """
""" TEST ZONE """
"""           """
#               #


#               #
"""           """
""" TEST ZONE """
"""           """