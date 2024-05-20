import copy
import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        # Erstellt eine flache Kopie des Person-Objekts
        new_person = Person(
            self.name,
            self.email,
            self.phone,
            self.favorite
        )
        return new_person

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

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

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        # Erstellt eine flache Kopie des Contacts-Objekts
        new_contacts = Contacts(
            self.filename,
            self.contacts.copy()  # Flache Kopie der Kontaktliste
        )
        new_contacts.is_unpacking = self.is_unpacking
        new_contacts.count_save = self.count_save
        return new_contacts

    def __deepcopy__(self, memo):
        # Erstellt eine tiefe Kopie des Contacts-Objekts
        new_contacts = Contacts(
            self.filename,
            copy.deepcopy(self.contacts, memo)  # Tiefe Kopie der Kontaktliste
        )
        new_contacts.is_unpacking = self.is_unpacking
        new_contacts.count_save = self.count_save
        return new_contacts

# Beispiel zur Überprüfung
person1 = Person("John Doe", "john@example.com", "123456789", False)
person2 = copy.copy(person1)

print(person1.name)  # John Doe
print(person2.name)  # John Doe

contacts1 = Contacts("contacts.pkl", [person1])
contacts2 = copy.copy(contacts1)

print(contacts1.filename)  # contacts.pkl
print(contacts2.filename)  # contacts.pkl
print(contacts1.contacts[0].name)  # John Doe
print(contacts2.contacts[0].name)  # John Doe

''' Implementieren Sie die Methode __copy__ für die Klasse Person.

Implementieren Sie die Methoden __copy__ und __deepcopy__ für die Klasse Contacts.
Erklärung:
Person-Klasse:

Die Methode __copy__ erstellt eine neue Instanz von Person und kopiert die Attribute name, email, phone und favorite.
Contacts-Klasse:

Die Methode __copy__ erstellt eine neue Instanz von Contacts und kopiert die filename und die Kontaktliste (contacts). 
Für die Liste wird eine flache Kopie erstellt.
Die Methode __deepcopy__ erstellt eine neue Instanz von Contacts und kopiert die filename und die Kontaktliste (contacts) 
rekursiv mit copy.deepcopy für eine tiefe Kopie.
'''