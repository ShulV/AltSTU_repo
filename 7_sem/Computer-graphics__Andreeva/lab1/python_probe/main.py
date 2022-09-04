from tkinter import *


class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.setUI()
        self.brush_size = 10
        self.brush_color = "black"
        self.canv.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.brush_color, outline=self.brush_color)

    def setUI(self):
        self.parent.title("Pythonicway PyPaint")  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне

        self.columnconfigure(6,
                             weight=1)  # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
        self.rowconfigure(2, weight=1)  # То же самое для третьего ряда

        self.canv = Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5,
                       sticky=E + W + S + N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна

        color_lab = Label(self, text="Color: ")  # Создаем метку для кнопок изменения цвета кисти
        color_lab.grid(row=0, column=0,
                       padx=6)  # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

        red_btn = Button(self, text="Red",
                         width=10)  # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов)
        red_btn.grid(row=0, column=1)  # Устанавливаем кнопку первый ряд, вторая колонка

        # Создание остальных кнопок повторяет ту же логику, что и создание
        # кнопки установки красного цвета, отличаются лишь аргументы.

        green_btn = Button(self, text="Green", width=10)
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Blue", width=10)
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, text="Black", width=10)
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, text="White", width=10)
        white_btn.grid(row=0, column=5)

        size_lab = Label(self, text="Brush size: ")  # Создаем метку для кнопок изменения размера кисти
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="Two", width=10)
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="Five", width=10)
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="Seven", width=10)
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="Ten", width=10)
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="Twenty", width=10)
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="Fifty", width=10)
        twenty_btn.grid(row=1, column=6, sticky=W)


def main():
    root = Tk()
    root.geometry("1920x1080+300+300")
    app = Paint(root)
    root.mainloop()


if __name__ == "__main__":
    main()
