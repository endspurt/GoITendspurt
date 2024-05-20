'''Wir erweitern das Beispiel aus der vorherigen Aufgabe. Fügen Sie der Klasse Contacts ein Attribut is_unpacking hinzu, 
das standardmäßig den Wert False haben soll. Implementieren Sie die magische Methode __setstate__ für die Klasse Contacts. 
Beim Entpacken einer Instanz der Klasse soll die Methode den Wert des Attributs is_unpacking auf True ändern. 
Dadurch wird diese Eigenschaft bestimmen, dass die Instanz der Klasse durch Entpacken erhalten wurde.'''

import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False  # Neues Attribut hinzugefügt

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.is_unpacking = True  # Attribut auf True setzen beim Entpacken

# Beispiel der Verwendung
contacts = [Person("John Doe", "john@example.com", "1234567890", False)]
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True


'''Erläuterung:

Das neue Attribut is_unpacking wurde zur Klasse Contacts hinzugefügt und standardmäßig auf False gesetzt.
Die Methode __setstate__ wurde so implementiert, dass das Attribut is_unpacking beim Entpacken auf True gesetzt wird.
Ein Beispielcode zeigt die Verwendung der Klasse und wie der Wert von is_unpacking überprüft wird.'''