from tkinter import Label, Button, Tk, Entry, Frame, StringVar, Radiobutton, END, messagebox
from style import *
from matrix import Matrix
from matrix_randomizer import MatrixRandomizer


class UserInput:
    """Введення матриці і методу розв'язання"""
    def __init__(self):
        self.__fields = []
        self.__field_values = []
        self.__lines = []
        self.matrix_size = 0
        self.matrix = None
        self.method = None

    def get_matrix(self):
        """Введення матриці"""
        root = Tk()
        root.config(bg=standard_bg)
        root.title("Обернення матриці")
        root.geometry('850x450')

        label1 = Label(root, fg='blue', bg=standard_bg, text="Введіть матрицю:", font=article_font, height=3)
        field_frame = Frame(root)
        button_frame = Frame(root)

        # just a function for info button
        def get_info():
            """Виведення інформації про матрицю, яку повинно бути введено"""
            messagebox.showinfo("Введення матриці",
                                '''Введіть матрицю, використовуючи цифри, оператор "-" та роздільник ".". Порожні поля будуть замінені нулями.''')

        def increase():
            """Збільшення розмірностей матриці"""
            new_line = Frame(field_frame)
            self.__lines.append(new_line)
            values = [StringVar() for _ in range(self.matrix_size)]
            self.__field_values.append(values)
            new_fields = [Entry(new_line, width=7, textvariable=v, highlightbackground=standard_bg) for v in values]
            self.__fields.append(new_fields)

            new_line.pack()
            for f in new_fields:
                f.pack(side='left')

            self.matrix_size += 1
            for i in range(self.matrix_size):
                new_val = StringVar()
                self.__field_values[i].append(new_val)
                new_field = Entry(self.__lines[i], width=7, textvariable=new_val, highlightbackground = standard_bg)
                self.__fields[i].append(new_field)
                new_field.pack(side='left')

            button_reduce.config(highlightbackground=standard_button_bg, state='normal')
            if self.matrix_size >= 10:
                button_increase.config(highlightbackground=disabled_button_bg, state='disabled')

        def reduce():
            """Зменшення розмірностей матриці"""
            self.__fields.pop()
            self.__lines.pop().pack_forget()
            self.__field_values.pop()

            self.matrix_size -= 1
            for i in range(self.matrix_size):
                redundant_field = self.__fields[i].pop()
                self.__field_values[i].pop()
                redundant_field.pack_forget()

            button_increase.config(highlightbackground=standard_button_bg, state='normal')
            if self.matrix_size <= 2:
                button_reduce.config(highlightbackground=disabled_button_bg, state='disabled')

        def randomize():
            """Введення випадкової матриці у поля"""
            if self.matrix_size >= 8:
                clear()
                label1.config(text="Очікуйте...")
                root.update()
            data = MatrixRandomizer.generate_matrix(self.matrix_size)
            for i in range(self.matrix_size):
                for j in range(self.matrix_size):
                    self.__field_values[i][j].set(str(round(data[i][j], 2)))
                    root.update()
            label1.config(text="Введіть матрицю:")

        def clear():
            """Очищення полів"""
            for line in self.__fields:
                for field in line:
                    field.delete(0, END)

        def __parse_matrix():
            """Парсинг введеної матриці"""
            numbers = []
            for line in self.__field_values:
                row = []
                for field in line:
                    str_val = field.get().replace(' ', '')
                    if len(str_val) == 0:
                        row.append(0)
                    elif (str_val[1:] if str_val[0] == '-' else str_val).replace('.', '', 1).isdigit():
                        row.append(float(str_val))
                    else:
                        raise TypeError
                numbers.append(row)
            if MatrixRandomizer.check(numbers):
                return Matrix(numbers)
            else:
                raise ValueError

        # closes the current window and going to the next stage
        def go_next():
            """Перехід до наступного пункту"""
            try:
                self.matrix = __parse_matrix()
                root.destroy()
            except TypeError:
                messagebox.showinfo("Помилка вводу", "Будь ласка, не використовуйте інших символів, окрім цифр, знаку" +
                                    " '-' перед числом та роздільника '.'!")
            except ValueError:
                messagebox.showinfo("Вироджена матриця", "Увага! Вироджені матриці або матриці з нулями на головній" +
                                    " діагоналі не можуть бути обернені! Будь ласка, введіть іншу матрицю!")
            except:
                messagebox.showinfo("Неочікувана помилка", "Упс, щось пішло не так :(")

        button_increase = Button(button_frame, text="+", command=increase, font=button_font, width=10, height=3,
                                 highlightbackground=standard_button_bg, fg=button_fg)
        button_reduce = Button(button_frame, text="-", command=reduce, font=button_font, width=10, height=3,
                               highlightbackground=standard_button_bg, fg=button_fg)
        button_random = Button(button_frame, text="Random", command=randomize, font=button_font, width=10, height=3,
                               highlightbackground=standard_button_bg, fg=button_fg)
        button_clear = Button(button_frame, text="Очистити", command=clear, font=button_font, width=20, height=3,
                              highlightbackground=cancel_button_bg, fg=button_fg)
        button_next = Button(button_frame, text="Далі", command=go_next, font=button_font, width=20, height=3,
                             highlightbackground=confirm_button_bg, fg=button_fg)
        button_info = Button(root, text="?", command=get_info, font=button_font, width=4, height=2, highlightbackground=info_button_bg,
                             fg=button_fg)

        label1.pack()
        field_frame.pack()
        button_frame.place(anchor='center', relx=0.5, rely=0.9)
        button_increase.pack(side='left')
        button_reduce.pack(side='left')
        button_random.pack(side='left')
        button_clear.pack(side='left')
        button_next.pack(side='left')
        button_info.place(anchor='ne', relx=1, rely=0)
        increase()
        increase()
        button_reduce.config(state='disabled', highlightbackground=disabled_button_bg)

        root.mainloop()

    def get_method(self):
        """Обрання методу обернення матриці"""
        root = Tk()
        root.config(bg=standard_bg)
        root.title("Обернення матриці")
        root.geometry('400x230')

        label1 = Label(root, fg='blue', bg=standard_bg, text="Оберіть метод обернення матриці:", font=article_font)
        method = StringVar(value="cells")
        rb1 = Radiobutton(root, text="Метод окаймлення", bg=standard_bg, variable=method, value="border")
        rb2 = Radiobutton(root, text="Метод розбиття на клітинки", bg=standard_bg, variable=method, value="cells")

        def get_info():
            """Виведення інформації про методи обернення матриці"""
            messagebox.showinfo("Дані про методи", "Методи окаймлення та розбиття на клітки передбачають знаходження обернених иатрць високих розмірностей відштовхуючись від відомих обернених матриць менших розмірностей. Метод окаймлення використовує підматрицю на 1 розмірність меншу, а метод розбиття на клітинки намагається розбити введену матрицю на 4 приблизно однакових сектори. Після цього обидва методи рекурсивно викликаються для цих підматриць.")

        # closes the current window and going to the next stage
        def end():
            """Перехід до наступного пункту"""
            self.method = method.get()
            root.destroy()

        button_info = Button(root, text="?", command=get_info, width=4, height=2, font=button_font, highlightbackground=info_button_bg,
                             fg=button_fg)
        button_end = Button(root, text="Обчислити", command=end, width=15, height=3, font=button_font,
                            highlightbackground=confirm_button_bg, fg=button_fg)

        label1.place(anchor='center', relx=0.5, rely=0.25)
        button_info.place(anchor='ne', relx=1, rely=0)
        rb1.place(anchor='w', relx=0.15, rely=0.45)
        rb2.place(anchor='w', relx=0.15, rely=0.60)
        button_end.place(anchor='center', relx=0.5, rely=0.87)

        root.mainloop()
