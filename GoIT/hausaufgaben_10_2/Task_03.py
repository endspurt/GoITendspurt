class Point:
    def __init__(self, x, y):
        # Initialisiert __x und __y auf None.
        self.__x = None
        self.__y = None
        # Ruft die Setter für x und y auf, um die Anfangswerte zu setzen.
        self.x = x
        self.y = y

    @property
    def x(self):
        # Ein Getter für x, der den Wert von __x zurückgibt.
        return self.__x

    @x.setter
    def x(self, value):
        # Ein Setter für x, der überprüft, ob der Wert streng vom Typ int oder float ist.
        # Wenn der Wert vom Typ int oder float ist, wird __x auf diesen Wert gesetzt.
        # Wenn nicht, bleibt __x auf None.
        if type(value) is int or type(value) is float:
            self.__x = value
        else:
            self.__x = None

    @property
    def y(self):
        # Ein Getter für y, der den Wert von __y zurückgibt.
        return self.__y

    @y.setter
    def y(self, value):
        # Ein Setter für y, der überprüft, ob der Wert streng vom Typ int oder float ist.
        # Wenn der Wert vom Typ int oder float ist, wird __y auf diesen Wert gesetzt.
        # Wenn nicht, bleibt __y auf None.
        if type(value) is int or type(value) is float:
            self.__y = value
        else:
            self.__y = None

# Beispiel der Nutzung
point = Point("a", 10)  # Versucht, 'a' als Wert für x und 10 als Wert für y zu setzen.

print(point.x)  # Gibt None aus, weil 'a' kein int oder float ist.
print(point.y)  # Gibt 10 aus, weil 10 ein int ist.


'''Diese Version des Codes verwendet type-Vergleiche, um sicherzustellen, dass x und y ausschließlich vom Typ int oder float sind, 
und akzeptiert keine Werte, die von diesen Typen abgeleitet sind. Diese Methode ist strikter und vermeidet das Akzeptieren von Subklassen, 
was in manchen Fällen nützlich sein kann, je nachdem, wie streng Sie die Typsicherheit in Ihrer Anwendung handhaben möchten.
Klassen-Definition (class Point): Definiert eine neue Klasse namens Point.

Konstruktor (__init__): Dies ist der Konstruktor der Klasse, der aufgerufen wird, wenn ein neues Objekt der Klasse erstellt wird. 
Er nimmt zwei Parameter, x und y, entgegen und setzt die privaten Variablen __x und __y auf None. Anschließend werden 
die Setter für x und y aufgerufen, um die übergebenen Werte zu setzen.

Properties (@property für x und y): Diese Dekoratoren definieren Methoden als Eigenschaften der Klasse. Sie ermöglichen es, 
die privaten Variablen __x und __y zu lesen, ohne sie direkt zugänglich zu machen.

Setters (@x.setter und @y.setter): Diese Methoden werden aufgerufen, wenn Werte zu x oder y zugewiesen werden. Sie enthalten Logik, 
um zu prüfen, ob der zugewiesene Wert vom Typ int oder float ist. Falls ja, wird der interne Wert entsprechend gesetzt. Falls nein, 
wird der interne Wert auf None gesetzt, um Typsicherheit zu gewährleisten.

Beispiel der Nutzung: Ein Point Objekt wird mit den Werten "a" und 10 für x und y erstellt. Da "a" kein int oder float ist, 
wird x auf None gesetzt. y wird korrekt auf 10 gesetzt, da 10 ein gültiger int Wert ist.

Ausgaben: Der Wert von x und y wird ausgegeben, wobei x None und y 10 ist.

Diese Methode der Typüberprüfung stellt sicher, dass nur korrekte Datentypen in den Koordinaten des Punktes gespeichert werden, 
was die Datenintegrität innerhalb der Klasse Point erhöht.'''