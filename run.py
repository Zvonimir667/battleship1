from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]