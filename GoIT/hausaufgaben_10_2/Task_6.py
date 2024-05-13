
'''
Hierbei wird die Klasse `Vector` so erweitert, dass sie sich wie eine Funktion verhält (Funktor), 
die je nach Argument 
entweder die Koordinaten des Vektors oder die skalierten Koordinaten zurückgibt.

Hier ist die Erweiterung des `Vector`-Klasse mit der Implementierung von `__call__`:'''

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

# Beispielverwendung
vector = Vector(Point(1, 10))
print(vector())  # Gibt (1, 10) aus
print(vector(5))  # Gibt (5, 50) aus

'''Erklärung des __call__-Verhaltens:

Wenn kein Argument übergeben wird (scalar=None), gibt die Methode die aktuellen Koordinaten des Vektors als Tupel zurück.
Wenn ein numerischer Wert übergeben wird, wird jede Koordinate mit diesem Wert multipliziert und das resultierende Tupel 
der neuen Koordinaten zurückgegeben. Dies stellt die Skalierung des Vektors dar.'''