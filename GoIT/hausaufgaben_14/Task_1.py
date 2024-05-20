'''Aufgabe:
Wir werden das Beispiel aus der vorherigen Aufgabe erweitern. Fügen Sie der Klasse Contacts ein Attribut count_save hinzu, 
das standardmäßig den Wert 0 haben soll. Implementieren Sie die magische Methode getstate für die Klasse Contacts. Beim Serialisieren 
einer Instanz soll die Methode den Wert des Attributs count_save um eins erhöhen. Somit ist diese Eigenschaft 
ein Zähler für die wiederholten Serialisierungsoperationen der Klasseninstanz.'''

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

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        state = self.__dict__.copy()
        state['count_save'] += 1
        return state

# Beispiel der Funktionalität
contacts = [Person("Alice", "alice@example.com", "12345", True),
            Person("Bob", "bob@example.com", "67890", False)]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3


'''Erläuterung:

Die Klasse Contacts wurde um das Attribut count_save erweitert, das standardmäßig den Wert 0 hat.
Die Methode __getstate__ wurde implementiert, um den Zustand der Instanz vor dem Serialisieren zu verändern. Dabei wird count_save um 1 erhöht.
Im Beispiel wird gezeigt, wie die count_save-Eigenschaft bei jeder Serialisierung (Speichern in eine Datei) erhöht wird.'''