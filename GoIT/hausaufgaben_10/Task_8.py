class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"



class CatDog(Cat, Dog):
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return Cat.say(self)  # Spezifisch "Meow" durch direkten Aufruf der Cat-Klasse Methode

    def info(self):
        return f"{self.nickname}-{self.weight}"

class DogCat(Dog, Cat):
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return Dog.say(self)  # Spezifisch "Woof" durch direkten Aufruf der Dog-Klasse Methode

    def info(self):
        return f"{self.nickname}-{self.weight}"
    
    '''Erstelle zwei Klassen: CatDog und DogCat. Diese Klassen sollten von zwei Klassen gleichzeitig erben: 
    Cat und Dog. Nach der Vererbung sollte die Methode say des CatDog-Klassenobjekts "Meow" zurückgeben und 
    beim DogCat-Klassenobjekt — "Woof". 
    Implementiere für beide genannten Klassen eine Methode info, die einen String im folgenden Format 
    zurückgibt: f"{self.nickname}-{self.weight}".
    Die CatDog Klasse erbt zuerst von Cat, dann von Dog. Die Methode say() ruft explizit die Methode der Cat Klasse auf, sodass "Meow" zurückgegeben wird.
    Die DogCat Klasse erbt zuerst von Dog, dann von Cat. Die Methode say() ruft explizit die Methode der Dog Klasse auf, sodass "Woof" zurückgegeben wird.
    Beide Klassen haben eine info() Methode, die einen formatierten String zurückgibt, der den Spitznamen und das Gewicht des Objekts enthält.'''