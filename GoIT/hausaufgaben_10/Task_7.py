class Animal:
    color = 'white'

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color

class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        super().__init__(nickname, weight)
        self.breed = breed
        self.owner = owner  # Zuweisung einer Owner-Instanz zu jeder Dog-Instanz

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()  # Rückgabe der Besitzerinformationen als Wörterbuch

class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address
        }

# Erstellung einer Instanz von Owner
owner = Owner("John Doe", 45, "1234 Elm Street")

# Erstellung einer Instanz von Dog, die einen Besitzer einschließt
dog = Dog("Baxter", 20, "Labrador", owner)

# Nutzung der who_is_owner Methode zur Ausgabe der Besitzerdaten
owner_info = dog.who_is_owner()
print(owner_info)

'''Wir werden nun einen neuen Klasse Owner hinzufügen, der drei Attribute hat: name, age, und address. 
Weiterhin wird eine Methode info implementiert, die ein Wörterbuch mit diesen Attributen als Schlüsseln zurückgibt. 
Für den Klasse Dog wird dann ein neues Attribut owner hinzugefügt, das eine Instanz von Owner ist. 
Zusätzlich fügen wir eine Methode who_is_owner hinzu, die die Informationen des Besitzers mithilfe der Methode info ausgibt.
Der Klasse Owner wird erstellt, der die Attribute name, age, und address enthält und eine Methode info, die diese Attribute als Wörterbuch zurückgibt.
Der Klasse Dog erhält das neue Attribut owner, das eine Instanz von Owner ist, und eine Methode who_is_owner, die die Informationen 
des Besitzers durch Aufrufen von info auf der owner-Instanz erhält.
Es wird gezeigt, wie man die Besitzerinformationen eines Dog-Objekts über die Methode who_is_owner abfragen kann.'''