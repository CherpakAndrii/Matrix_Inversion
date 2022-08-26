from tkinter import Label, Frame, Button, Tk
from style import *
from non_square_matrix import NonSquareMatrix
from matrix import Matrix


class ResultOutput:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg=standard_bg)
        self.root.title("Обернення матриці")
        self.root.geometry('850x450')
        self.temporary_elements = []

        self.title_label = Label(self.root, fg='blue', bg=standard_bg, font=article_font)
        self.field_frame = Frame(self.root, bg=standard_bg)
        self.next_button = Button(self.root, width=15, height=3, font=button_font,
                                  highlightbackground=confirm_button_bg, fg=button_fg)

        self.title_label.place(anchor='center', relx=0.5, rely=0.1)
        self.next_button.place(anchor='center', relx=0.5, rely=0.9)
        self.field_frame.place(anchor='center', relx=0.5, rely=0.5)

    def clear(self):
        for element in self.temporary_elements:
            element.pack_forget()

    def output_border(self, matrix, submatrix_inv, V, U, alpha, r, q, B_inv, A_inv):
        def next1():
            self.clear()
            self.__output_matrix("Обернена підматриця: ", submatrix_inv, next2)

        def next2():
            self.clear()
            self.__output_matrix("V - останній рядок початкової матриці", V, next3)

        def next3():
            self.clear()
            self.__output_matrix("U - останній стовпець початкової матриці", U, next4)

        def next4():
            self.clear()
            self.__output_one_value("a = A[k][k] - V * submatrix_inv * U", "a = ", alpha, next5)

        def next5():
            self.clear()
            self.__output_matrix("r = submatr_inv * U * (-1 / a)", r, next6)

        def next6():
            self.clear()
            self.__output_matrix("q = V * submatr_inv * (-1 / a)", q, next7)

        def next7():
            self.clear()
            self.__output_matrix("B^(-1) = submatr_inv - (submatr_inv*U)*q", B_inv, next8)

        def next8():
            self.clear()
            self.__output_matrix("A^(-1) = ((B^(-1), r), (q, 1/a))", A_inv, next9, "Next iteration")

        def next9():
            self.clear()
            self.root.destroy()

        self.__output_matrix("Введена матриця: ", matrix, next1)
        self.root.mainloop()

    def output_cells(self, matrix, t, p, A, B, C, D, D_inv, X, Y, K, L, M, N, res):
        def next1():
            self.clear()
            self.__output_one_value("Розмір матриці t", "t = ", t, next2)

        def next2():
            self.clear()
            self.__output_one_value("Половина розміру матриці p", "p = t/2 = ", p, next3)

        def next3():
            self.clear()
            self.__output_matrix("Верхня ліва підматриця A", A, next4)

        def next4():
            self.clear()
            self.__output_matrix("Верхня права підматриця B", B, next5)

        def next5():
            self.clear()
            self.__output_matrix("Нижня ліва підматриця C", C, next6)

        def next6():
            self.clear()
            self.__output_matrix("Нижня права підматриця D", D, next7)

        def next7():
            self.clear()
            self.__output_matrix("Інвертована підматриця D^(-1)", D_inv, next8)

        def next8():
            self.clear()
            self.__output_matrix("Проміжна підматриця X = B*D^(-1)", X, next9)

        def next9():
            self.clear()
            self.__output_matrix("Проміжна підматриця Y = D^(-1)*C", Y, next10)
        def next10():
            self.clear()
            self.__output_matrix("Результуюча підматриця K = (A-X*C)^(-1)", K, next11)

        def next11():
            self.clear()
            self.__output_matrix("Результуюча підматриця L = K*X*(-1)", L, next12)

        def next12():
            self.clear()
            self.__output_matrix("Результуюча підматриця M = Y*K*(-1)", M, next13)

        def next13():
            self.clear()
            self.__output_matrix("Результуюча підматриця N = D^(-1) - Y*L", N, next14)

        def next14():
            self.clear()
            self.__output_matrix("Результуюча обернена матриця", res, next15)

        def next15():
            self.clear()
            self.root.destroy()

        self.__output_matrix("Введена матриця: ", matrix, next1)
        self.root.mainloop()

    def __output_matrix(self, title: str, matrix: NonSquareMatrix, next_func, button_text='Next value'):
        if isinstance(matrix, Matrix):
            matrix = NonSquareMatrix(matrix.data)

        self.title_label.config(text=title)
        self.next_button.config(text=button_text, command=next_func)

        for line in matrix.data:
            line_frame = Frame(self.field_frame, bg=standard_bg)
            line_frame.pack()
            self.temporary_elements.append(line_frame)
            for element in line:
                matrix_label = Label(line_frame, text=str(round(element, 3)), bg=standard_bg, font=matrix_label_font,
                      height=matrix_label_height, width=matrix_label_width, fg=matrix_label_fg)
                matrix_label.pack(side='left')
                self.temporary_elements.append(matrix_label)

    def __output_one_value(self, title: str, text: str, value: float, next_func, button_text='Next value'):
        self.title_label.config(text=title)
        self.next_button.config(text=button_text, command=next_func)
        val_label = Label(self.field_frame, text=text+str(round(value, 3)), bg=standard_bg, font=matrix_label_font,
                      height=matrix_label_height, width=matrix_label_width, fg=matrix_label_fg)
        val_label.pack()
        self.temporary_elements.append(val_label)
