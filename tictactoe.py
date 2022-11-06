import random


class TicTacToe:
    def __init__(self):
        self.player = True
        self.winner = False
        self.turns = 0

        # Can be condensed into one list after game board is finessed
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

        self.rally = ["Ready up, ",
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
        if self.player:
            cry = random.randint(0, len(self.rally) - 1)
            print(f'{self.rally[cry]}Player 1')
        else:
            cry = random.randint(0, len(self.rally) - 1)
            print(f'{self.rally[cry]}Player 2')
        print("(type 'commands' to see move list)")

    def player_input(self, val):
        if val.lower() == "exit":
            quit()

        if val.lower() == "commands":
            print(self.command_info)
            return 1

        move = val.lower()
        if move not in self.commands:
            print("Please enter a valid command")
            return -1

        row, col = self.commands[move]

        if self.board[row][col] != " ":
            print("Space already occupied")
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
                break

    def manager(self):
        # while not self.winner or self.turns < 9:
        while True:
            self.prompts()
            self.print_board()

            # while eval != 0
            while True:
                val = input(": ")
                eval = self.player_input(val)
                if eval == 0:
                    self.turns += 1
                    break

            self.check_winner()
            if self.winner:
                break

            if self.turns == 9:
                break

            self.player = not self.player

        self.print_board()
        self.prompts()
        val = input(": ")
        if val.lower() == "n":
            quit()


if __name__ == "__main__":
    while True:
        game = TicTacToe()
        game.manager()
