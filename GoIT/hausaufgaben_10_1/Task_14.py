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

        '''Implementiere eine Klasse Contacts, die zum Verwalten von Kontaktinformationen dient. Die Klasse soll 
        zwei Methoden enthalten: list_contacts, die eine Liste der gespeicherten Kontakte zurückgibt, und add_contact, die es ermöglicht, neue Kontakte hinzuzufügen. 
        Jeder Kontakt soll durch eindeutige IDs identifiziert werden, die mit einer Klassenvariable current_id verwaltet wird.
        Die Methode add_contact nimmt vier Parameter (name, phone, email, favorite) und erzeugt ein Wörterbuch mit diesen Werten sowie einer eindeutigen ID, 
        die aus der Klassenvariable current_id stammt. 
        Nach jedem Hinzufügen eines Kontakts wird current_id um eins erhöht, um die Einzigartigkeit der ID für jeden neuen Kontakt zu gewährleisten.'''