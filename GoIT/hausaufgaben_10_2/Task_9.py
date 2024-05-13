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

vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

print(vector1.len())  # 10.04987562112089
print(vector2.len())  # 14.142135623730951

'''Die Aufgabe besteht darin, eine Methode zur Berechnung der Länge eines Vektors in einer Klasse `Vector` in Python zu implementieren. Zuerst übersetze ich die gegebene Aufgabe vom Ukrainischen ins Deutsche:

**Aufgabe:**
"Bevor wir mit Vergleichsoperationen für Vektoren beginnen, implementieren Sie eine Methode zur Bestimmung der Länge eines Vektors - len für die Klasse Vector.

Für den Vektor a mit den Koordinaten (x1, y1) wird seine Länge durch die folgende Formel bestimmt:

(x1 ** 2 + y1 ** 2) ** 0.5."

Jetzt fügen wir die `len` Methode zur Klasse `Vector` hinzu, um die Länge des Vektors zu berechnen. Hier ist die vollständige Implementierung, gefolgt von einer schrittweisen Erklärung des Codes:

### Python-Code:

```python
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
```

### Erklärung des Codes:

1. **Klasse `Point`:**
   - Der Konstruktor `__init__` initialisiert die privaten Variablen `__x` und `__y` und setzt sie dann über Setter-Methoden.
   - `@property` und `@setter` für `x` und `y`: Diese stellen sicher, dass nur Ganzzahlen oder Fließkommazahlen als Koordinaten gesetzt werden können.
   - `__str__`: Gibt eine repräsentative String-Darstellung des Punktes zurück.

2. **Klasse `Vector`:**
   - Der Konstruktor `__init__` nimmt ein `Point`-Objekt als Koordinaten des Vektors.
   - `__setitem__` und `__getitem__`: Ermöglichen den Zugriff und die Zuweisung zu den Koordinaten über Indizes.
   - `__call__`: Kann einen Skalierungsfaktor annehmen und skaliert den Vektor entsprechend.
   - `__add__`, `__sub__`, und `__mul__`: Methoden zur Addition, Subtraktion und zum Skalarprodukt von Vektoren.
   - `len`: Berechnet die Länge des Vektors nach der gegebenen Formel.
   - `__str__`: Gibt eine String-Darstellung des Vektors zurück.

Jede dieser Methoden trägt zur Funktionalität und Flexibilität der `Vector`-Klasse bei, indem sie verschiedene Operationen auf Vektoren ermöglicht, 
wie das Skalieren, Addieren, Subtrahieren oder Berechnen des Skalarprodukts.'''