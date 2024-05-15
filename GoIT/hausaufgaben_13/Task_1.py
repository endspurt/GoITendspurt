import pickle


def write_contacts_to_file(filename, contacts):
    with open (filename, 'wb') as file:
        pickle.dump (contacts, file )
        


def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        contacts = pickle.load(file)
    return contacts  
        
    
'''Es gibt eine Liste, deren jedes Element ein Wörterbuch mit Benutzerkontakten folgenden Typs ist:

python
Code kopieren
{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Das Wörterbuch enthält den Benutzernamen name, seine E-Mail-Adresse email, Telefonnummer phone und die Eigenschaft favorite, 
ob es sich um einen bevorzugten Kontakt handelt oder nicht.

Entwickeln Sie zwei Funktionen zur Serialisierung und Deserialisierung der Kontaktliste mit dem Paket pickle und zum Speichern 
der erhaltenen Daten in einer Binärdatei.

Die erste Funktion write_contacts_to_file nimmt zwei Parameter: filename - den Dateinamen und contacts - die Kontaktliste. 
Sie speichert die angegebene Liste in einer Datei unter Verwendung der Methode dump des Pakets pickle.

Die zweite Funktion read_contacts_from_file liest und gibt die angegebene Liste contacts aus der Datei filename zurück, 
indem sie die Methode load des Pakets pickle verwendet.
Beispielnutzung:
Angenommen, Sie haben eine Kontaktliste:

python
Code kopieren
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True,
    }
]
Schreiben Sie die Kontaktliste in eine Datei:

python
Code kopieren
write_contacts_to_file('contacts.pkl', contacts)
Lesen Sie die Kontaktliste aus der Datei:

python
Code kopieren
retrieved_contacts = read_contacts_from_file('contacts.pkl')
print(retrieved_contacts)
'''

