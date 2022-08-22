from user_input import UserInput
from matrix_invertor import MatrixInverter


t = UserInput()
t.get_matrix()
if not t.matrix:
    print("The program has been closed at the matrix input stage")
    quit(1)
t.get_method()
if not t.method:
    print("The program has been closed at the method selection stage")
    quit(2)
print(t.matrix)
print(t.matrix_size)
print(t.method)

t_inv = MatrixInverter.invert_bordering(t.matrix)
round(t_inv)
print()
print(t_inv)
print()
print(round(t_inv*t.matrix))
