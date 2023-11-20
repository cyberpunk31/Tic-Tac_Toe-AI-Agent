import random

class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def display_board(self):
        for i in range(3):
            print('| ' + self.board[i*3] + ' | ' + self.board[i*3+1] + ' | ' + self.board[i*3+2] + ' |')

    def check_move(self, move):
        if move < 0 or move > 8 or self.board[move] != ' ':
            return False
        else:
            return True

    def make_move(self, move, player):
        if self.check_move(move):
            self.board[move] = player
            self.current_player = 'X' if self.current_player == 'O' else 'O'
            return True
        else:
            return False

    def check_win(self):
        winning_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for condition in winning_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def check_tie(self):
        for cell in self.board:
            if cell == ' ':
                return False
        return True

class AI:
    def __init__(self):
        self.depth = 6

    def minimax(self, board, depth, maximizing):
        if board.check_win() or board.check_tie():
            if maximizing:
                if board.check_win():
                    return -10
                elif board.check_tie():
                    return 0
                else:
                    return 10
            else:
                if board.check_win():
                    return 10
                elif board.check_tie():
                    return 0
                else:
                    return -10

        if maximizing:
            best_value = -float('inf')
            for move in range(9):
                if board.check_move(move):
                    board.make_move(move, 'X')
                    value = self.minimax(board, depth - 1, False)
                    board.make_move(move, ' ')
                    best_value = max(best_value, value)
            return best_value

        else:
            best_value = float('inf')
            for move in range(9):
                if board.check_move(move):
                    board.make_move(move, 'O')
                    value = self.minimax(board, depth - 1, True)
                    board.make_move(move, ' ')
                    best_value = min(best_value, value)
            return best_value

    def get_best_move(self, board):
        best_value = -float('inf')
        best_move = None

        for move in range(9):
            if board.check_move(move):
                board.make_move(move, 'X')
                value = self.minimax(board, self.depth - 1, False)
                board.make_move(move, ' ')

                if value > best_value:
                    best_value = value
                    best_move = move

        return best_move


def play_game():
    board = Board()
    ai = AI()

    while True:
        board.display_board()

        if board.current_player == 'X
