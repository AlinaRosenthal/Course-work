from tkinter import *
from tkinter import ttk
from math import *

# Класс для расчёта различных геометрических параметров
class GeometryCalculator:
    @staticmethod
    def area_square(side):
        return side ** 2

    @staticmethod
    def perimeter_square(side):
        return 4 * side

    @staticmethod
    def area_rectangle(side1, side2):
        return side1 * side2

    @staticmethod
    def perimeter_rectangle(side1, side2):
        return 2 * (side1 + side2)

    @staticmethod
    def area_parallelogram1(side, height):
        return side * height

    @staticmethod
    def area_parallelogram2(side1, side2, angle):
        return side1 * side2 * sin(radians(angle))

    @staticmethod
    def perimeter_parallelogram(side1, side2):
        return 2 * (side1 + side2)

    @staticmethod
    def area_rhomb1(side, height):
        return side * height

    @staticmethod
    def area_rhomb2(side, angle):
        return side ** 2 * sin(radians(angle))

    @staticmethod
    def area_rhomb3(diagonal1, diagonal2):
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def perimeter_rhomb(side):
        return 4 * side

    @staticmethod
    def area_isosceles_trapezoid(side1, side2, height):
        return ((side1 + side2)/2) * height

    @staticmethod
    def perimeter_isosceles_trapezoid(side1, side2, side3):
        return side1 + side2 + 2 * side3

    @staticmethod
    def area_triangle1(side, height):
        return 0.5 * side * height

    @staticmethod
    def area_triangle2(side1, side2, angle):
        return 0.5 * side1 * side2 * sin(radians(angle))

    @staticmethod
    def area_triangle3(side1, side2, side3):
        p = (side1 + side2 + side3)/2
        return sqrt(p * (p - side1) * (p - side2) * (p - side3))

    @staticmethod
    def perimeter_triangle(side1, side2, side3):
        return side1 + side2 + side3

    @staticmethod
    def area_circle(radius):
        return pi * radius ** 2

    @staticmethod
    def perimeter_circle(radius):
        return 2 * pi * radius

    @staticmethod
    def volume_cube(side):
        return side ** 3

    @staticmethod
    def surface_area_cube(side):
        return 6 * side ** 2

    @staticmethod
    def volume_rectangular_parallelepiped(length, width, height):
        return length * width * height

    @staticmethod
    def surface_area_rectangular_parallelepiped(length, width, height):
        return 2 * (length * width + length * height + width * height)

    @staticmethod
    def volume_cylinder(radius, height):
        return pi * radius ** 2 * height

    @staticmethod
    def surface_area_cylinder(radius, height):
        return 2 * pi * radius * (radius + height)

    @staticmethod
    def volume_cone(radius, height):
        return (1/3) * pi * radius ** 2 * height

    @staticmethod
    def surface_area_cone(radius, height):
        generatrix = sqrt(radius ** 2 + height ** 2)
        return pi * radius * (generatrix + radius)

    @staticmethod
    def volume_sphere(radius):
        return (4/3) * pi * radius ** 3

    @staticmethod
    def surface_area_sphere(radius):
        return 4 * pi * radius ** 2

