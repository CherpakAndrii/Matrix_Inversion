from user_input import UserInput
from matrix_invertor import MatrixInverter


inp = UserInput()
inp.get_matrix()
if not inp.matrix:
    print("The program has been closed at the matrix input stage")
    quit(1)
inp.get_method()
if not inp.method:
    print("The program has been closed at the method selection stage")
    quit(2)
print("Inputted: ", inp.matrix)

m_inv = MatrixInverter.invert_bordering(inp.matrix) if inp.method == 'border' else MatrixInverter.invert_cells(inp.matrix)
test = round(m_inv * inp.matrix)
round(m_inv)
print()
print("Method: ", inp.method)
print("Inverted: ", m_inv)
print()
print("Test: ", test)
