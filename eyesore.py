import pieces as p

files = ["A", "B", "C", "D", "E", "F", "G", "H"]
ranks = [8, 7, 6, 5, 4, 3, 2, 1]

def populate(board):
    global files, ranks
    
    # pawns
    for x in range(8):
            board.loc[2, files[x]] = p.Pawn('W')
            board.loc[7, files[x]] = p.Pawn('B')

    # pieces
    board.loc[1, 'A'] = p.Rook('W')
    board.loc[1, 'H'] = p.Rook('W')
    board.loc[8, 'A'] = p.Rook('B')
    board.loc[8, 'H'] = p.Rook('B')

    board.loc[1, 'B'] = p.Knight('W')
    board.loc[1, 'G'] = p.Knight('W')
    board.loc[8, 'B'] = p.Knight('B')
    board.loc[8, 'G'] = p.Knight('B')
    
    board.loc[1, 'C'] = p.Bishop('W')
    board.loc[1, 'F'] = p.Bishop('W')    
    board.loc[8, 'C'] = p.Bishop('B')
    board.loc[8, 'F'] = p.Bishop('B')
    
    board.loc[1, 'D'] = p.Queen('W')
    board.loc[1, 'E'] = p.King('W')
    board.loc[8, 'E'] = p.King('B')
    board.loc[8, 'D'] = p.Queen('B')