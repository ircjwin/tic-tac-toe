import random


class TicTacToe:
    def __init__(self):
        self.player = True
        self.winner = False
        self.turns = 0

        # Can be condensed into one list or dictionary after game board is finessed
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

        # Left to right: top 0-2, middle 3-5, bottom 6-8
        self.test_board = [" ", " ", " ",
                           " ", " ", " ",
                           " ", " ", " "]

        self.rally_cry = ["Ready up, ",
                          "Go get 'em, ",
                          "Never give up, ",
                          "You can do it, ",
                          "I believe in you, ",
                          "Release your inner strength, "]

        self.commands = {
            "tl": (0, 0),
            "tm": (0, 1),
            "tr": (0, 2),
            "ml": (1, 0),
            "mm": (1, 1),
            "mr": (1, 2),
            "bl": (2, 0),
            "bm": (2, 1),
            "br": (2, 2)
        }

        self.command_info =\
            "tl: Top Left Square\n" \
            "tm: Top Middle Square\n" \
            "tr: Top Right Square\n" \
            "ml: Middle Left Square\n" \
            "mm: Middle Middle Square\n" \
            "mr: Middle Right Square\n" \
            "bl: Bottom Left Square\n" \
            "bm: Bottom Middle Square\n" \
            "br: Bottom Right Square"

        # Backend checks don't need as much abstraction or human readability
        # Consider checking conditions with indices to remove dependency on self.commands
        self.win_conditions = {
            # Horizontals
            "Condition 1": ("tl", "tm", "tr"),
            "Condition 2": ("ml", "mm", "mr"),
            "Condition 3": ("bl", "bm", "br"),
            # Verticals
            "Condition 4": ("tl", "ml", "bl"),
            "Condition 5": ("tm", "mm", "bm"),
            "Condition 6": ("tr", "mr", "br"),
            # Diagonals
            "Condition 7": ("tl", "mm", "br"),
            "Condition 8": ("tr", "mm", "bl")
        }

        self.test_win_conditions = {
            # Horizontals
            "Condition 1": (0, 1, 2),
            "Condition 2": (3, 4, 5),
            "Condition 3": (6, 7, 8),
            # Verticals
            "Condition 4": (0, 3, 6),
            "Condition 5": (1, 4, 7),
            "Condition 6": (2, 5, 8),
            # Diagonals
            "Condition 7": (0, 4, 8),
            "Condition 8": (2, 4, 6)
        }

        self.test_commands = {
            "tl": 0,
            "tc": 1,
            "tr": 2,
            "cl": 3,
            "c": 4,
            "cr": 5,
            "bl": 6,
            "bc": 7,
            "br": 8
        }

        self.test_command_info = \
            "tl: Top Left Square\n" \
            "tc: Top Center Square\n" \
            "tr: Top Right Square\n" \
            "cl: Center Left Square\n" \
            "c: Center Square\n" \
            "cr: Center Right Square\n" \
            "bl: Bottom Left Square\n" \
            "bc: Bottom Center Square\n" \
            "br: Bottom Right Square"

    def test_print_board(self):
        print(f" {self.test_board[0]} | {self.test_board[1]} | {self.test_board[2]}")
        print("---|---|---")
        print(f" {self.test_board[3]} | {self.test_board[4]} | {self.test_board[5]}")
        print("---|---|---")
        print(f" {self.test_board[6]} | {self.test_board[7]} | {self.test_board[8]}")

    # Finesse game board
    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def prompts(self):
        if self.winner:
            if self.player:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            print("Play again? (y/n)")
            return

        if self.turns == 9:
            print("That's a tie!")
            print("Play again? (y/n)")
            return

        if self.turns == 0:
            print("Welcome to Tic-Tac-Toe!")
            print("(type 'commands' to see move list)\n")

        if self.player:
            index = random.randint(0, len(self.rally_cry) - 1)
            print(f'{self.rally_cry[index]}Player 1!')
        else:
            index = random.randint(0, len(self.rally_cry) - 1)
            print(f'{self.rally_cry[index]}Player 2!')

    def player_input(self, user_cmd):
        if user_cmd.lower() == "exit":
            quit()

        if user_cmd.lower() == "commands":
            print(self.command_info)
            return 1

        move = user_cmd.lower()
        if move not in self.commands:
            print("Please enter a valid command.")
            return -1

        row, col = self.commands[move]

        if self.board[row][col] != " ":
            print("Space already occupied.")
            return -1

        if self.player:
            self.board[row][col] = "X"
        else:
            self.board[row][col] = "O"

        return 0

    def check_winner(self):
        if self.player:
            fill = "X"
        else:
            fill = "O"

        for key in self.win_conditions:
            condition = self.win_conditions[key]

            row_1, col_1 = self.commands[condition[0]]
            row_2, col_2 = self.commands[condition[1]]
            row_3, col_3 = self.commands[condition[2]]

            space_1 = self.board[row_1][col_1]
            space_2 = self.board[row_2][col_2]
            space_3 = self.board[row_3][col_3]

            if fill == space_1 == space_2 == space_3:
                self.winner = True
                return

    def manager(self):
        while self.winner is False and self.turns < 9:
            if self.turns > 0:
                self.player = not self.player
            self.prompts()
            self.print_board()
            cmd_check = 1

            while cmd_check != 0:
                user_cmd = input(": ")
                cmd_check = self.player_input(user_cmd)

            self.turns += 1
            self.check_winner()

        self.print_board()
        self.prompts()
        user_cmd = input(": ")
        if user_cmd.lower() == "n":
            quit()


if __name__ == "__main__":
    while True:
        game = TicTacToe()
        game.manager()

    # game = TicTacToe()
    # game.test_print_board()

