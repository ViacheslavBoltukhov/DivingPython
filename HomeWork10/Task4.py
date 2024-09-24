'''
Создайте базовый класс Animal, который имеет атрибут name, представляющий имя
животного.
Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и
добавляют дополнительные атрибуты и методы:
Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который
возвращает длину крыла птицы.
Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который
возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в
зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к
категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к категории
"Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".
Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию
млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта
меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".
Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных
разных типов на основе переданного типа и параметров. Класс-фабрика должен иметь
метод create_animal, который принимает следующие аргументы:
animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
*args - переменное количество аргументов, представляющих параметры для конкретного
типа животного. Количество и типы аргументов могут различаться в зависимости от типа
животного.
Метод create_animal должен создавать и возвращать экземпляр животного заданного
типа с переданными параметрами.
Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с
сообщением 'Недопустимый тип животного'.
'''


class Animal:
    def __init__(self, name: str):

        self.name = name


def speak(self):
    raise NotImplementedError("Subclasses should implement thismethod")


def __str__(self):
    return f"{self.__class__.__name__} named {self.name}"


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def __str__(self):
        return f"{super().__str__()} of breed {self.breed}"


class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color

    def speak(self):
        return "Meow!"

    def __str__(self):
        return f"{super().__str__()} with color {self.color}"


class AnimalFactory:


    @staticmethod
    def create_animal(animal_type: str, *args) -> Animal:
        """
        Создает экземпляр животного на основе переданного типа и
        параметров.
        :param animal_type: Название типа животного (например, 'Dog'
        или 'Cat')
        :param args: Параметры для конструктора животного
        :return: Экземпляр соответствующего класса животного
        """
        animal_classes = {
            'Dog': Dog,
            'Cat': Cat
        }
        if animal_type in animal_classes:
            return animal_classes[animal_type](*args)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


# Создаем экземпляры животных с использованием фабрики
dog = AnimalFactory.create_animal('Dog', 'Buddy', 'GoldenRetriever')
cat = AnimalFactory.create_animal('Cat', 'Whiskers', 'Black')
print(dog)  # Вывод: Dog named Buddy of breed Golden Retriever
print(cat)  # Вывод: Cat named Whiskers with color Black
print(dog.speak())  # Вывод: Woof!
print(cat.speak())  # Вывод: Meow
