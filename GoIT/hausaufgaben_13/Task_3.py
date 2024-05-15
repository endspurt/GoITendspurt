import csv

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone", "favorite"])
        writer.writeheader()
        writer.writerows(contacts)

def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        contacts = []
        for row in reader:
            # Konvertiere das 'favorite'-Feld zurück in einen booleschen Wert
            row['favorite'] = row['favorite'] == 'True'
            contacts.append(row)
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

Entwickeln Sie zwei Funktionen zur Serialisierung und Deserialisierung der Kontaktliste mit dem Paket csv und zum Speichern 
der erhaltenen Daten in einer Textdatei.

Die erste Funktion write_contacts_to_file nimmt zwei Parameter: filename - den Dateinamen und contacts - die Kontaktliste. 
Sie speichert die angegebene Liste in einer Datei im CSV-Format.

Die Struktur der CSV-Datei sollte wie folgt aussehen:

csv
Code kopieren
name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True
Beachten Sie, dass die erste Zeile der Datei die Überschriften enthält – dies sind die Namen der Schlüssel.

Die zweite Funktion read_contacts_from_file liest, konvertiert die Daten und gibt die angegebene Liste contacts aus 
der Datei filename zurück, die zuvor von der Funktion write_contacts_to_file gespeichert wurde.

Hinweis: Beim Lesen der CSV-Datei erhalten wir die Eigenschaft favorite des Wörterbuchs als Zeichenfolge, z.B. favorite='False'. 
Es ist notwendig, sie zurück in einen booleschen Wert zu konvertieren, sodass favorite=False wird.
Lösung der Aufgabe:
Hier sind die zwei geforderten Funktionen:

python
Code kopieren
import csv

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone", "favorite"])
        writer.writeheader()
        writer.writerows(contacts)

def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        contacts = []
        for row in reader:
            # Konvertiere das 'favorite'-Feld zurück in einen booleschen Wert
            row['favorite'] = row['favorite'] == 'True'
            contacts.append(row)
        return contacts
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
Schreiben Sie die Kontaktliste in eine CSV-Datei:

python
Code kopieren
write_contacts_to_file('contacts.csv', contacts)
Lesen Sie die Kontaktliste aus der CSV-Datei:

python
Code kopieren
retrieved_contacts = read_contacts_from_file('contacts.csv')
print(retrieved_contacts)
Dies speichert die Kontaktliste in einer Textdatei namens contacts.csv und liest sie später zurück, wobei die booleschen Werte korrekt konvertiert werden.

'''