from random import randint
from matrix import Matrix


class MatrixRandomizer:
    @staticmethod
    def generate_matrix(size):
        data = [[randint(-5000, 5000) / 100 for _ in range(size)] for _ in range(size)]
        matrix = Matrix(data)
        return data if matrix.get_determinant() != 0 else MatrixRandomizer.generate_matrix(size)
