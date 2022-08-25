from matrix import Matrix


class ResultToFile:
    @staticmethod
    def print_to_file(inp_matrix: Matrix, method: str, result_matrix: Matrix, filename="result.txt"):
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
        string = ""
        for line in matrix.data:
            for num in line:
                string += str(num).ljust(8)
            string += "\n"
        return string
