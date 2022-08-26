from random import randint
from matrix import Matrix


class MatrixRandomizer:
    """Генератор випадкових матриць"""
    @staticmethod
    def generate_matrix(size):
        """Генерація матриці"""
        data = [[randint(-5000, 5000) / 100 for _ in range(size)] for _ in range(size)]
        return data if MatrixRandomizer.check(data) else MatrixRandomizer.generate_matrix(size)

    @staticmethod
    def check(data):
        """Перевірка даних на можливість обернення"""
        matrix = Matrix(data)
        if matrix.get_determinant() == 0:
            return False
        for i in range(len(data)):
            if data[i][i] == 0:
                return False
        return True
