class Matrix:
    def __init__(self, arg):
        if isinstance(arg, int):
            if arg < 1: raise ValueError
            self.size = arg
            self.data = [[0 for _ in range(arg)] for _ in range(arg)]
            for i in range(self.size):
                self.data[i][i] = 1
        elif isinstance(arg, list):
            if len(arg) == 0: raise ValueError
            self.size = len(arg)
            self.fill(arg)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        if isinstance(index, slice):
            numbers = [line[index] for line in self.data[index]]
            return Matrix(numbers)
        else:
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            numbers = [[num * other for num in line] for line in self.data]
            new_matrix = Matrix(self.size)
            new_matrix.fill(numbers)
            return new_matrix
        elif isinstance(other, Matrix):
            if self.size == other.size:
                numbers = [[sum(self.data[i][n]*other.data[n][j]
                                for n in range(self.size))
                            for j in range(self.size)]
                           for i in range(self.size)]
                new_matrix = Matrix(self.size)
                new_matrix.fill(numbers)
                return new_matrix
            else:
                raise ValueError
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.size == other.size:
                new_matrix = Matrix(self.size)
                numbers = [[num1+num2 for (num1, num2) in zip(line1, line2)]
                           for (line1, line2) in zip(self.data, other.data)]
                new_matrix.fill(numbers)
                return new_matrix
            else:
                raise ValueError
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.size == other.size:
                new_matrix = Matrix(self.size)
                numbers = [[num1-num2 for (num1, num2) in zip(line1, line2)]
                           for (line1, line2) in zip(self.data, other.data)]
                new_matrix.fill(numbers)
                return new_matrix
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
        numbers = [line[:j]+line[j+1:] for line in self.data[:i]+self.data[i+1:]]
        return Matrix(numbers)

    def get_determinant(self):
        if self.size == 1: return self.data[0][0]
        determinant = 0
        for i in range(self.size):
            determinant += self.data[0][i] * (-1) ** i * self.get_minor(0, i).get_determinant()
        return determinant
