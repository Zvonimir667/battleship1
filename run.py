from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    def __init__(self, size, num_ships, name, type):
        """
        Initialize a game board.

        Parameters:
        - size (int): The size of the square board.
        - num_ships (int): The number of ships to be placed on the board.
        - name (str): The name of the player or computer.
        - type (str): The type of the board, either "player" or "computer".
        """
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        """
        Print the current state of the board.
        """
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        """
        Make a guess on the board and update the board state.

        Parameters:
        - x (int): The row index of the guess.
        - y (int): The column index of the guess.

        Returns:
        - str: The result of the guess, either "Hit" or "Miss".
        """
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        """
        Add a ship to the board at the specified coordinates.

        Parameters:
        - x (int): The row index to place the ship.
        - y (int): The column index to place the ship.
        - type (str): The type of the ship, default is "computer".
        """
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "S"


def random_point(size):
    """
    Generate a random coordinate within the given size.

    Parameters:
    - size (int): The size of the board.

    Returns:
    - int: A random coordinate within the board size.
    """
    return randint(0, size - 1)


def valid_coordinates(x, y, board):
    """
    Check if the given coordinates are valid for the board.

    Parameters:
    - x (int): The row index.
    - y (int): The column index.
    - board (Board): The game board.

    Returns:
    - bool: True if the coordinates are valid, False otherwise.
    """"
    size = board.size
    return 0 <= x < size and 0 <= y < size and (x, y) not in board.guesses


def populate_board(board):
    """
    Populate the board with ships until the required number is reached.

    Parameters:
    - board (Board): The game board to populate.
    """
    while len(board.ships) < board.num_ships:
        x = random_point(board.size)
        y = random_point(board.size)

        if valid_coordinates(x, y, board):
            board.add_ship(x, y)
        else:
            continue


def make_guess(board):
    """
    Get user input for a guess until a valid one is provided.

    Parameters:
    - board (Board): The game board.

    Returns:
    - tuple: A valid guess as a tuple (x, y).
    """
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
    """
    Play the Battleship game.

    Parameters:
    - computer_board (Board): The computer's game board.
    - player_board (Board): The player's game board.
    """
    while True:
        print("\nYour Board:")
        player_board.print()
        x, y = make_guess(player_board)
        result = computer_board.guess(x, y)
        print(f"\nYour guess: ({x}, {y}) - {result}")

        if result == "Hit":
            scores["player"] += 1

        if scores["player"] == player_board.num_ships:
            print("\nYou sunk all the computer's ships. You win!")
            break

        print("\nComputer's Board:")
        computer_board.print()
        x = random_point(computer_board.size)
        y = random_point(computer_board.size)
        result = player_board.guess(x, y)
        print(f"\nComputer's guess: ({x}, {y}) - {result}")

        if result == "Hit":
            scores["computer"] += 1

        if scores["computer"] == computer_board.num_ships:
            print("\nOh no! The computer sunk all your ships. You lose!")
            break


def new_game():
    """
    Start a new game of Battleship.
    """
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
