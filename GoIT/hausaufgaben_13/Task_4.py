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

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content


'''Entwickeln Sie eine Klasse Person. Sie hat vier Eigenschaften: den Benutzernamen name, seine E-Mail email, die Telefonnummer phone 
und die Eigenschaft favorite - ob es ein Favorit ist oder nicht.
Beispiel für die Erstellung einer Instanz der Klasse:
Person(
"Allen Raymond",
"nulla.ante@vestibul.co.uk", 
"(992) 914-3792",
False,

)

Entwickeln Sie eine Klasse Contacts. Sie sollte über den Konstruktor zwei Eigenschaften initialisieren: filename - der Name der 
Datei zum Packen des Objekts der Klasse Contacts, contacts - eine Liste von Kontakten, Instanzen der Klasse Person.
Beispiel für die Erstellung einer Instanz der Klasse:
contacts = [
Person(
"Allen Raymond",
"nulla.ante@vestibul.co.uk",
"(992) 914-3792",
False,
),
Person(
"Chaim Lewis",
"dui.in@egetlacus.ca",
"(294) 840-6685",
False,
),
]


persons = Contacts("user_class.dat", contacts)
Entwickeln Sie zwei Methoden zur Serialisierung und Deserialisierung der Instanz der Klasse Contacts mithilfe des Pakets pickle 
und zum Speichern der Daten in einer Binärdatei.
Die erste Methode save_to_file speichert die Instanz der Klasse Contacts in einer Datei unter Verwendung der dump-Methode des pickle-Pakets. 
Der Dateiname wird im Attribut filename gespeichert.
Die zweite Methode read_from_file liest eine Instanz der Klasse Contacts aus der Datei filename und gibt sie zurück, 
wobei die load-Methode des pickle-Pakets verwendet wird.
Beispiel:
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file) # False
print(persons.contacts == person_from_file.contacts) # False
print(persons.contacts.name == person_from_file.contacts.name) # True
print(persons.contacts.email == person_from_file.contacts.email) # True
print(persons.contacts.phone == person_from_file.contacts.phone) # True

Die Klasse Person hat einen Konstruktor, der die vier Eigenschaften name, email, phone und favorite initialisiert.
Die Klasse Contacts hat einen Konstruktor, der den Dateinamen filename und optional eine Liste von Person-Objekten 
contacts entgegennimmt. Wenn contacts nicht angegeben wird, wird eine leere Liste verwendet.
Die Methode save_to_file öffnet die Datei mit dem Namen filename im Binärschreibmodus und verwendet pickle.dump, 
um das aktuelle Contacts-Objekt in die Datei zu schreiben
.
Die Methode read_from_file öffnet die Datei mit dem Namen filename im Binärlesemodus, verwendet pickle.load, 
um den Inhalt der Datei zu laden, und gibt das geladene Contacts-Objekt zurück
.
Dieser Code erfüllt die Anforderungen der Aufgabe und ermöglicht das Serialisieren und Deserialisieren 
von Contacts-Objekten mithilfe des pickle-Moduls in Python.
'''