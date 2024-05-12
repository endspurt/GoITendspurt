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

    def remove_contacts(self, id):
        # Durchsucht die Kontaktliste und entfernt den Kontakt mit der angegebenen ID
        for i, contact in enumerate(self.contacts):
            if contact['id'] == id:
                self.contacts.pop(i)
                break
'''Um die Funktionalität der Klasse Contacts abzuschließen, fügen wir die Methode remove_contact hinzu. 
Diese Methode soll einen Kontakt anhand seiner einzigartigen ID aus der Liste contacts entfernen. 
Wenn kein Kontakt mit der angegebenen ID gefunden wird, führt die Methode keine Aktionen auf der Liste aus.

Hier ist die vollständige Implementierung der Klasse Contacts inklusive der neuen Methode remove_contact:
In der Methode remove_contact wird die Liste contacts nach einem Kontakt durchsucht, dessen ID mit 
dem übergebenen Wert übereinstimmt. Wenn dieser Kontakt gefunden wird, wird er aus der Liste entfernt. 
Die Methode verwendet die Python-Methode enumerate, um sowohl den Index als auch den Wert während der Iteration zu erhalten, 
was das Entfernen eines Elements aus der Liste basierend auf einem Bedingungscheck erleichtert.
'''