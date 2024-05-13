class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

# Beispiel zur Verwendung der Klasse
point = Point(5, 10)
print(point.x)  # Gibt 5 aus
print(point.y)  # Gibt 10 aus


'''In der Klasse Point sind durch den Konstruktor __init__ zwei Attribute deklariert: die Koordinaten x und y. Verstecke den Zugang zu 
ihnen mithilfe der doppelten Unterstriche: __x und __y.

Implementiere für die Klasse Point Mechanismen von Setter und Getter für die Attribute __x und __y mithilfe der Dekoratoren property und setter.
Dieser Code definiert eine Klasse Point mit privaten Attributen __x und __y. Die Zugriffe auf diese privaten Variablen werden durch die property-Dekoratoren 
und die entsprechenden Setter reguliert, was eine kapselnde Verwaltung der Daten ermöglicht.'''