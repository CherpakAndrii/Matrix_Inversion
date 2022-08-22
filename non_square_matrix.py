from matrix import Matrix


class NonSquareMatrix:
    def __init__(self, arg):
        if isinstance(arg, list):
            if len(arg) == 0:
                raise ValueError
            self.height = self.width = 0
            self.data = None
            self.fill(arg)
        elif isinstance(arg, Matrix):
            self.data = arg.data
            self.height = self.width = arg.size
        else: raise TypeError

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)

    def get_submatrix(self, rows_slice, columns_slice):
        if not (isinstance(rows_slice, slice) and isinstance(columns_slice, slice)):
            raise TypeError
        return NonSquareMatrix([line[columns_slice] for line in self.data[rows_slice]])

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return NonSquareMatrix([[num * other for num in line] for line in self.data])
        elif isinstance(other, NonSquareMatrix):
            if self.width == other.height:
                return NonSquareMatrix([[sum(self.data[i][n]*other.data[n][j] for n in range(self.width))
                                         for j in range(other.width)] for i in range(self.height)])
            else:
                raise ValueError
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, NonSquareMatrix):
            if self.width == other.width and self.height == other.height:
                return NonSquareMatrix([[num1+num2 for (num1, num2) in zip(line1, line2)] for (line1, line2) in zip(self.data, other.data)])
            else:
                raise ValueError
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, NonSquareMatrix):
            if self.width == other.width and self.height == other.height:
                return NonSquareMatrix([[num1-num2 for (num1, num2) in zip(line1, line2)]
                                        for (line1, line2) in zip(self.data, other.data)])
            else:
                raise ValueError
        else:
            raise TypeError

    @staticmethod
    def __check_inputted_data(numbers):
        if not (isinstance(numbers, list) and len(numbers) >= 1):
            return False
        if not isinstance(numbers[0], list):
            return False
        row_size = len(numbers[0])
        for line in numbers:
            if not (isinstance(line, list) and len(line) == row_size):
                return False
            for num in line:
                if not (isinstance(num, int) or isinstance(num, float)):
                    return False
        return True

    def fill(self, numbers):
        if NonSquareMatrix.__check_inputted_data(numbers):
            self.data = numbers
            self.height = len(self.data)
            self.width = len(self.data[0])
        else:
            raise TypeError

    def get_minor(self, i, j):
        return NonSquareMatrix([line[:j]+line[j+1:] for line in self.data[:i]+self.data[i+1:]])
