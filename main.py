from tkinter import ttk, Tk, Canvas
from abc import ABC
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
        if angle <= 0 or angle >= 180:
            raise ValueError("Угол должен быть больше 0 и меньше 180 градусов")
        return side1 * side2 * sin(radians(angle))

    @staticmethod
    def perimeter_parallelogram(side1, side2):
        return 2 * (side1 + side2)

    @staticmethod
    def area_rhomb1(side, height):
        return side * height

    @staticmethod
    def area_rhomb2(side, angle):
        if angle <= 0 or angle >= 180:
            raise ValueError("Угол должен быть больше 0 и меньше 180 градусов")
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
    def perimeter_isosceles_trapezoid(side1, side2, height):
        return side1 + side2 + 2 * sqrt((abs(side1-side2)/2)**2 + height**2)

    @staticmethod
    def area_triangle1(side, height):
        return 0.5 * side * height

    @staticmethod
    def area_triangle2(side1, side2, angle):
        if angle <= 0 or angle >= 180:
            raise ValueError("Угол должен быть больше 0 и меньше 180 градусов")
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

class Figure(ABC):
    def __init__(self):
        self.input_fields = {}

    def area(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass

    def surface_area(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return GeometryCalculator.area_square(self.side)

    def perimeter(self):
        return GeometryCalculator.perimeter_square(self.side)

class Rectangle(Figure):
    def __init__(self, side1=None, side2=None):
        self.side1 = side1
        self.side2 = side2

    def area(self, method=None):
        return GeometryCalculator.area_rectangle(self.side1, self.side2)

    def perimeter(self, method=None):
        return GeometryCalculator.perimeter_rectangle(self.side1, self.side2)

class Parallelogram(Figure):
    Methods = {"По двум сторонам и углу между ними": ["side1", "side2", "angle"],
               "По стороне и высоте к ней": ["side1", "height"]}

    def __init__(self, params=None):
        self.params = params or {}

    def area(self, method):
        if method == "По стороне и высоте к ней":
            return GeometryCalculator.area_parallelogram1(self.params["side1"], self.params["height"])
        elif method == "По двум сторонам и углу между ними":
            return GeometryCalculator.area_parallelogram2(self.params["side1"], self.params["side2"], self.params["angle"])
        else:
            raise ValueError("Недостаточно данных для выбранного метода расчёта")

    def perimeter(self, method):
        if method == "По двум сторонам и углу между ними":
            return GeometryCalculator.perimeter_parallelogram(self.params["side1"], self.params["side2"])
        raise ValueError("Недостаточно данных для выбранного метода расчёта")

class Rhomb(Figure):
    Methods = {"По сторонам и углу между ними": ["side", "angle"],
               "По стороне и высоте": ["side", "height"],
               "По диагоналям": ["diagonal1", "diagonal2"]}

    def __init__(self, params=None):
        self.params = params or {}

    def area(self, method):
        if method == "По стороне и высоте":
            return GeometryCalculator.area_rhomb1(self.params["side"], self.params["height"])
        elif method == "По сторонам и углу между ними":
            return GeometryCalculator.area_rhomb2(self.params["side"], self.params["angle"])
        elif method == "По диагоналям":
            return GeometryCalculator.area_rhomb3(self.params["diagonal1"], self.params["diagonal2"])
        else:
            raise ValueError("Недостаточно данных для выбранного метода расчёта")

    def perimeter(self, method):
        if method == "По стороне и высоте":
            return GeometryCalculator.perimeter_rhomb(self.params["side"])
        elif method == "По сторонам и углу между ними":
            return GeometryCalculator.perimeter_rhomb(self.params["side"])
        raise ValueError("Недостаточно данных для выбранного метода расчёта")

class IsoscelesTrapezoid(Figure):
    def __init__(self, side1, side2, height):
        self.side1 = side1
        self.side2 = side2
        self.height = height

    def area(self, method=None):
        return GeometryCalculator.area_isosceles_trapezoid(self.side1, self.side2, self.height)

    def perimeter(self, method=None):
        return GeometryCalculator.perimeter_isosceles_trapezoid(self.side1, self.side2, self.height)

class Triangle(Figure):
    Methods = {"По трём сторонам": ["side1", "side2", "side3"],
               "По стороне и высоте": ["side1", "height"],
               "По двум сторонам и углу между ними": ["side1", "side2", "angle"]}

    def __init__(self, params =None):
        self.params = params or {}

    def area(self, method):
        if method == "По стороне и высоте":
            return GeometryCalculator.area_triangle1(self.params["side1"], self.params["height"])
        elif method == "По двум сторонам и углу между ними":
            return GeometryCalculator.area_triangle2(self.params["side1"], self.params["side2"], self.params["angle"])
        elif method == "По трём сторонам":
            if ((self.params["side1"] + self.params["side2"] <= self.params["side3"]) or
                    (self.params["side1"] + self.params["side3"] <= self.params["side2"]) or
                    (self.params["side2"] + self.params["side3"] <= self.params["side1"])):
                raise ValueError("Такого треугольника не существует")
            return GeometryCalculator.area_triangle3(self.params["side1"], self.params["side2"], self.params["side3"])
        raise ValueError("Недостаточно данных для выбранного метода расчёта")

    def perimeter(self, method):
        if method == "По трём сторонам":
            return GeometryCalculator.perimeter_triangle(self.params["side1"], self.params["side2"], self.params["side3"])
        raise ValueError("Недостаточно данных для выбранного метода расчёта")

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self, method=None):
        return GeometryCalculator.area_circle(self.radius)

    def perimeter(self, method=None):
        return GeometryCalculator.perimeter_circle(self.radius)

class Cube(Figure):
    def __init__(self, side):
        self.side = side

    def volume(self, method=None):
        return GeometryCalculator.volume_cube(self.side)

    def surface_area(self, method=None):
        return GeometryCalculator.surface_area_cube(self.side)

class RectangularParallelepiped(Figure):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self, method=None):
        return GeometryCalculator.volume_rectangular_parallelepiped(self.length, self.width, self.height)

    def surface_area(self, method=None):
        return GeometryCalculator.surface_area_rectangular_parallelepiped(self.length, self.width, self.height)

