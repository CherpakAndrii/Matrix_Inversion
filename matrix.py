import numpy as np
class Matrix:
    def __init__(self, arg):
        if isinstance(arg, int):
            if arg < 1:
                raise ValueError
            self.size = arg
            self.data = [[0.0 for _ in range(arg)] for _ in range(arg)]
            for i in range(self.size):
                self.data[i][i] = 1.0
        elif isinstance(arg, list):
            if len(arg) == 0:
                raise ValueError
            self.size = len(arg)
            self.data = None
            self.fill(arg)
        else:
            print(type(arg))
            raise TypeError

    def __eq__(self, other):
        if not (isinstance(other, Matrix) and self.size == other.size):
            return False
        for ln1, ln2 in zip(self.data, other.data):
            for el1, el2 in zip(ln1, ln2):
                if el1 != el2:
                    return False
        return True

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Matrix([line[index] for line in self.data[index]])
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[num * other for num in line] for line in self.data])
        elif isinstance(other, Matrix):
            if self.size == other.size:
                return Matrix([[sum(self.data[i][n]*other.data[n][j] for n in range(self.size))
                                for j in range(self.size)] for i in range(self.size)])
            else:
                raise ValueError
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.size == other.size:
                return Matrix([[num1+num2 for (num1, num2) in zip(line1, line2)]
                               for (line1, line2) in zip(self.data, other.data)])
            else:
                raise ValueError
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.size == other.size:
                return Matrix([[num1-num2 for (num1, num2) in zip(line1, line2)]
                               for (line1, line2) in zip(self.data, other.data)])
            else:
                raise ValueError
        else:
            raise TypeError

    @staticmethod
    def __check_inputted_data(numbers, size):
        if not (isinstance(numbers, list) and len(numbers) == size):
            return False
        for line in numbers:
            if not (isinstance(line, list) and len(line) == size):
                return False
            for num in line:
                if not (isinstance(num, int) or isinstance(num, float)):
                    return False
        return True

    def fill(self, numbers):
        if Matrix.__check_inputted_data(numbers, self.size):
            self.data = numbers
        else:
            raise TypeError

    def get_minor(self, i, j):
        return Matrix([line[:j]+line[j+1:] for line in self.data[:i]+self.data[i+1:]])

    def get_determinant(self):
        if self.size == 1:
            return self.data[0][0]
        return sum([self.data[0][i] * (-1) ** i * self.get_minor(0, i).get_determinant() for i in range(self.size)]) \
            if self.size < 8 else np.linalg.det(np.array(self.data)) # для n>=8 пошук детермінанту займає
        # значно більше часу через факторіальну складність алгоритму, тому використаємо numpy

    def add_border(self, row, column, corner_element):
        numbers = self.data
        row.data[0].append(corner_element)
        numbers.append(
            row.data[0])
        for i in range(self.size):
            numbers[i].append(column.data[i][0])
        return Matrix(numbers)

    def __round__(self, n=3):
        for i in range(self.size):
            for j in range(self.size):
                self.data[i][j] = round(self.data[i][j], n)
        return self
