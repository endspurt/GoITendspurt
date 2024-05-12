class Contacts:
    current_id = 1  # Klassenvariable zur Speicherung der aktuellen ID

    def __init__(self):
        self.contacts = []  # Dies speichert die Kontaktliste als Instanzvariable

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        # Erstellt einen neuen Kontakt als Wörterbuch
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        # Fügt den Kontakt zur Kontaktliste hinzu
        self.contacts.append(contact)
        # Inkrementiert die ID, um sicherzustellen, dass jede ID eindeutig ist
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        # Durchsucht die Kontaktliste nach einem Kontakt mit der gegebenen ID
        for contact in self.contacts:
            if contact['id'] == id:
                return contact
        return None
'''Auf dieser Stufe wird die Funktionalität der Klasse Contacts um die Methode get_contact_by_id erweitert, 
die es ermöglicht, einen Kontakt anhand seiner einzigartigen ID zu suchen. Falls kein Kontakt 
mit der angegebenen ID gefunden wird, soll die Methode None zurückgeben.

Hier ist die erweiterte Implementierung der Klasse Contacts:

Die neue Methode get_contact_by_id durchläuft die Liste contacts und sucht nach einem Kontakt, 
dessen id mit dem gegebenen Parameter übereinstimmt. Wenn der Kontakt gefunden wird, 
gibt die Methode das entsprechende Wörterbuch zurück.
 Andernfalls gibt sie None zurück, um anzuzeigen, dass kein Kontakt mit der angegebenen ID existiert.'''