class Cylinder(Figure):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self, method=None):
        return GeometryCalculator.volume_cylinder(self.radius, self.height)

    def surface_area(self, method=None):
        return GeometryCalculator.surface_area_cylinder(self.radius,self.height)

class Cone(Figure):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self, method=None):
        return GeometryCalculator.volume_cone(self.radius, self.height)

    def surface_area(self, method=None):
        return GeometryCalculator.surface_area_cone(self.radius, self.height)

class Sphere(Figure):
    def __init__(self, radius):
        self.radius = radius

    def volume(self, method=None):
        return GeometryCalculator.volume_sphere(self.radius)

    def surface_area(self, method=None):
        return GeometryCalculator.surface_area_sphere(self.radius)


# Класс для создания графического интерфейса приложения
class GeometryApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Geometry Calculator Pro")
        self.root.geometry('1100x750')
        self.root.configure(bg='#cfd2ff')

        # Настройка стилей для виджетов
        self.setup_styles()

        # Создание фреймов со стилями
        self.frm = ttk.Frame(self.root, padding=15, style='Card.TFrame')
        self.frm.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.canvas_frame = ttk.Frame(self.root, padding=15, style='Card.TFrame')
        self.canvas_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.root.columnconfigure(0, weight=2)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(0, weight=1)

        self.canvas = Canvas(self.canvas_frame, width=500, height=600, bg='white', highlightthickness=0, bd=0)
        self.canvas.pack(fill='both', expand=True)

        # Инициализация главного меню
        self.create_main_menu()

        #Выбранная фигура (2D или 3D)
        self.figure = None

        #Виджеты для выбора фигур
        self.figures_2d_menu = None
        self.figures_3d_menu = None

        #Поля для ввода данных
        self.input_fields = {}

    def setup_styles(self):
        style = ttk.Style()

        style.theme_use('alt')

        # Стиль для карточек (фреймов)
        style.configure('Card.TFrame',
                        background='white',
                        borderwidth=2,
                        relief='groove',
                        bordercolor='#e0e0e0')

        # Стиль для кнопок
        style.configure('TButton',
                        font=('Helvetica', 10, 'bold'),
                        foreground='white',
                        background='#6369cb',
                        borderwidth=1,
                        relief='raised',
                        padding=8)
        style.map('TButton', background=[('active', '#3e43a2'), ('disabled', '#cccccc')])

        # Стиль для меток
        style.configure('TLabel',
                        font=('Helvetica', 10),
                        background='white',
                        foreground='#333333')

        # Стиль для заголовков
        style.configure('Title.TLabel',
                        font=('Helvetica', 12, 'bold'),
                        foreground='#2a5885')

        # Стиль для полей ввода
        style.configure('TEntry',
                        fieldbackground='white',
                        bordercolor='#cccccc',
                        lightcolor='#cccccc',
                        darkcolor='#cccccc',
                        padding=5)

        # Стиль для Combobox
        style.configure('TCombobox',
                        fieldbackground='white',
                        selectbackground='#e0e0e0',
                        padding=5)

    def create_label(self, text, row, column, columnspan=1, style='TLabel'):
        label = ttk.Label(self.frm, text=text, style=style)
        label.grid(row=row, column=column, columnspan=columnspan,
                 padx=5, pady=8, sticky='w')
        return label

    def create_button(self, text, command, row, column, columnspan=1):
        button = ttk.Button(self.frm, text=text, command=command)
        button.grid(row=row, column=column, columnspan=columnspan,
                  padx=5, pady=8, ipadx=10, ipady=5, sticky='ew')
        return button

    def create_input_fields(self, text, row, field_name):
        self.create_label(text, row, 0)

        entry = ttk.Entry(self.frm, font=('Helvetica', 10))
        entry.grid(row=row, column=1, padx=5, pady=5, sticky='ew')

        self.input_fields[field_name] = entry
        return entry

    def clear_canvas(self):
        self.canvas.delete("all")

    # Методы для визуализации фигур
    def draw_square(self, side):
        self.clear_canvas()
        scale = max(50/side, 1) if side < 50 else 200/side
        size = side * scale
        x = (600 - size) / 2
        y = (400 - size) / 2
        self.canvas.create_rectangle(x, y, x + size, y + size, outline='blue', width=2, fill='lightblue')
        self.canvas.create_text(x + size / 2, y - 20, text=f"Сторона: {side:.1f}", fill="black")

    def draw_rectangle(self, width, height):
        self.clear_canvas()
        max_dim = max(width, height)
        scale = max(50/max_dim, 1) if max_dim < 50 else 200/max_dim
        w = width * scale
        h = height * scale
        x = (600 - w) / 2
        y = (400 - h) / 2
        self.canvas.create_rectangle(x, y, x + w, y + h, outline='blue', width=2, fill='lightblue')
        self.canvas.create_text(x + w / 2, y - 20, text=f"Длина: {width:.1f}", fill="black")
        self.canvas.create_text(x - 50, y + h / 2, text=f"Ширина: {height:.1f}", fill="black", angle=90)

    def draw_parallelogram(self, side, height=None, method=None, angle=None, side2=None):
        self.clear_canvas()

        x_center, y_center = 100, 400
        label_offset = 10

        if method == "По стороне и высоте к ней":
            max_dim = max(side, height)
            scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim
            a = side * scale
            h = height * scale

            x1 = x_center + a
            y1 = y_center
            x2 = x1 + 0.3 * a
            y2 = y1 - h
            x3 = x_center + 0.3 * a
            y3 = y_center - h

            self.canvas.create_polygon(
                x_center, y_center,
                x1, y1,
                x2, y2,
                x3, y3,
                outline='blue', width=2, fill='lightblue'
            )

            self.canvas.create_line(
                x_center, y_center,
                x_center, y_center - h,
                fill='red', width=1, dash=(4, 2)
            )

            self.canvas.create_text(
                (x_center + x1) / 2, (y_center + y1) / 2 + label_offset,
                text=f"a = {side:.1f}",
                fill="black",
                font=('Arial', 10)
            )

            self.canvas.create_text(
                x_center - label_offset, (y_center + y3) / 2,
                text=f"h = {height:.1f}",
                fill="red",
                font=('Arial', 10)
            )

        elif method == "По двум сторонам и углу между ними" and (angle <= 0 or angle >= 180):
            self.canvas.create_text(250, 200, text="Недопустимый угол. Уго должен быть меньше 180° и больше 0°", fill="red")

        elif method == "По двум сторонам и углу между ними":
            max_dim = max(side, side2)
            scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim
            a = side * scale
            b = side2 * scale
            angle_rad = radians(angle)
            x1 = x_center + a
            y1 = y_center
            x2 = x1 + b * cos(angle_rad)
            y2 = y1 - b * sin(angle_rad)
            x3 = x_center + b * cos(angle_rad)
            y3 = y_center - b * sin(angle_rad)

            self.canvas.create_polygon(
                x_center, y_center,
                x1, y1,
                x2, y2,
                x3, y3,
                outline='blue', width=2, fill='lightblue'
            )

            self.canvas.create_text(
                (x_center + x1) / 2, y_center + label_offset,
                text=f"a = {side:.1f}",
                fill="black",
                font=('Arial', 10)
            )

            mid_x = (x_center + x3) / 2
            mid_y = (y_center + y3) / 2
            label_x = mid_x - label_offset * sin(angle_rad)
            label_y = mid_y - label_offset * cos(angle_rad)

            self.canvas.create_text(
                label_x, label_y,
                text=f"b = {side2:.1f}",
                fill="black",
                font=('Arial', 10),
                angle=degrees(angle_rad)
            )

            angle_label_x = x_center - label_offset * 0.7
            angle_label_y = y_center + label_offset * 0.7
            self.canvas.create_text(
                angle_label_x, angle_label_y,
                text=f"{angle}°",
                fill="black",
                font=('Arial', 10)
            )

    def draw_rhomb(self, method, side=None, height=None, angle=None, d1=None, d2=None):
        self.clear_canvas()

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_center, y_center = canvas_width // 2, canvas_height // 2
        label_offset = 15

        if method == "По стороне и высоте":
            max_dim = max(side, height)
            scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim
            a_scaled = side * scale
            h_scaled = height * scale

            x1 = x_center + a_scaled / 2
            y1 = y_center
            x2 = x_center
            y2 = y_center - h_scaled / 2
            x3 = x_center - a_scaled / 2
            y3 = y_center
            x4 = x_center
            y4 = y_center + h_scaled / 2

            self.canvas.create_polygon(
                x1, y1,
                x2, y2,
                x3, y3,
                x4, y4,
                outline='blue', width=2, fill='lightblue'
            )

            self.canvas.create_text(
                (x_center + x1) / 2, y_center + label_offset,
                text=f"a = {side:.1f}",
                fill="black",
                font=('Arial', 10)
            )

            self.canvas.create_text(
                x_center + label_offset, (y_center + y2) / 2,
                text=f"h = {height:.1f}",
                fill="red",
                font=('Arial', 10)
            )

        elif method == "По сторонам и углу между ними" and (angle <= 0 or angle >= 180):
            self.canvas.create_text(250, 200, text="Недопустимый угол. Уго должен быть меньше 180° и больше 0°", fill="red")

        elif method == "По сторонам и углу между ними":
            angle_rad = radians(angle)
            points = [
                (0, 0),
                (side, 0),
                (side + side * cos(angle_rad), -side * sin(angle_rad)),
                (side * cos(angle_rad), -side * sin(angle_rad))
            ]

            min_x = min(p[0] for p in points)
            max_x = max(p[0] for p in points)
            min_y = min(p[1] for p in points)
            max_y = max(p[1] for p in points)

            rhomb_width = max_x - min_x
            rhomb_height = max_y - min_y

            available_width = canvas_width - 100
            available_height = canvas_height - 100
            width_scale = available_width / rhomb_width
            height_scale = available_height / rhomb_height
            scale = min(width_scale, height_scale) * 0.9
            scale = max(min(scale, 2.0), 0.5)
            scaled_points = [
                (x_center + (p[0] - (min_x + max_x) / 2) * scale,
                 y_center + (p[1] - (min_y + max_y) / 2) * scale)
                for p in points
            ]

            self.canvas.create_polygon(
                *[coord for point in scaled_points for coord in point],
                outline='blue', width=2, fill='lightblue'
            )

            mid_side_x = (scaled_points[0][0] + scaled_points[1][0]) / 2
            mid_side_y = (scaled_points[0][1] + scaled_points[1][1]) / 2

            self.canvas.create_text(
                mid_side_x, mid_side_y + label_offset,
                text=f"a = {side:.1f}",
                fill="black",
                font=('Arial', 10)
            )

            angle_label_x = scaled_points[0][0] - label_offset
            angle_label_y = scaled_points[0][1] + label_offset

            self.canvas.create_text(
                angle_label_x, angle_label_y,
                text=f"{angle}°",
                fill="black",
                font=('Arial', 10)

            )

        elif method == "По диагоналям":
            max_dim = max(d1, d2)
            scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim
            d1_scaled = d1 * scale
            d2_scaled = d2 * scale

            x1, y1 = x_center + d1_scaled / 2, y_center
            x2, y2 = x_center, y_center - d2_scaled / 2
            x3, y3 = x_center - d1_scaled / 2, y_center
            x4, y4 = x_center, y_center + d2_scaled / 2

            self.canvas.create_polygon(
                x1, y1,
                x2, y2,
                x3, y3,
                x4, y4,
                outline='blue', width=2, fill='lightblue'
            )

            self.canvas.create_text(
                (x_center + x1) / 2, y_center + label_offset,
                text=f"d1 = {d1:.1f}",
                fill="purple",
                font=('Arial', 10)
            )

            self.canvas.create_text(
                x_center + label_offset, (y_center + y2) / 2,
                text=f"d2 = {d2:.1f}",
                fill="purple",
                font=('Arial', 10)
            )

            side = sqrt(d1 ** 2 + d2 ** 2) / 2
            self.canvas.create_text(
                (x1 + x2) / 1.7 + label_offset * 0.7,
                (y1 + y2) / 2 - label_offset * 0.7,
                text=f"a = {side:.1f}",
                fill="black",
                font=('Arial', 10)
            )

    def draw_isosceles_trapezoid(self, base1, base2, height):
        self.clear_canvas()

        max_dim = max(base1, base2, height)
        scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim
        b1 = base1 * scale
        b2 = base2 * scale
        h = height * scale

        x_center = self.canvas.winfo_width() / 2
        y_center = self.canvas.winfo_height() / 2

        x_top1 = x_center - b1 / 2
        x_top2 = x_center + b1 / 2
        x_bottom1 = x_center - b2 / 2
        x_bottom2 = x_center + b2 / 2

        y_top = y_center - h / 2
        y_bottom = y_center + h / 2

        self.canvas.create_polygon(
            x_bottom1, y_bottom,
            x_bottom2, y_bottom,
            x_top2, y_top,
            x_top1, y_top,
            outline='blue', width=2, fill='lightblue'
        )

        leg = abs(base1 - base2) / 2
        side_length = (leg ** 2 + height ** 2) ** 0.5

        self.canvas.create_text(
            x_center, y_top - 20,
            text=f"Верхнее основание: {base1:.1f}",
            fill="black", font=('Arial', 10)
        )

        self.canvas.create_text(
            x_center, y_bottom + 20,
            text=f"Нижнее основание: {base2:.1f}",
            fill="black", font=('Arial', 10)
        )

        left_side_mid_x = (x_top1 + x_bottom1) / 2 - 20
        left_side_mid_y = (y_top + y_bottom) / 2
        self.canvas.create_text(
            left_side_mid_x, left_side_mid_y,
            text=f"Боковая сторона: {side_length:.1f}",
            fill="black", font=('Arial', 10),
            angle=degrees(atan(height / leg))
        )

        right_side_mid_x = (x_top2 + x_bottom2) / 2 + 20
        right_side_mid_y = (y_top + y_bottom) / 2
        self.canvas.create_text(
            right_side_mid_x, right_side_mid_y,
            text=f"Боковая сторона: {side_length:.1f}",
            fill="black", font=('Arial', 10),
            angle=-degrees(atan(height / leg))
        )

        self.canvas.create_line(
            x_center, y_top,
            x_center, y_bottom,
            fill='red', width=1, dash=(4, 2)
        )
        self.canvas.create_text(
            x_center + 30, y_center,
            text=f"Высота: {height:.1f}",
            fill="red", font=('Arial', 10),
            angle=90
        )

    def draw_triangle(self, method, side1=None, side2=None, side3=None, height=None, angle=None):
        self.clear_canvas()

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x_center, y_center = canvas_width // 2, canvas_height // 2
        label_offset = 15

        if method == "По стороне и высоте":
            max_dim = max(side1, height)
            scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim

            base = side1 * scale
            h = height * scale

            if h > canvas_height - 2 * label_offset:
                scale = (canvas_height - 2 * label_offset) / height
                base = side1 * scale
                h = height * scale

            if base > canvas_width - 2 * label_offset:
                scale = min(scale, (canvas_width - 2 * label_offset) / side1)
                base = side1 * scale
                h = height * scale

            x1, y1 = x_center - base / 2, y_center + h / 2
            x2, y2 = x_center + base / 2, y_center + h / 2
            x3, y3 = x_center, y_center - h / 2

            self.canvas.create_polygon(x1, y1, x2, y2, x3, y3,
                                       outline='blue', width=2, fill='lightblue')

            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2 + label_offset,
                                    text=f"Основание: {side1:.1f}",
                                    fill="black", font=('Arial', 10))
            self.canvas.create_text(x_center, y_center - h / 4,
                                    text=f"Высота: {height:.1f}",
                                    fill="red", font=('Arial', 10))

        elif method == "По двум сторонам и углу между ними" and (angle <= 0 or angle >= 180):
            self.canvas.create_text(250, 200, text="Недопустимый угол. Уго должен быть меньше 180° и больше 0°", fill="red")

        elif method == "По двум сторонам и углу между ними":
            angle_rad = radians(angle)
            max_dim = max(side1, side2)
            scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim

            a = side1 * scale
            b = side2 * scale

            x1, y1 = x_center, y_center
            x2, y2 = x1 + a, y1
            x3, y3 = x1 + b * cos(angle_rad), y1 - b * sin(angle_rad)

            min_x = min(x1, x2, x3)
            max_x = max(x1, x2, x3)
            min_y = min(y1, y2, y3)
            max_y = max(y1, y2, y3)

            if max_x - min_x > canvas_width - 2 * label_offset or max_y - min_y > canvas_height - 2 * label_offset:
                scale_x = (canvas_width - 2 * label_offset) / (max_x - min_x)
                scale_y = (canvas_height - 2 * label_offset) / (max_y - min_y)
                scale *= min(scale_x, scale_y)
                a = side1 * scale
                b = side2 * scale
                x2, y2 = x1 + a, y1
                x3, y3 = x1 + b * cos(angle_rad), y1 - b * sin(angle_rad)

            self.canvas.create_polygon(x1, y1, x2, y2, x3, y3,
                                       outline='blue', width=2, fill='lightblue')

            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2 + label_offset,
                                    text=f"a = {side1:.1f}",
                                    fill="black", font=('Arial', 10))
            self.canvas.create_text((x1 + x3) / 2 - label_offset, (y1 + y3) / 2 - label_offset,
                                    text=f"b = {side2:.1f}",
                                    fill="black", font=('Arial', 10))
            self.canvas.create_text(x1 - label_offset * 1.5, y1 + label_offset * 0.5,
                                    text=f"∠ = {angle}°",
                                    fill="green", font=('Arial', 10, 'bold'))

        elif method == "По трём сторонам":
            a, b, c = side1, side2, side3

            if a + b <= c or a + c <= b or b + c <= a:
                self.canvas.create_text(x_center, y_center,
                                        text="Такого треугольника не существует!",
                                        fill="red", font=('Arial', 14))
                return

            max_dim = max(a, b, c)
            scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim

            x = (a ** 2 + b ** 2 - c ** 2) / (2 * a)
            y = sqrt(b ** 2 - x ** 2)

            x1, y1 = x_center, y_center
            x2, y2 = x1 + a * scale, y1
            x3, y3 = x1 + x * scale, y1 - y * scale

            min_x = min(x1, x2, x3)
            max_x = max(x1, x2, x3)
            min_y = min(y1, y2, y3)
            max_y = max(y1, y2, y3)

            if max_x - min_x > canvas_width - 2 * label_offset or max_y - min_y > canvas_height - 2 * label_offset:
                scale_x = (canvas_width - 2 * label_offset) / (max_x - min_x)
                scale_y = (canvas_height - 2 * label_offset) / (max_y - min_y)
                scale *= min(scale_x, scale_y)
                x2, y2 = x1 + a * scale, y1
                x3, y3 = x1 + x * scale, y1 - y * scale

            self.canvas.create_polygon(x1, y1, x2, y2, x3, y3,
                                       outline='blue', width=2, fill='lightblue')

            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2 + label_offset,
                                    text=f"a = {a:.1f}",
                                    fill="black", font=('Arial', 10))
            self.canvas.create_text((x1 + x3) / 2 - label_offset, (y1 + y3) / 2,
                                    text=f"b = {b:.1f}",
                                    fill="black", font=('Arial', 10))
            self.canvas.create_text((x2 + x3) / 2, (y2 + y3) / 2 - label_offset,
                                    text=f"c = {c:.1f}",
                                    fill="black", font=('Arial', 10))

    def draw_circle(self, radius):
        self.clear_canvas()

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        x_center = canvas_width // 2
        y_center = canvas_height // 2

        max_possible_radius = min(canvas_width, canvas_height) // 2 - 20

        scale = max(50 / radius, 1) if radius < 50 else 200 / radius
        scaled_radius = min(radius * scale, max_possible_radius)

        x1 = x_center - scaled_radius
        y1 = y_center - scaled_radius
        x2 = x_center + scaled_radius
        y2 = y_center + scaled_radius

        self.canvas.create_oval(x1, y1, x2, y2, outline='blue', width=2, fill='lightblue')

        self.canvas.create_text(
            x_center, y1 - 15,
            text=f"Радиус: {radius:.1f}",
            fill="black",
            font=('Arial', 10)
        )

        self.canvas.create_line(
            x_center, y_center,
            x_center, y1,
            fill='red', width=1, dash=(4, 2)
        )

    def draw_cube(self, side):
        self.clear_canvas()
        scale = max(50 / side, 1) if side < 50 else 200 / side
        size = side * scale
        x = 300 - size / 2
        y = 300 - size / 2

        front = [
            (x, y),
            (x + size, y),
            (x + size, y + size),
            (x, y + size)
        ]

        perspective = 0.3

        back = [
            (x - size * perspective, y - size * perspective),
            (x + size - size * perspective, y - size * perspective),
            (x + size - size * perspective, y + size - size * perspective),
            (x - size * perspective, y + size - size * perspective)
        ]

        self.canvas.create_polygon(back, outline='blue', width=2, fill='')

        self.canvas.create_polygon(front, outline='blue', width=2, fill='')

        connections = [
            (front[0], back[0]),
            (front[1], back[1]),
            (front[2], back[2]),
            (front[3], back[3])
        ]

        for (fx, fy), (bx, by) in connections:
            self.canvas.create_line(fx, fy, bx, by, fill='blue', width=2)

        self.canvas.create_text(300, y + size + 20, text=f"Сторона: {side:.1f}", fill="black", font=('Arial', 10))

    def draw_rectangular_parallelepiped(self, length, width, height):
        self.clear_canvas()

        max_dim = max(length, width, height)
        scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim
        l, w, h = length * scale, width * scale, height * scale

        cx, cy = 250, 200

        x1, y1 = cx - w / 2, cy - h / 2
        x2, y2 = cx + w / 2, cy + h / 2

        perspective = 0.3
        x3, y3 = cx - w / 2 - l * perspective, cy - h / 2 - l * perspective
        x4, y4 = cx + w / 2 - l * perspective, cy + h / 2 - l * perspective

        self.canvas.create_rectangle(x1, y1, x2, y2, outline='blue', width=2)

        self.canvas.create_rectangle(x3, y3, x4, y4, outline='blue', width=2)

        self.canvas.create_line(x1, y1, x3, y3, fill='blue', width=2)
        self.canvas.create_line(x1, y2, x3, y4, fill='blue', width=2)
        self.canvas.create_line(x2, y1, x4, y3, fill='blue', width=2)
        self.canvas.create_line(x2, y2, x4, y4, fill='blue', width=2)

        self.canvas.create_text(cx - 5, y1 - 20, text=f"Ширина: {width:.1f}", fill="black")
        self.canvas.create_text((x1 + x3)/2, (y2 + y4)/2 + 20, text=f"Длина: {length:.1f}", fill="black", angle=-45)
        self.canvas.create_text(x2 + 50, cy, text=f"Высота: {height:.1f}", fill="black", angle=90)

    def draw_cylinder(self, radius, height):
        self.clear_canvas()

        max_dim = max(radius * 2, height)
        scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim

        scaled_radius = radius * scale
        scaled_height = height * scale

        x_center = 250
        y_center = 300

        top_y = y_center - scaled_height / 2
        bottom_y = y_center + scaled_height / 2

        self.canvas.create_oval(
            x_center - scaled_radius, top_y - scaled_radius * 0.3,
            x_center + scaled_radius, top_y + scaled_radius * 0.3,
            outline='blue', width=2
        )

        self.canvas.create_oval(
            x_center - scaled_radius, bottom_y - scaled_radius * 0.3,
            x_center + scaled_radius, bottom_y + scaled_radius * 0.3,
            outline='blue', width=2
        )

        self.canvas.create_line(
            x_center - scaled_radius, top_y,
            x_center - scaled_radius, bottom_y,
            fill='blue', width=2
        )
        self.canvas.create_line(
            x_center + scaled_radius, top_y,
            x_center + scaled_radius, bottom_y,
            fill='blue', width=2
        )

        self.canvas.create_text(
            x_center, top_y - 40,
            text=f"Радиус: {radius:.1f}",
            fill="black"
        )
        self.canvas.create_text(
            x_center, top_y - 60,
            text=f"Высота: {height:.1f}",
            fill="black"
        )

    def draw_cone(self, radius, height):
        self.clear_canvas()

        max_dim = max(radius * 2, height)
        scale = max(50 / max_dim, 1) if max_dim < 50 else 200 / max_dim

        scaled_radius = radius * scale
        scaled_height = height * scale

        x_center = 250
        y_center = 300

        apex_x = x_center
        apex_y = y_center - scaled_height / 2

        base_y = y_center + scaled_height / 2

        self.canvas.create_oval(
            x_center - scaled_radius, base_y - scaled_radius * 0.3,
            x_center + scaled_radius, base_y + scaled_radius * 0.3,
            outline='blue', width=2
        )

        self.canvas.create_line(
            apex_x, apex_y,
            x_center + scaled_radius, base_y,
            fill='blue', width=2
        )
        self.canvas.create_line(
            apex_x, apex_y,
            x_center - scaled_radius, base_y,
            fill='blue', width=2
        )

        self.canvas.create_text(
            x_center, apex_y - 30,
            text=f"Радиус: {radius:.1f}", fill="black"
        )
        self.canvas.create_text(
            x_center, apex_y - 10,
            text=f"Высота: {height:.1f}", fill="black"
        )

        l = (radius ** 2 + height ** 2) ** 0.5

        self.canvas.create_text(
            x_center + scaled_radius + 30,
            base_y - scaled_height / 4,
            text=f"Образующая: {l:.1f}",
            fill="black"
        )

    def draw_sphere(self, radius):
        self.clear_canvas()

        scale = max(50 / radius, 1) if radius < 50 else 100 / radius
        scaled_radius = radius * scale

        x_center = 250
        y_center = 300

        self.canvas.create_oval(
            x_center - scaled_radius, y_center - scaled_radius,
            x_center + scaled_radius, y_center + scaled_radius,
            outline='blue', width=2
        )

        vertical_scale = 0.4
        self.canvas.create_oval(
            x_center - scaled_radius, y_center - scaled_radius * vertical_scale,
            x_center + scaled_radius, y_center + scaled_radius * vertical_scale,
            outline='gray', width=1, dash=(4, 2)
        )

        horizontal_scale = 0.4
        self.canvas.create_oval(
            x_center - scaled_radius * horizontal_scale, y_center - scaled_radius,
            x_center + scaled_radius * horizontal_scale, y_center + scaled_radius,
            outline='gray', width=1, dash=(4, 2)
        )

        self.canvas.create_text(
            x_center, y_center - scaled_radius - 30,
            text=f"Радиус: {radius:.1f}", fill="black"
        )

    # Метод для создания главного меню
    def create_main_menu(self):
        for widget in self.frm.winfo_children():
            widget.destroy()

        self.create_label("Выберите тип фигуры", 0, 0, 2, 'Title.TLabel')

        self.create_button("📐 Двумерная фигура", self.show_2d, 1, 0)
        self.create_button("🧊 Трёхмерная фигура", self.show_3d, 1, 1)

        ttk.Separator(self.frm, orient='horizontal').grid(row=2, column=0, columnspan=2, pady=10, sticky='ew')

        # Кнопка выхода
        self.create_button("🚪 Выход", self.root.quit, 3, 0, 2)

    # Метод для отображения выбора двумерных фигур
    def show_2d(self):
        for widget in self.frm.winfo_children():
            widget.destroy()

        self.create_label("Выберите двумерную фигуру", 0, 2, 2)

        figures_2d = ["Квадрат", "Прямоугольник", "Параллелограмм", "Ромб", "Равнобедренная трапеция", "Треугольник", "Круг"]
        self.figures_2d_menu = ttk.Combobox(self.frm, values=figures_2d, width = 30)
        self.figures_2d_menu.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        self.figures_2d_menu.current(0)

        # Кнопки координации "Дальше" и "Вперёд"
        self.create_button("Дальше", self.show_2d_input, 2, 2, 2)
        self.create_button("Назад", self.create_main_menu, 3, 2, 2)

    # Метод для отображения выбора трёхмерных фигур
    def show_3d(self):
        for widget in self.frm.winfo_children():
            widget.destroy()

        self.create_label("Выберите трёхмерную фигуру", 0, 2, 2)
        figures_3d = ["Куб", "Прямоугольный параллелепипед", "Цилиндр", "Конус", "Шар"]
        self.figures_3d_menu = ttk.Combobox(self.frm, values=figures_3d, width = 30)
        self.figures_3d_menu.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
        self.figures_3d_menu.current(0)

        # Кнопки координации "Дальше" и "Вперёд"
        self.create_button("Дальше", self.show_3d_input, 2, 2, 2)
        self.create_button("Назад", self.create_main_menu, 3, 2, 2)

    # Метод для отображения кнопок с учётом последней строки
    def update_buttons(self, figure):
        for widget in self.frm.winfo_children():
            if isinstance(widget, ttk.Button):
                widget.destroy()

        last_row = 0
        for widget in self.frm.winfo_children():
            row = widget.grid_info().get("row", 0)
            if row > last_row:
                last_row = row

        button_row = last_row + 1

        self.create_button("Рассчитать", lambda: self.calculate(figure), button_row, 0, 2)

        back_cmd = self.show_2d if figure in ["Квадрат", "Прямоугольник", "Параллелограмм",
                                              "Ромб", "Равнобедренная трапеция", "Треугольник",
                                              "Круг"] else self.show_3d
        self.create_button("Назад", back_cmd, button_row + 1, 0, 2)
        self.create_button("На главную", self.create_main_menu, button_row + 2, 0, 2)

    # Метод для отображения полей ввода для фигур с разными методами расчёта
    def input_fields_for_method(self, figure, method):
        for widget in self.frm.winfo_children():
            if widget.grid_info()["row"] >= 2 and widget.grid_info()["row"] < 5:
                widget.destroy()

        self.input_fields = {}
        if figure == "Параллелограмм":
            if method == "По стороне и высоте к ней":
                self.create_input_fields("Сторона:", 2, "side1")
                self.create_input_fields("Высота:", 3, "height")
            elif method == "По двум сторонам и углу между ними":
                self.create_input_fields("Первая сторона:", 2, "side1")
                self.create_input_fields("Вторая сторона:", 3, "side2")
                self.create_input_fields("Угол (в градусах):", 4, "angle")

        elif figure == "Ромб":
            if method == "По стороне и высоте":
                self.create_input_fields("Сторона:", 2, "side")
                self.create_input_fields("Высота:", 3, "height")
            elif method == "По сторонам и углу между ними":
                self.create_input_fields("Сторона:", 2, "side")
                self.create_input_fields("Угол (в градусах):", 3, "angle")
            elif method == "По диагоналям":
                self.create_input_fields("Первая диагональ:", 2, "diagonal1")
                self.create_input_fields("Вторая диагональ:", 3, "diagonal2")

        elif figure == "Треугольник":
            if method == "По стороне и высоте":
                self.create_input_fields("Сторона:", 2, "side1")
                self.create_input_fields("Высота:", 3, "height")
            elif method == "По двум сторонам и углу между ними":
                self.create_input_fields("Сторона 1:", 2, "side1")
                self.create_input_fields("Сторона 2:", 3, "side2")
                self.create_input_fields("Угол (в градусах):", 4, "angle")
            elif method == "По трём сторонам":
                self.create_input_fields("Сторона 1:", 2, "side1")
                self.create_input_fields("Сторона 2:", 3, "side2")
                self.create_input_fields("Сторона 3:", 4, "side3")

        self.update_buttons(figure)

    # Метод для отображения полей ввода данных для двумерных фигур
    def show_2d_input(self):
        self.figure = self.figures_2d_menu.get()

        for widget in self.frm.winfo_children():
            widget.destroy()

        self.create_label(f"Введите параметры для {self.figure.lower()}", 0, 0, 2)

        self.input_fields = {}
        if self.figure == "Квадрат":
            self.create_input_fields("Длина стороны: ", 1, "side")

        elif self.figure == "Прямоугольник":
            self.create_input_fields("Длина: ", 1, "side1")
            self.create_input_fields("Ширина: ", 2, "side2")

        elif self.figure == "Параллелограмм":
            self.create_label("Выберите метод расчета:", 1, 0)
            self.method_combobox = ttk.Combobox(
                self.frm,
                values=list(Parallelogram.Methods.keys()),
                state="readonly"
            )
            self.method_combobox.grid(row=1, column=1, padx=10, pady=10)
            self.method_combobox.current(0)
            self.method_combobox.bind("<<ComboboxSelected>>",
                                      lambda e: self.input_fields_for_method("Параллелограмм",
                                                                                  self.method_combobox.get()))

            self.input_fields_for_method("Параллелограмм", self.method_combobox.get())

        elif self.figure == "Ромб":
            self.create_label("Выберите метод расчета:", 1, 0)
            self.method_combobox = ttk.Combobox(
                self.frm,
                values=list(Rhomb.Methods.keys()),
                state="readonly"
            )
            self.method_combobox.grid(row=1, column=1, padx=10, pady=10)
            self.method_combobox.current(0)
            self.method_combobox.bind("<<ComboboxSelected>>",
                                      lambda e: self.input_fields_for_method("Ромб",
                                                                                  self.method_combobox.get()))
            self.input_fields_for_method("Ромб", self.method_combobox.get())

        elif self.figure == "Равнобедренная трапеция":
            self.create_input_fields("Длина верхнего основания: ", 1, "side1")
            self.create_input_fields("Длина нижнего основания: ", 2, "side2")
            self.create_input_fields("Длина высоты: ", 3, "height")

        elif self.figure == "Треугольник":
            self.create_label("Выберите метод расчета:", 1, 0)
            self.method_combobox = ttk.Combobox(
                self.frm,
                values=list(Triangle.Methods.keys()),
                state="readonly"
            )
            self.method_combobox.grid(row=1, column=1, padx=10, pady=10)
            self.method_combobox.current(0)
            self.method_combobox.bind("<<ComboboxSelected>>",
                                      lambda e: self.input_fields_for_method("Треугольник", self.method_combobox.get()))

            self.input_fields_for_method("Треугольник", self.method_combobox.get())

        elif self.figure == "Круг":
            self.create_input_fields("Радиус: ", 1, "radius")

        self.update_buttons(self.figure)

    # Метод для отображения полей ввода данных для трёхмерных фигур
    def show_3d_input(self):
        self.figure = self.figures_3d_menu.get()

        for widget in self.frm.winfo_children():
            widget.destroy()

        self.create_label(f"Введите параметры для {self.figure.lower()}", 0, 0, 2)

        self.input_fields = {}

        if self.figure == "Куб":
            self.create_input_fields("Длина стороны: ", 1, "side")

        elif self.figure == "Прямоугольный параллелепипед":
            self.create_input_fields("Длина: ", 1, "length")
            self.create_input_fields("Ширина: ", 2, "width")
            self.create_input_fields("Высота: ", 3, "height")

        elif self.figure == "Цилиндр":
            self.create_input_fields("Радиус: ", 1, "radius")
            self.create_input_fields("Высота: ", 2, "height")

        elif self.figure == "Конус":
            self.create_input_fields("Радиус: ", 1, "radius")
            self.create_input_fields("Высота: ", 2, "height")

        elif self.figure == "Шар":
            self.create_input_fields("Радиус: ", 1, "radius")

        self.update_buttons(self.figure)


    # Метод для расчёта параметров выбранных фигур с использованием введённых данных
    def calculate(self, figure):
        try:
            current_inputs = {key: entry.get() for key, entry in self.input_fields.items()}

            inputs = {}
            for key, value in current_inputs.items():
                if not value:
                    raise ValueError("Все поля должны быть заполнены")
                try:
                    inputs[key] = float(value)
                    if inputs[key] <= 0:
                        raise ValueError("Все числа должны быть положительными")
                except ValueError:
                    raise ValueError(f"Некорректное значение в поле {key}")

            for widget in self.frm.winfo_children():
                if isinstance(widget, ttk.Label) and widget.grid_info()["row"] >= 8:
                    widget.destroy()

            method = None
            if figure in ["Параллелограмм", "Ромб", "Треугольник"] and hasattr(self, 'method_combobox'):
                method = self.method_combobox.get()

            shape = None
            if figure == "Квадрат":
                shape = Square(inputs["side"])
                self.draw_square(inputs["side"])
            elif figure == "Прямоугольник":
                shape = Rectangle(inputs["side1"], inputs["side2"])
                self.draw_rectangle(inputs["side1"], inputs["side2"])
            elif figure == "Параллелограмм":
                shape = Parallelogram(inputs)
                if method == "По двум сторонам и углу между ними":
                    self.draw_parallelogram(side=inputs["side1"], method=method, angle=inputs["angle"], side2=inputs["side2"])
                elif method == "По стороне и высоте к ней":
                    self.draw_parallelogram(side=inputs["side1"], height=inputs["height"], method=method)
            elif figure == "Ромб":
                shape = Rhomb(inputs)
                if method == "По стороне и высоте":
                    self.draw_rhomb(method=method, side=inputs["side"], height=inputs["height"])
                elif method == "По сторонам и углу между ними":
                    self.draw_rhomb(method=method, side=inputs["side"], angle=inputs["angle"])
                elif method == "По диагоналям":
                    self.draw_rhomb(method=method, d1=inputs["diagonal1"], d2=inputs["diagonal2"])
            elif figure == "Равнобедренная трапеция":
                shape = IsoscelesTrapezoid(inputs["side1"], inputs["side2"], inputs["height"])
                self.draw_isosceles_trapezoid(inputs["side1"], inputs["side2"], inputs["height"])
            elif figure == "Треугольник":
                shape = Triangle(inputs)
                if method == "По двум сторонам и углу между ними":
                    self.draw_triangle(method=method, side1=inputs["side1"], side2=inputs["side2"], angle=inputs["angle"])
                elif method == "По стороне и высоте":
                    self.draw_triangle(method=method, side1=inputs["side1"], height=inputs["height"])
                elif method == "По трём сторонам":
                    self.draw_triangle(method=method, side1=inputs["side1"], side2=inputs["side2"], side3=inputs["side3"])
            elif figure == "Круг":
                shape = Circle(inputs["radius"])
                self.draw_circle(inputs["radius"])
            elif figure == "Куб":
                shape = Cube(inputs["side"])
                self.draw_cube(inputs["side"])
            elif figure == "Прямоугольный параллелепипед":
                shape = RectangularParallelepiped(inputs["length"], inputs["width"], inputs["height"])
                self.draw_rectangular_parallelepiped(inputs["length"], inputs["width"], inputs["height"])
            elif figure == "Цилиндр":
                shape = Cylinder(inputs["radius"], inputs["height"])
                self.draw_cylinder(inputs["radius"], inputs["height"])
            elif figure == "Конус":
                shape = Cone(inputs["radius"], inputs["height"])
                self.draw_cone(inputs["radius"], inputs["height"])
            elif figure == "Шар":
                shape = Sphere(inputs["radius"])
                self.draw_sphere(inputs["radius"])
            else:
                raise ValueError("Неизвестная фигура")

            results = []
            # Для 2D фигур
            if figure in ["Квадрат", "Прямоугольник", "Параллелограмм",
                          "Ромб", "Равнобедренная трапеция", "Треугольник", "Круг"]:
                if method and hasattr(shape, 'area') and callable(shape.area):
                    area = shape.area(method)
                elif hasattr(shape, 'area') and callable(shape.area):
                    area = shape.area()
                else:
                    area = "Недоступно"
                results.append(f"Площадь: {area:.2f}")

                try:
                    if method and hasattr(shape, 'perimeter') and callable(shape.perimeter):
                        perimeter = shape.perimeter(method)
                    elif hasattr(shape, 'perimeter') and callable(shape.perimeter):
                        perimeter = shape.perimeter()
                    else:
                        perimeter = "Недоступно"
                    results.append(f"Периметр: {perimeter:.2f}")
                except Exception as e:
                    results.append(f"Периметр: {str(e)}")

            # Для 3D фигур
            else:
                volume = shape.volume()
                results.append(f"Объем: {volume:.2f}")

                surface_area = shape.surface_area()
                results.append(f"Площадь поверхности: {surface_area:.2f}")

            for i, result in enumerate(results):
                self.create_label(result, 8 + i, 0, 2)

            self.update_buttons(figure)

        except ValueError as e:
            for widget in self.frm.winfo_children():
                if isinstance(widget, ttk.Label) and widget.grid_info()["row"] >= 8:
                    widget.destroy()
            self.create_label(f"Ошибка: {str(e)}", 8, 0, 2)
            self.update_buttons(figure)


# Основной блок программы
if __name__ == "__main__":
    window = Tk()
    app = GeometryApp(window)
    window.mainloop()
