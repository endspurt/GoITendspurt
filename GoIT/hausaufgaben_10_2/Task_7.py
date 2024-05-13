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
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

class Vector:
    def __init__(self, end_point: Point):
        self.start_point = Point(0, 0)
        self.coordinates = end_point

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Index out of range, must be 0 or 1.")

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Index out of range, must be 0 or 1.")

    def __str__(self):
        return f"Vector({self.coordinates.x}, {self.coordinates.y})"

    def __call__(self, scalar=None):
        if scalar is None:
            return (self.coordinates.x, self.coordinates.y)
        else:
            return (self.coordinates.x * scalar, self.coordinates.y * scalar)

    def __add__(self, other):
        new_x = self.coordinates.x + other.coordinates.x
        new_y = self.coordinates.y + other.coordinates.y
        return Vector(Point(new_x, new_y))

    def __sub__(self, other):
        new_x = self.coordinates.x - other.coordinates.x
        new_y = self.coordinates.y - other.coordinates.y
        return Vector(Point(new_x, new_y))

# Beispielverwendung
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11, 20)
print(vector4)  # Vector(9, 0)

'''Die Aufgabenstellung auf Ukrainisch lautet:

"Implementieren Sie für die Klasse Vector die Operationen Addition und Subtraktion von Vektoren. Das heißt, 
überschreiben Sie die mathematischen Operatoren __add__ und __sub__.

Es gibt zwei Vektoren: a mit den Koordinaten (x1, y1) und b mit den Koordinaten (x2, y2).

Dann ist das Addieren der Vektoren b + a ein neuer Vektor mit den Koordinaten (x2 + x1, y2 + y1). 
Die Subtraktion ist die umgekehrte Operation, b - a ist ein neuer Vektor mit den Koordinaten (x2 - x1, y2 - y1).
Diese Code-Erweiterung ermöglicht es, Vektoren zu addieren und zu subtrahieren, indem die entsprechenden mathematischen 
Operatoren __add__ und __sub__ implementiert werden, die jeweils einen neuen Vector mit den addierten oder subtrahierten Koordinaten zurückgeben.
'''