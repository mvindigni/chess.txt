import re

def read(move):
    data = []    
    if re.match(r'^[a-h]', move): # check if pawn is being moved

        if re.match(r'[a-h][1-8][BNQR]?$', move): #check for pawn move
            e = re.compile(r'(?P<dest>[a-h][1-8])(?P<promote>[BKNQR])?$')
            dest = e.match(move).group('dest') #get destination of pawn move
            data.append(dest)
            
            if dest[1] == '8' or dest[1] == '1': #if pawn goes to last rank, get promotion piece
                data.append(e.match(move).group('promote'))
       
        elif re.match(r'[a-h]x[a-h][1-8][BKNQR]?$', move): #check for pawn capture
            e = re.compile(r'(?P<loc>[a-h])x(?P<dest>[a-h][1-8])(?P<piece>[BKNQR])?$')            
            data += list(e.match(move).group('loc', 'dest'))
            dest = e.match(move).group('dest')

            if dest[1] == '8' or dest[1] == '1': #if pawn goes to last rank, get promotion piece
                data.append(e.match(move).group('promote'))
    
    elif re.match(r'^[BKNQR]', move): # check if non-pawn is being moved
        if re.match(r'[BKNQR][a-h]?[1-8]?[a-h][1-8]$', move): #check for non-pawn move
            e = re.compile(r'(?P<piece>[BKNQR])(?P<ref>[a-h]?[1-8]?)(?P<dest>[a-h][1-8])$')
            data += e.match(move).group('piece', 'dest', 'ref')

        if re.match(r'[BKNQR][a-h]?[1-8]?x[a-h][1-8]$', move): #check for non-pawn capture
            e = re.compile(r'(?P<piece>[BKNQR])(?P<ref>[a-h]?[1-8]?)x(?P<dest>[a-h][1-8])$')
            data += e.match(move)

    elif re.match(r'([O][-]){1,2}O$', move): #check for castles
        data = 'KC' if re.match(r'O-O$', move) else 'QC'
    
    if not data:
        print('invalid notation')
        pass
    else: return (data)