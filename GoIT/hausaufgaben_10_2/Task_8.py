'''"Implementieren Sie für die Klasse Vector die Operation des Skalarprodukts der Vektoren. Das heißt, überschreiben Sie für ihn den mathematischen Operator __mul__.

Es gibt zwei Vektoren: a mit den Koordinaten (x1, y1) und Vektor b mit den Koordinaten (x2, y2).

Dann ist das Skalarprodukt der Vektoren ba ein solches Zahl x2x1 + y2*y1.'''

'''vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

scalar = vector2 * vector1

print(scalar)  # 110
'''

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

    def __mul__(self, other):
        return self.coordinates.x * other.coordinates.x + self.coordinates.y * other.coordinates.y

# Beispielverwendung
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

scalar = vector2 * vector1

print(scalar)  # 110


'''Erklärung der Implementierung des Skalarprodukts (__mul__):

Zweck: Berechnet das Skalarprodukt zweier Vektoren, was ein Maß für die Richtungsähnlichkeit und die Stärke der beiden Vektoren ist.
Ablauf: Multipliziert die x-Koordinaten und die y-Koordinaten der beiden Vektoren miteinander und summiert die Ergebnisse, 
um das Skalarprodukt zu erhalten. Das Ergebnis ist eine einzige Zahl, nicht ein Vektor.
Diese Methode ermöglicht es, das Skalarprodukt zweier Vektorinstanzen direkt durch den *-Operator zu berechnen, 
was in vielen mathematischen und physikalischen Berechnungen nützlich ist.'''