'''
Задача 3. Тестирование класса с использованием doctest
Напишите класс Rectangle, который управляет прямоугольником. Класс должен
поддерживать следующие методы:
● set_dimensions(width, height): устанавливает ширину и высоту
прямоугольника.
● get_area(): возвращает площадь прямоугольника.
● get_perimeter(): возвращает периметр прямоугольника.
Напишите 3 теста с помощью doctest.
'''


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Инициализация прямоугольника с заданными шириной и высотой.
        >>> r = Rectangle(3, 4)
        >>> r.get_area()
        12
        >>> r.get_perimeter()
        14
        """
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        """
        Устанавливает ширину и высоту прямоугольника.
        >>> r = Rectangle()
        >>> r.set_dimensions(6, 7)
        >>> r.get_area()
        42
        >>> r.get_perimeter()
        26
        """
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами.")
        self.width = width
        self.height = height

    def get_area(self):
        """Возвращает площадь прямоугольника."""
        return self.width * self.height

    def get_perimeter(self):
        """Возвращает периметр прямоугольника."""
        return 2 * (self.width + self.height)


import doctest

if __name__ == "__main__":
    doctest.testmod()
