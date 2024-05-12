class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


    
class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return "Meow"

    def change_weight(self, weight):
        self.weight = weight
        
'''Die Anweisung bedeutet, dass du einen CatDog-Klasse implementieren sollst, die sich sowohl wie eine Katze als 
auch wie ein Hund verhält, ohne von einer Animal-Klasse zu erben. Da spezifiziert wurde, 
dass sie sich wie eine Katze verhalten soll, implementieren wir dies durch das Hinzufügen von Katzenverhalten zur CatDog-Klasse.
Diese Klasse CatDog hat die Eigenschaften nickname und weight, ähnlich wie die Animal-Klasse. Die Methode say ermöglicht es, 
dass der CatDog "Meow" wie eine Katze sagt. Die Methode change_weight ermöglicht es, das Gewicht des CatDog zu ändern. Dieser Ansatz folgt 
dem Konzept des Polymorphismus, 
indem CatDog sich wie ein Objekt der Cat-Klasse verhält, obwohl sie nicht direkt von Animal erbt.
'''