import tkinter

# Настройка окна
root = tkinter.Tk()
root.geometry("600x500")

# Создание поля для ввода
entry = tkinter.Entry(root, width=25, font=("Arial", 20))
entry.grid(columnspan=3)


class Calculator:
    """Класс калькулятора."""

    def __init__(self):
        self.znak = ""
        self.operation = False
        self.proverka = False
        self.result = 0
        self.first_number = 0

    def numb_clear(self):
        """Очистка поля ввода."""
        entry.delete(0, tkinter.END)
        self.result = 0
        self.first_number = 0
        self.znak = ""

    def kalkulator(self, number):
        """Добавление цифры в поле ввода."""
        if self.proverka:
            entry.delete(0, tkinter.END)
            self.proverka = False
        entry.insert('end', number)
        self.operation = True

    def plusik(self):
        """Сложение."""
        if self.operation:
            self.first_number = float(entry.get())
            entry.delete(0, tkinter.END)
            self.proverka = True
        self.operation = False
        self.znak = "+"

    def minecraft(self):
        """Вычитание."""
        if self.operation:
            self.first_number = float(entry.get())
            entry.delete(0, tkinter.END)
            self.proverka = True
        self.operation = False
        self.znak = "-"

    def ravno(self):
        """Вычисление результата."""
        if self.znak == "+":
            self.result = self.first_number + float(entry.get())
        elif self.znak == "-":
            self.result = self.first_number - float(entry.get())
        elif self.znak == "*":
            self.result = self.first_number * float(entry.get()) 
        elif self.znak == "/":
            self.result = self.first_number / float(entry.get())
        elif self.znak == "^":
            self.result = self.first_number ** float(entry.get())    
        entry.delete(0, tkinter.END)
        entry.insert('end', self.result)
        self.proverka = True

    def ymnozit(self):
        if self.operation:
            self.first_number = float(entry.get())
            entry.delete(0, tkinter.END)
            self.proverka = True
        self.operation = False
        self.znak = "*"

    def delit(self):
        if self.operation:
            self.first_number = float(entry.get())
            entry.delete(0, tkinter.END)
            self.proverka = True
        self.operation = False
        self.znak = "/"

    def stepan(self):
        if self.operation:
            self.first_number = float(entry.get())
            entry.delete(0, tkinter.END)
            self.proverka = True
        self.operation = False
        self.znak = "^"   

# Создание экземпляра калькулятора
app = Calculator()

# Создание кнопок
b7 = tkinter.Button(root, text="7", height=3, width=16, command=lambda: app.kalkulator("7"))
b7.grid(column=0, row=1)
b8 = tkinter.Button(root, text="8", height=3, width=16, command=lambda: app.kalkulator("8"))
b8.grid(column=1, row=1)
b9 = tkinter.Button(root, text="9", height=3, width=16, command=lambda: app.kalkulator("9"))
b9.grid(column=2, row=1)

b4 = tkinter.Button(root, text="4", height=3, width=16, command=lambda: app.kalkulator("4"))
b4.grid(column=0, row=2)
b5 = tkinter.Button(root, text="5", height=3, width=16, command=lambda: app.kalkulator("5"))
b5.grid(column=1, row=2)
b6 = tkinter.Button(root, text="6", height=3, width=16, command=lambda: app.kalkulator("6"))
b6.grid(column=2, row=2)

b1 = tkinter.Button(root, text="1", height=3, width=16, command=lambda: app.kalkulator("1"))
b1.grid(column=0, row=3)
b2 = tkinter.Button(root, text="2", height=3, width=16, command=lambda: app.kalkulator("2"))
b2.grid(column=1, row=3)
b3 = tkinter.Button(root, text="3", height=3, width=16, command=lambda: app.kalkulator("3"))
b3.grid(column=2, row=3)

b0 = tkinter.Button(root, text="0", height=3, width=16, command=lambda: app.kalkulator("0"))
b0.grid(column=0, row=4)


# Кнопки операций
b_delete = tkinter.Button(root, text="delete", height=3, width=16, command=app.numb_clear)
b_delete.grid(column=3, row=1)

b_delenie = tkinter.Button(root, text="/", height=3, width=16, command=app.delit)
b_delenie.grid(column=3, row=2)

b_ymnozenie = tkinter.Button(root, text="*", height=3, width=16, command=app.ymnozit)
b_ymnozenie.grid(column=3, row=3)

b_minus = tkinter.Button(root, text="-", height=3, width=16, command=app.minecraft)
b_minus.grid(column=1, row=4)

b_plus = tkinter.Button(root, text="+", height=3, width=16, command=app.plusik)
b_plus.grid(column=2, row=4)

b_enter = tkinter.Button(root, text="=", height=3, width=16, command=app.ravno)
b_enter.grid(column=3, row=5)

b_stepen = tkinter.Button(root, text="^", height=3, width=16, command=app.stepan)
b_stepen.grid(column=3, row=4)

root.mainloop()