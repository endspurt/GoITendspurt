
'''Um den gegebenen Code zu vervollständigen und sicherzustellen, dass alle Vergleichsmethoden korrekt 
implementiert sind, werden wir die Methoden __eq__, __ne__, __lt__, __gt__, __le__, und __ge__ hinzufügen. 
Diese Methoden sollen die Vektoren basierend auf ihrer Länge vergleichen, die durch die Methode len() berechnet wird.'''

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == int or type(x) == float:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (self.coordinates.x * vector.coordinates.x +
                self.coordinates.y * vector.coordinates.y)

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, other):
        return self.len() == other.len()

    def __ne__(self, other):
        return self.len() != other.len()

    def __lt__(self, other):
        return self.len() < other.len()

    def __gt__(self, other):
        return self.len() > other.len()

    def __le__(self, other):
        return self.len() <= other.len()

    def __ge__(self, other):
        return self.len() >= other.len()

# Beispiel zur Verwendung der Klasse Vector
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))

print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True

'''rklärung der hinzugefügten Vergleichsmethoden:
__eq__ (gleich): Vergleicht, ob zwei Vektoren dieselbe Länge haben.
__ne__ (nicht gleich): Vergleicht, ob zwei Vektoren unterschiedliche Längen haben.
__lt__ (kleiner als): Bestimmt, ob die Länge des ersten Vektors kleiner ist als die des zweiten.
__gt__ (größer als): Bestimmt, ob die Länge des ersten Vektors größer ist als die des zweiten.
__le__ (kleiner gleich): Bestimmt, ob die Länge des ersten Vektors kleiner oder gleich der des zweiten ist.
__ge__ (größer gleich): Bestimmt, ob die Länge des ersten Vektors größer oder gleich der des zweiten ist.
Diese Methoden ermöglichen es Ihnen, die Instanzen der Vector-Klasse direkt miteinander zu vergleichen, 
basierend auf ihrer Länge, was der Anforderung der Aufgabe entspricht.'''