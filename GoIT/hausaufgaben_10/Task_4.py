class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight
        
    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color
        
first_animal = Animal("B",10)
second_animal = Animal("C",20)   

first_animal.change_color("red")

# Anzeigen der Farbe und des Gewichts beider Tiere zur Überprüfung der Änderungen
print(f"Erstes Tier: {first_animal.nickname}, Gewicht: {first_animal.weight}, Farbe: {first_animal.color}")
print(f"Zweites Tier: {second_animal.nickname}, Gewicht: {second_animal.weight}, Farbe: {second_animal.color}")
        
'''Um den Python-Klasse Animal zu erweitern und eine Klassenvariable color sowie eine Methode change_color zu implementieren, 
die die Farbe aller Instanzen von Animal ändert, können Sie den folgenden Code verwenden:

python
In diesem Code:

Die Methode change_weight ändert das Gewicht eines spezifischen Animal-Objekts.
Die Methode change_color ist eine Klassenmethode, die die color Klassenvariable für alle Instanzen von Animal ändert. Dazu verwenden wir 
den Dekorator @classmethod, der es ermöglicht, dass die Methode auf die Klasse selbst und nicht auf eine Instanz der Klasse wirkt.
Durch den Aufruf von change_color("red") auf einer Instanz (hier first_animal) wird die Farbe aller Instanzen von Animal auf "rot" geändert, 
da color eine Klassenvariable ist. Dies zeigt, wie eine Änderung an einer Klassenvariable sich auf alle Instanzen auswirkt.'''