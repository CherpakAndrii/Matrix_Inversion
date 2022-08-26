from matrix import Matrix


class ResultToFile:
    """Збереження результатів у файл"""
    @staticmethod
    def print_to_file(inp_matrix: Matrix, method: str, result_matrix: Matrix, filename="result.txt"):
        """Вивиедення результатів"""
        test = round(result_matrix * inp_matrix)
        round(result_matrix)
        handle = open(filename, 'w+')
        handle.write("Введена матриця:\n")
        handle.write(ResultToFile.__matr_to_string(inp_matrix))
        handle.write('\n')
        handle.write("Метод: "+("Окаймлення" if method == 'border' else "Розбиття на клітки")+'\n')
        handle.write('\n')
        handle.write("Результат:\n")
        handle.write(ResultToFile.__matr_to_string(result_matrix))
        handle.write('\n')
        handle.write("Test: "+str(Matrix(test.data) == Matrix(inp_matrix.size))+'\n')
        handle.close()

    @staticmethod
    def __matr_to_string(matrix: Matrix):
        """Виведення матриці"""
        string = ""
        for line in matrix.data:
            for num in line:
                string += str(num).ljust(8)
            string += "\n"
        return string