# Класс для создания графического интерфейса приложения
class GeometryApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Geometry calculator")
        self.root.geometry('500x400')

        # Создание фрейма, в котором будут размещаться виджеты
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        # Инициализация главного меню
        self.create_main_menu()

        #Выбранная фигура (2D или 3D)
        self.figure = None

        #Виджеты для выбора фигур
        self.figures_2d_menu = None
        self.figures_3d_menu = None

        #Поля для ввода данных
        self.input_fields = {}

    # Метод для создания главного меню
    def create_main_menu(self):

        for widget in self.frm.winfo_children():
            widget.destroy()

        label = ttk.Label(self.frm, text="Выберите тип фигуры")
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        button2d = ttk.Button(self.frm, text="Двумерная (на плоскости)", command=self.show_2d)
        button2d.grid(row=1, column=0, padx=10, pady=10)
        button3d = ttk.Button(self.frm, text="Трёхмерная (в пространстве)", command=self.show_3d)
        button3d.grid(row=1, column=1, padx=10, pady=10)

    # Метод для отображения выбора двумерных фигур
    def show_2d(self):
        for widget in self.frm.winfo_children():
            widget.destroy()

        label2d = ttk.Label(self.frm, text="Выберите двумерную фигуру")
        label2d.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        figures_2d = ["Квадрат", "Прямоугольник", "Параллелограмм", "Ромб", "Равнобедренная трапеция", "Треугольник", "Круг"]
        self.figures_2d_menu = ttk.Combobox(self.frm, values=figures_2d, width = 30)
        self.figures_2d_menu.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        self.figures_2d_menu.current(0)

        # Кнопки координации "Дальше" и "Вперёд"
        button_next = ttk.Button(self.frm, text="Дальше", command=self.show_2d_input)
        button_next.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        button_back = ttk.Button(self.frm, text="Назад", command=self.create_main_menu)
        button_back.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

    # Метод для отображения выбора трёхмерных фигур
    def show_3d(self):
        for widget in self.frm.winfo_children():
            widget.destroy()

        label3d = ttk.Label(self.frm, text="Выберите трёхмерную фигуру")
        label3d.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        figures_3d = ["Куб", "Прямоугольный параллелепипед", "Цилиндр", "Конус", "Шар"]
        self.figures_3d_menu = ttk.Combobox(self.frm, values=figures_3d, width = 30)
        self.figures_3d_menu.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        self.figures_3d_menu.current(0)

        # Кнопки координации "Дальше" и "Вперёд"
        button_next = ttk.Button(self.frm, text="Дальше", command=self.show_3d_input)
        button_next.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        button_back = ttk.Button(self.frm, text="Назад", command=self.create_main_menu)
        button_back.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

    # Метод для отображения полей ввода данных для двумерных фигур
    def show_2d_input(self):
        self.figure = self.figures_2d_menu.get()

        for widget in self.frm.winfo_children():
            widget.destroy()

        label_input = ttk.Label(self.frm, text=f"Введите параметры для {self.figure}")
        label_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.input_fields = {}
        if self.figure == "Квадрат":
            ttk.Label(self.frm, text="Длина стороны: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["side"] = ttk.Entry(self.frm)
            self.input_fields["side"].grid(row=1, column=1, padx=10, pady=10)

        elif self.figure == "Прямоугольник":
            ttk.Label(self.frm, text="Длина: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["side1"] = ttk.Entry(self.frm)
            self.input_fields["side1"].grid(row=1, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Ширина: ").grid(row=2, column=0, padx=10, pady=10)
            self.input_fields["side2"] = ttk.Entry(self.frm)
            self.input_fields["side2"].grid(row=2, column=1, padx=10, pady=10)

        elif self.figure == "Параллелограмм":
            ttk.Label(self.frm, text="Длина стороны: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["side"] = ttk.Entry(self.frm)
            self.input_fields["side"].grid(row=1, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Длина высоты к этой стороне: ").grid(row=2, column=0, padx=10, pady=10)
            self.input_fields["height"] = ttk.Entry(self.frm)
            self.input_fields["height"].grid(row=2, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Длина второй стороны: ").grid(row=3, column=0, padx=10, pady=10)
            self.input_fields["side2"] = ttk.Entry(self.frm)
            self.input_fields["side2"].grid(row=3, column=1, padx=10, pady=10)

        elif self.figure == "Ромб":
            ttk.Label(self.frm, text="Длина стороны: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["side"] = ttk.Entry(self.frm)
            self.input_fields["side"].grid(row=1, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Длина высоты к этой стороне: ").grid(row=2, column=0, padx=10, pady=10)
            self.input_fields["height"] = ttk.Entry(self.frm)
            self.input_fields["height"].grid(row=2, column=1, padx=10, pady=10)

        elif self.figure == "Равнобедренная трапеция":
            ttk.Label(self.frm, text="Длина первого основания: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["side1"] = ttk.Entry(self.frm)
            self.input_fields["side1"].grid(row=1, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Длина второго основания: ").grid(row=2, column=0, padx=10, pady=10)
            self.input_fields["side2"] = ttk.Entry(self.frm)
            self.input_fields["side2"].grid(row=2, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Длина боковой стороны: ").grid(row=3, column=0, padx=10, pady=10)
            self.input_fields["side3"] = ttk.Entry(self.frm)
            self.input_fields["side3"].grid(row=3, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Длина высоты: ").grid(row=4, column=0, padx=10, pady=10)
            self.input_fields["height"] = ttk.Entry(self.frm)
            self.input_fields["height"].grid(row=4, column=1, padx=10, pady=10)

        elif self.figure == "Треугольник":
            ttk.Label(self.frm, text="Длина первой стороны: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["side1"] = ttk.Entry(self.frm)
            self.input_fields["side1"].grid(row=1, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Длина второй стороны: ").grid(row=2, column=0, padx=10, pady=10)
            self.input_fields["side2"] = ttk.Entry(self.frm)
            self.input_fields["side2"].grid(row=2, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Длина третьей стороны: ").grid(row=3, column=0, padx=10, pady=10)
            self.input_fields["side3"] = ttk.Entry(self.frm)
            self.input_fields["side3"].grid(row=3, column=1, padx=10, pady=10)

        elif self.figure == "Круг":
            ttk.Label(self.frm, text="Радиус: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["radius"] = ttk.Entry(self.frm)
            self.input_fields["radius"].grid(row=1, column=1, padx=10, pady=10)

        button_calculate = ttk.Button(self.frm, text="Рассчитать", command=lambda: self.calculate(self.figure))
        button_calculate.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        button_back = ttk.Button(self.frm, text="Назад", command=self.show_2d)
        button_back.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        button_main = ttk.Button(self.frm, text="На главную", command=self.create_main_menu)
        button_main.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Метод для отображения полей ввода данных для трёхмерных фигур
    def show_3d_input(self):
        self.figure = self.figures_3d_menu.get()

        for widget in self.frm.winfo_children():
            widget.destroy()

        label_input = ttk.Label(self.frm, text=f"Введите параметры для {self.figure}")
        label_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.input_fields = {}

        if self.figure == "Куб":
            ttk.Label(self.frm, text="Длина стороны: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["side"] = ttk.Entry(self.frm)
            self.input_fields["side"].grid(row=1, column=1, padx=10, pady=10)

        elif self.figure == "Прямоугольный параллелепипед":
            ttk.Label(self.frm, text="Длина: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["length"] = ttk.Entry(self.frm)
            self.input_fields["length"].grid(row=1, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Ширина: ").grid(row=2, column=0, padx=10, pady=10)
            self.input_fields["width"] = ttk.Entry(self.frm)
            self.input_fields["width"].grid(row=2, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Высота: ").grid(row=3, column=0, padx=10, pady=10)
            self.input_fields["height"] = ttk.Entry(self.frm)
            self.input_fields["height"].grid(row=3, column=1, padx=10, pady=10)

        elif self.figure == "Цилиндр":
            ttk.Label(self.frm, text="Радиус: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["radius"] = ttk.Entry(self.frm)
            self.input_fields["radius"].grid(row=1, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Высота: ").grid(row=2, column=0, padx=10, pady=10)
            self.input_fields["height"] = ttk.Entry(self.frm)
            self.input_fields["height"].grid(row=2, column=1, padx=10, pady=10)

        elif self.figure == "Конус":
            ttk.Label(self.frm, text="Радиус: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["radius"] = ttk.Entry(self.frm)
            self.input_fields["radius"].grid(row=1, column=1, padx=10, pady=10)

            ttk.Label(self.frm, text="Высота: ").grid(row=2, column=0, padx=10, pady=10)
            self.input_fields["height"] = ttk.Entry(self.frm)
            self.input_fields["height"].grid(row=2, column=1, padx=10, pady=10)

        elif self.figure == "Шар":
            ttk.Label(self.frm, text="Радиус: ").grid(row=1, column=0, padx=10, pady=10)
            self.input_fields["radius"] = ttk.Entry(self.frm)
            self.input_fields["radius"].grid(row=1, column=1, padx=10, pady=10)

        button_calculate = ttk.Button(self.frm, text="Рассчитать", command=lambda: self.calculate(self.figure))
        button_calculate.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        button_back = ttk.Button(self.frm, text="Назад", command=self.show_3d)
        button_back.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        button_main = ttk.Button(self.frm, text="На главную", command=self.create_main_menu)
        button_main.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Метод для расчёта параметров выбранных фигур с использованием введённых данных
    def calculate(self, figure):
        try:
            # Получение введённых данных
            inputs = {key: float(entry.get()) for key, entry in self.input_fields.items()}
        except ValueError:
            # Обработка ошибки преобразования данных
            for widget in self.frm.winfo_children():
                if isinstance(widget, ttk.Label) and widget.grid_info()["row"] >= 8:
                    widget.destroy()
            ttk.Label(self.frm, text="Ошибка: Введены некорректные данные (ожидалось число).").grid(row=9, column=0,columnspan=2, padx=10, pady=10)
            return

        try:
            for key, value in inputs.items():
                if value <= 0:
                    raise ValueError("Все числа должны быть положительными")

            result = None

            # Расчёты для выбранной фигуры
            if figure == "Квадрат":
                area = GeometryCalculator.area_square(inputs["side"])
                perimeter = GeometryCalculator.perimeter_square(inputs["side"])
                result = f"Площадь: {area:.2f}\nПериметр: {perimeter:.2f}"
            elif figure == "Прямоугольник":
                area = GeometryCalculator.area_rectangle(inputs["side1"], inputs["side2"])
                perimeter = GeometryCalculator.perimeter_rectangle(inputs["side1"], inputs["side2"])
                result = f"Площадь: {area:.2f}\nПериметр: {perimeter:.2f}"
            elif figure == "Параллелограмм":
                area = GeometryCalculator.area_parallelogram1(inputs["side"], inputs["height"])
                perimeter = GeometryCalculator.perimeter_parallelogram(inputs["side"], inputs["side2"])
                result = f"Площадь: {area:.2f}\nПериметр: {perimeter:.2f}"
            elif figure == "Ромб":
                area = GeometryCalculator.area_rhomb1(inputs["side"], inputs["height"])
                perimeter = GeometryCalculator.perimeter_rhomb(inputs["side"])
                result = f"Площадь: {area:.2f}\nПериметр: {perimeter:.2f}"
            elif figure == "Равнобедренная трапеция":
                area = GeometryCalculator.area_isosceles_trapezoid(inputs["side1"], inputs["side2"], inputs["height"])
                perimeter = GeometryCalculator.perimeter_isosceles_trapezoid(inputs["side1"], inputs["side2"], inputs["side3"])
                result = f"Площадь: {area:.2f}\nПериметр: {perimeter:.2f}"
            elif figure == "Треугольник":
                area = GeometryCalculator.area_triangle3(inputs["side1"], inputs["side2"], inputs["side3"])
                perimeter = GeometryCalculator.perimeter_triangle(inputs["side1"], inputs["side2"], inputs["side3"])
                result = f"Площадь: {area:.2f}\nПериметр: {perimeter:.2f}"
            elif figure == "Круг":
                area = GeometryCalculator.area_circle(inputs["radius"])
                perimeter = GeometryCalculator.perimeter_circle(inputs["radius"])
                result = f"Площадь: {area:.2f}\nПериметр: {perimeter:.2f}"
            elif figure == "Куб":
                volume = GeometryCalculator.volume_cube(inputs["side"])
                surface_area = GeometryCalculator.surface_area_cube(inputs["side"])
                result = f"Объём: {volume:.2f}\nПлощадь полной поверхности: {surface_area:.2f}"
            elif figure == "Прямоугольный параллелепипед":
                volume = GeometryCalculator.volume_rectangular_parallelepiped(inputs["length"], inputs["width"], inputs["height"])
                surface_area = GeometryCalculator.surface_area_rectangular_parallelepiped(inputs["length"], inputs["width"], inputs["height"])
                result = f"Объём: {volume:.2f}\nПлощадь полной поверхности: {surface_area:.2f}"
            elif figure == "Цилиндр":
                volume = GeometryCalculator.volume_cylinder(inputs["radius"], inputs["height"])
                surface_area = GeometryCalculator.surface_area_cylinder(inputs["radius"], inputs["height"])
                result = f"Объём: {volume:.2f}\nПлощадь полной поверхности: {surface_area:.2f}"
            elif figure == "Конус":
                volume = GeometryCalculator.volume_cone(inputs["radius"], inputs["height"])
                surface_area = GeometryCalculator.surface_area_cone(inputs["radius"], inputs["height"])
                result = f"Объём: {volume:.2f}\nПлощадь полной поверхности: {surface_area:.2f}"
            elif figure == "Шар":
                volume = GeometryCalculator.volume_sphere(inputs["radius"])
                surface_area = GeometryCalculator.surface_area_sphere(inputs["radius"])
                result = f"Объём: {volume:.2f}\nПлощадь полной поверхности: {surface_area:.2f}"

            for widget in self.frm.winfo_children():
                if isinstance(widget, ttk.Label) and widget.grid_info()["row"] >= 8:
                    widget.destroy()

            # Отображение результатов расчёта
            ttk.Label(self.frm, text=result).grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # Обработка ошибки
        except ValueError as e:
            # Обработка ошибки (например, отрицательные числа)
            for widget in self.frm.winfo_children():
                if isinstance(widget, ttk.Label) and widget.grid_info()["row"] >= 8:
                    widget.destroy()
            ttk.Label(self.frm, text=f"Ошибка: {str(e)}").grid(row=9, column=0, columnspan=2, padx=10, pady=10)

# Основной блок программы
if __name__ == "__main__":
    window = Tk()
    app = GeometryApp(window)
    window.mainloop()
