import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


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


def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)


# Beispielcode
persons = Contacts("user_class.dat", [Person("Allen Raymond", "allen@example.com", "555-555-5555", False)])

new_persons = copy_class_contacts(persons)

new_persons.contacts[0].name = "Another name"

print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name


'''Hier ist die vollständige Lösung der Aufgabe, bei der die Funktion copy_class_contacts für die Klasse 
Contacts implementiert wird. Diese Funktion verwendet 
die Methode deepcopy aus dem Paket copy, um eine tiefe Kopie eines Contacts-Objekts zu erstellen:
In dieser Lösung wird die Funktion copy_class_contacts implementiert, die eine tiefe Kopie eines Contacts-Objekts mithilfe 
der deepcopy-Funktion aus dem copy-Modul erstellt. Diese tiefe Kopie stellt sicher, 
dass Änderungen an den kopierten Objekten die Originalobjekte nicht beeinflussen.
'''