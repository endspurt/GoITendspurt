class Animal:
    color = 'white'  # Klassenvariable, gemeinsam für alle Instanzen

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass  # Grundimplementierung, die überschrieben werden kann

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color  # Ändert die Farbe für alle Instanzen

class Cat(Animal):
    def say(self):
        return "Meow"  # Überschreiben der say Methode für die Cat Klasse

# Erstellung einer Instanz von Cat
cat = Cat("Simon", 10)

# Testen des Polymorphismus durch den Aufruf der überschriebenen Methode
print(cat.say())  # Sollte "Meow" ausgeben


'''Die Aufgabe besteht darin, einen Klasse Cat zu erstellen, der von einem bereits vorhandenen Klasse Animal erbt, 
und dann die Methode say zu überschreiben, 
sodass sie den String "Meow" für Instanzen von Cat zurückgibt. Dieses Konzept ist ein Beispiel für Polymorphismus 
in der objektorientierten Programmierung.Der Klasse Animal enthält eine Klassenvariable color, einen Konstruktor und eine Methode say, die in der Unterklasse überschrieben wird.
Der Klasse Cat erbt von Animal und überschreibt die say Methode, sodass sie "Meow" zurückgibt, was demonstriert, wie Polymorphismus funktioniert.
Eine Instanz von Cat wird erstellt mit dem Namen "Simon" und einem Gewicht von 10 Einheiten, und die überschriebene Methode say wird aufgerufen, um zu zeigen, 
dass die neue Implementierung verwendet wird, nicht die von der Basisklasse Animal.'''