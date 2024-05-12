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

class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)  # Aufruf des Konstruktors der Basisklasse
        self.breed = breed  # Neue Eigenschaft spezifisch für Dog

    def say(self):
        return "Woof"  # Überschreiben der say Methode für die Dog Klasse

# Erstellung einer Instanz von Dog
dog = Dog("Baxter", 20, "Labrador")

# Testen des Polymorphismus und der neuen Eigenschaft
print(dog.say())  # Sollte "Woof" ausgeben
print(f"{dog.nickname} ist ein {dog.breed} und wiegt {dog.weight} kg.")


'''Für die nächste Aufgabe müssen wir einen Klasse Dog erstellen, der von Animal erbt. 
In diesem Klasse wird die Methode say überschrieben, sodass sie den String "Woof" zurückgibt. 
Zudem wird im Konstruktor des Klasse Dog eine neue Eigenschaft breed (Rasse) eingeführt, 
wobei alle von Animal geerbten Eigenschaften beibehalten werden sollen.Der Klasse Dog erbt 
von Animal und führt eine zusätzliche Eigenschaft breed ein.
Der Konstruktor von Dog verwendet super().__init__(nickname, weight) um den Konstruktor 
der Basisklasse aufzurufen, sodass die geerbten Eigenschaften nickname und weight korrekt initialisiert werden.
Die Methode say wird in Dog überschrieben, um "Woof" zurückzugeben.
Es wird eine Instanz von Dog erstellt, und die Eigenschaften sowie die überschriebene Methode werden getestet, 
um die korrekte Implementierung zu überprüfen.'''