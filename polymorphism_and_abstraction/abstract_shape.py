"""
## 3. Abstract Shape with ABC Module  *(Medium)*

=================================================
ABSTRACT SHAPE (USING abc MODULE)
=================================================

Problem Statement:
Use Python's built-in `abc` module to define a
TRUE abstract base class called `Shape`. Any
child class that does NOT implement every
abstract method must NOT be instantiable — the
abc module enforces this for you at object
creation time.

Children to build:
   Circle
   Rectangle
   Triangle

Each child must implement two abstract
methods: `area()` and `perimeter()`.

This problem teaches ABSTRACTION:
   - hiding the details behind a clean
     contract
   - forcing all children to follow that
     contract
   - the caller writes ONE function that
     works on ANY shape

-------------------------------------------------
Instructions:
1. Import the abc module:
      from abc import ABC, abstractmethod

2. Define the abstract base class:
      class Shape(ABC):
          def __init__(self, name):
              self.name = name

          @abstractmethod
          def area(self):
              pass

          @abstractmethod
          def perimeter(self):
              pass

3. Define the children Circle, Rectangle and
   Triangle. Each one:
      - calls super().__init__("Circle" / ...)
      - implements area() and perimeter()
        with the appropriate formula
4. In the driver code:
      - try to instantiate Shape("nope")
        inside a try / except TypeError block
        to show that Python REFUSES because
        the abstract methods are not
        implemented.
      - create at least one of each child
      - put them in a LIST and call area() and perimeter()
            on each one in a for loop, showing that
            on each in a for loop.
5. Do NOT use:
   - the math module (use 3.14159 as PI)
   - any external library
   - isinstance() / type() in the for loop

-------------------------------------------------
Input Example:
Shapes("nope")
shapes = [
   Circle(5),
   Rectangle(4, 6),
   Triangle(3, 4, 5),
]

Output Example:
Cannot create Shape directly:
   TypeError: Can't instantiate abstract class
   Shape with abstract methods area, perimeter

Circle    -> area=78.53975, perimeter=31.4159
Rectangle -> area=24,       perimeter=20
Triangle  -> area=6.0,      perimeter=12

-------------------------------------------------
Explanation:
- The `@abstractmethod` decorator marks
  area() and perimeter() as REQUIRED methods.
- Any class that inherits Shape MUST
  implement them or it cannot be
  instantiated.
- describe() uses the abstract methods but
  ITSELF is concrete. It works for any shape
  because of polymorphism — exactly the
  abstraction we want.
=================================================

"""
from abc import ABC, abstractmethod

class Figure(ABC):

    def __init__(self, figure_name):
        self.figure_name = figure_name

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def show_details(self):
        print(f"{self.figure_name}")
        print(f"Area      : {self.calculate_area()}")
        print(f"Perimeter : {self.calculate_perimeter()}")
        print("-" * 30)


class RoundShape(Figure):

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        pi = 3.14159
        return pi * self.radius * self.radius

    def calculate_perimeter(self):
        pi = 3.14159
        return 2 * pi * self.radius


class BoxShape(Figure):

    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class ThreeSideShape(Figure):

    def __init__(self, side1, side2, side3):
        super().__init__("Triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) *
                (s - self.side2) *
                (s - self.side3)) ** 0.5

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


try:
    sample = Figure("Test Shape")

except TypeError as error:
    print("Cannot create abstract class object!")
    print(error)


all_shapes = [
    RoundShape(5),
    BoxShape(4, 6),
    ThreeSideShape(3, 4, 5)
]

for item in all_shapes:
    item.show_details()