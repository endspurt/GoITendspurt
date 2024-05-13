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
        self.start_point = Point(0, 0)  # Der Startpunkt ist immer (0,0)
        self.coordinates = end_point    # Das Ende des Vektors wird durch das 'coordinates'-Attribut definiert

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

# Beispielverwendung
vector = Vector(Point(1, 10))
print(vector)  # Druckt 'Vector(1, 10)'

vector[0] = 10
print(vector[0])  # 10
print(vector[1])  # 10
print(vector)  # Druckt 'Vector(10, 10)'


''' Implementieren Sie die magische Methode __str__ für die Klassen Point und Vector. Für die Klasse Point 
muss die Methode eine Zeichenkette der Form Point(x,y) zurückgeben, für die Klasse Vector die Zeichenkette Vector(x,y), wie im folgenden Beispiel 
(anstelle von x,y müssen Sie die Koordinaten der Klasseninstanz ersetzen):
Point-Klasse: Die __str__-Methode gibt jetzt eine Zeichenkette der Form Point(x, y) zurück, was den Koordinaten des Punktes entspricht.

Vector-Klasse: Die __str__-Methode gibt die Zeichenkette Vector(x, y) zurück, was den Koordinaten des Vektorendpunktes entspricht. 
Dies zeigt die Koordinaten des Vektors in der Form, wie er sich vom Ursprung (0, 0) zum Punkt (x, y) erstreckt.

Diese Anpassungen stellen sicher, dass die Ausgabe der Objekte der Point- und Vector-Klasse genau den Vorgaben deiner Aufgabe 
entspricht und klar verständlich ist.'''
