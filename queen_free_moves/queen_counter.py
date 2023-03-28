import numpy
from numpy import matrix, ndarray
from copy import deepcopy


class QueenSquare:
    """Creating matrix with set position for a Queen and count all available moves"""
    def __init__(self, matrix_length: int):
        if matrix_length < 1:
            raise ValueError("matrix_length can't be less than 2")
        self.counter = 0
        self.sq_matrix: list[list[str]] = [["-"] * matrix_length for _ in range(matrix_length)]
        self.queen_y: int = 0
        self.queen_x: int = 0
        self.queen_pos: dict = {"Y": self.queen_y,
                                "X": self.queen_x
                                }
        self.y: int = 0
        self.x: int = 0
        self.max_index_y: int = len(self.sq_matrix) - 1
        self.max_index_x: int = len(self.sq_matrix[0]) - 1
        self.free_moves: dict = {"Y": [],
                                 "X": [],
                                 "YX": [],
                                 }
        self.marked_moves: list[list[str]] = deepcopy(self.sq_matrix)

    def set_queen(self, y: int, x: int, symbol: str = "Q") -> list[list[str]]:
        """Set Queen position in a matrix"""
        self.sq_matrix[y][x] = symbol
        self.queen_y = y
        self.queen_x = x
        return self.sq_matrix

    def reset_position(self):
        """Reset Queen position for counting"""
        self.y = self.queen_y
        self.x = self.queen_x

    def count_move(self):
        """Count every appended free move"""
        self.counter += 1

    def count_free_moves(self) -> dict:
        """Count all available moves for a Queen"""
        self.reset_position()
        for _ in range(self.max_index_x + 1):
            if _ != self.x:
                self.free_moves["X"].append((self.y, _))
                self.count_move()
        for _ in range(self.max_index_y + 1):
            if _ != self.y:
                self.free_moves["Y"].append((_, self.x))
                self.count_move()
        while self.y > 0 and self.x > 0:
            self.y -= 1
            self.x -= 1
            free_move = (self.y, self.x)
            self.free_moves["YX"].append(free_move)
            self.count_move()
        self.reset_position()
        while self.y > 0 and self.x < self.max_index_x:
            self.x += 1
            self.y -= 1
            free_move = (self.y, self.x)
            self.free_moves["YX"].append(free_move)
            self.count_move()
        self.reset_position()
        while self.x > 0 and self.y < self.max_index_y:
            self.x -= 1
            self.y += 1
            free_move = (self.y, self.x)
            self.free_moves["YX"].append(free_move)
            self.count_move()
        self.reset_position()
        while self.x < self.max_index_x and self.y < self.max_index_y:
            self.x += 1
            self.y += 1
            free_move = (self.y, self.x)
            self.free_moves["YX"].append(free_move)
            self.count_move()
        return self.free_moves

    def mark_free_moves(self, symbol: str = "X") -> matrix | ndarray:
        """Visualising matrix with available moves as a chosen Symbol"""
        for key, value in self.free_moves.items():
            for _ in value:
                self.marked_moves[_[0]][_[1]] = symbol
        return numpy.matrix(self.marked_moves)
