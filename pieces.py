class Pawn:
    def __init__(self, color):
        self.color = color
        self.id = color + 'P'

    def __str__(self):
        return self.id
    
class Rook:
    def __init__(self, color):
        self.color = color
        self.id = color + 'R'

    def __str__(self):
        return self.id

class Knight:
    def __init__(self, color):
        self.color = color
        self.id = color + 'N'

    def __str__(self):
        return self.id

class Bishop:
    def __init__(self, color):
        self.color = color
        self.id = color + 'B'

    def __str__(self):
        return self.id

class Queen:
    def __init__(self, color):
        self.color = color
        self.id = color + 'Q'

    def __str__(self):
        return self.id

class King:
    def __init__(self, color):
        self.color = color
        self.id = color + 'K'

    def __str__(self):
        return self.id
