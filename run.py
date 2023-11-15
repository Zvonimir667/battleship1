from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "S"

def random_point(size):
	return randint(0, size -1)

def valid_coordinates(x, y, board):
    size = board.size
    return 0 <= x < size and 0 <= y < size and (x, y) not in board.guesses

def populate_board(board):
    while len(board.ships) < board.num_ships:
        x = random_point(board.size)
        y = random_point(board.size)

        if valid_coordinates(x, y, board):
            board.add_ship(x, y)
        else:
            continue

def make_guess(board):
    while True:
        try:
            x = int(input(f"Enter row (0-{board.size-1}): "))
            y = int(input(f"Enter column (0-{board.size-1}): "))

            if valid_coordinates(x, y, board):
                return x, y
            else:
                print("Invalid guess. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


def play_game(computer_board, player_board):


def new_game():
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcome to Battleship game!")
    print(f"Board size: {size}. Number of ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name: \n")
    print("-" * 35)

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)

new_game()