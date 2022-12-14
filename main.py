from result_to_file import ResultToFile
from user_input import UserInput
from matrix_invertor import MatrixInverter
from result_output import ResultOutput


class Program:
    """ Main logic of the program"""
    @staticmethod
    def Main():
        inp = UserInput()
        inp.get_matrix()
        if not inp.matrix:
            print("The program has been closed at the matrix input stage")
            quit(1)
        inp.get_method()
        if not inp.method:
            print("The program has been closed at the method selection stage")
            quit(2)
        m_inv = MatrixInverter.invert_bordering(inp.matrix) if inp.method == 'border' else MatrixInverter.invert_cells(inp.matrix)
        final_result = ResultOutput()
        final_result.output_final_result(m_inv)
        ResultToFile.print_to_file(inp.matrix, inp.method, m_inv)


Program.Main()
