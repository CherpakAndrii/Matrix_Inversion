from user_input import UserInput


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
