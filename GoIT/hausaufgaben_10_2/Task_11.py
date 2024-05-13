from random import randrange

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
        if isinstance(x, (int, float)):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"

class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x *= value
            self.coordinates.y *= value
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
        return self.coordinates.x * vector.coordinates.x + self.coordinates.y * vector.coordinates.y

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()

class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.max_vectors = max_vectors
        self.vectors = [Vector(Point(randrange(0, max_points + 1), randrange(0, max_points + 1))) for _ in range(max_vectors)]

    def __next__(self):
        if self.current_index < self.max_vectors:
            result = self.vectors[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration()

class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)

# Beispiel zur Verwendung
vectors = RandomVectors(5, 10)
for vector in vectors:
    print(vector)

'''Klasse Point - Verwaltet x- und y-Koordinaten eines Punktes mit entsprechenden Getter- und Setter-Methoden zur Validierung.

Klasse Vector - Repräsentiert einen mathematischen Vektor, der verschiedene Operationen wie Addition, Subtraktion und Multiplikation 
(Skalarprodukt) unterstützt. Vergleicht Vektoren basierend auf ihrer Länge durch Überschreibung der Vergleichsmethoden.

Klasse Iterable - Ist ein spezieller Iterator, der eine Liste von Vector-Instanzen erzeugt und über diese iteriert. 
Sie verwaltet einen internen Index (current_index), der bei jedem Aufruf von __next__ erhöht wird, bis das Ende der Liste erreicht ist.

Klasse RandomVectors - Stellt eine Sammlung von Vector-Objekten zur Verfügung, die durch die Iterator-Schnittstelle 
zugänglich sind. Diese Klasse dient als Container, der über die Methode __iter__ den Zugang zu ihren Elementen mittels 
der Iterable-Klasse ermöglicht.

Dieser Code ermöglicht es, über eine Sammlung von zufällig generierten Vektoren zu iterieren, und verwendet dabei 
fortgeschrittene Konzepte der objektorientierten Programmierung in Python.'''