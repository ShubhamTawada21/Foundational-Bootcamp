from abc import ABC, abstractmethod
import math
class Shape(ABC):
    total_shape_count = 0
    def __init__(self, name):
        self.name = name
        Shape.total_shape_count += 1
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def describe(self):
        print(f"{self.name}:")
        print(f"  Area: {self.area():.2f}")
        print(f"  Perimeter: {self.perimeter():.2f}")
        print()
    @classmethod
    def total_shapes(cls):
        return cls.total_shape_count
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
class Triangle(Shape):
    def __init__(self, side1, side2, side3, height):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
    def area(self):
        return 0.5 * self.side1 * self.height
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
def print_report(shape_list):
    print("Shape Report")
    print("-" * 20)
    for shape in shape_list:
        shape.describe()
shapes = [
    Circle(5),
    Rectangle(10, 4),
    Triangle(6, 5, 7, 4)
]
print_report(shapes)
print("Total shapes created:", Shape.total_shapes())
