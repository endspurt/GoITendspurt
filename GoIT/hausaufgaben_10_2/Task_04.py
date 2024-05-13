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

class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

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



'''
m einen Wert mit eckigen Klammern wie print(vector[0]) abzurufen, implementieren Sie die Methode __getitem__ in der Klasse Vector.

Um einen Wert in die Koordinaten des Vektors über einen Index wie vector[0] = 10 zu schreiben, implementieren Sie die Methode __setitem__ in der Klasse Vector.

Der Zugriff auf die Koordinate x erfolgt über den Index 0 und der Zugriff auf die Koordinate y über den Index 1."

Nun schreiben wir den vollständigen Python-Code basierend auf der bereitgestellten Klasse Point und fügen die entsprechenden Methoden in der Klasse Vector hinzu

Erklärung der Typenprüfung mit type() im Kontext von Python:

type()-Prüfung: Diese Funktion gibt den Typ eines Objekts zurück. Wenn wir die type()-Funktion verwenden, 
um auf Gleichheit zu testen (type(x) == int), überprüfen wir, ob x genau vom Typ int ist. Das ist etwas restriktiver als isinstance(), 
denn isinstance() würde auch True zurückgeben, wenn x eine Instanz einer Subklasse von int wäre.

Verwendung in Setter: Im Setter nutzen wir diese Prüfung, um sicherzustellen, dass nur Werte vom Typ int oder float zugewiesen werden können. 
Dadurch wird sichergestellt, dass die Koordinatenwerte des Punktes streng den Typen int oder float entsprechen, ohne dass Subklassen 
oder andere Typen akzeptiert werden.

Diese Methode ist in Python besonders nützlich, wenn Sie sehr spezifische Anforderungen an die Typen haben, die eine Variable annehmen kann, 
und keine Typflexibilität wünschen.
Klasse Point:

Der Konstruktor (__init__) initialisiert die privaten Variablen __x und __y und setzt sie über Setter, die die Werte nur akzeptieren, wenn sie vom Typ int oder float sind.
Die property und setter Methoden für x und y stellen sicher, dass die Werte korrekt gesetzt und abgerufen werden können.
Klasse Vector:

Der Konstruktor nimmt ein Point-Objekt entgegen, das als coordinates gespeichert wird.
__setitem__: Erlaubt das Setzen der Werte x oder y des Point-Objekts über Indizes. Index 0 setzt x und Index 1 setzt y. Bei ungültigem Index wird ein IndexError ausgelöst.
__getitem__: Erlaubt das Abrufen der Werte x oder y über Indizes in ähnlicher Weise. Bei ungültigem Index wird ebenfalls ein IndexError ausgelöst.
Dieser Code implementiert die geforderte Funktionalität, sodass auf die Koordinaten des Vektors sowohl über Methodenaufrufe als auch über Indizes zugegriffen werden kann.'''