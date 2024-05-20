import os
import re
from datetime import datetime, timedelta

# Contact class to store contact information
class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

# Note class to store note information        
class Note:
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags

# Personal Assistant class
class PersonalAssistant:
    def __init__(self):
        self.contacts = []
        self.notes = []
        self.load_data()

    # Load data from files    
    def load_data(self):
        if os.path.exists("contacts.txt"):
            with open("contacts.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    contact = Contact(data[0], data[1], data[2], data[3], data[4])
                    self.contacts.append(contact)
        
        if os.path.exists("notes.txt"):
            with open("notes.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    note = Note(data[0], data[1:])
                    self.notes.append(note)

    # Save data to files
    def save_data(self):
        with open("contacts.txt", "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.address},{contact.phone},{contact.email},{contact.birthday}\n")
        
        with open("notes.txt", "w") as file:
            for note in self.notes:
                file.write(f"{note.text},{','.join(note.tags)}\n")

    # Add a new contact
    def add_contact(self, name, address, phone, email, birthday):
        if not self.validate_phone(phone):
            print("Invalid phone number!")
            return
        
        if not self.validate_email(email):
            print("Invalid email address!")
            return
        
        contact = Contact(name, address, phone, email, birthday)
        self.contacts.append(contact)
        self.save_data()
        print("Contact added successfully!")

    # Search for contacts
    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower():
                results.append(contact)
        return results

    # Edit a contact
    def edit_contact(self, index, name, address, phone, email, birthday):
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact index!")
            return
        
        if not self.validate_phone(phone):
            print("Invalid phone number!")
            return
        
        if not self.validate_email(email):
            print("Invalid email address!")
            return
        
        contact = self.contacts[index]
        contact.name = name
        contact.address = address
        contact.phone = phone
        contact.email = email
        contact.birthday = birthday
        self.save_data()
        print("Contact updated successfully!")

    # Delete a contact
    def delete_contact(self, index):
        if index < 0 or index >= len(self.contacts):
            print("Invalid contact index!")
            return
        
        del self.contacts[index]
        self.save_data()
        print("Contact deleted successfully!")

    # Get upcoming birthdays
    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming = []
        for contact in self.contacts:
            birthday = datetime.strptime(contact.birthday, "%Y-%m-%d").date()
            next_birthday = birthday.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            if (next_birthday - today).days <= days:
                upcoming.append(contact)
        return upcoming

    # Validate phone number format
    def validate_phone(self, phone):
        pattern = re.compile(r'^\+?1?\d{9,15}$')
        return pattern.match(phone)

    # Validate email address format
    def validate_email(self, email):
        pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        return pattern.match(email)

    # Add a new note
    def add_note(self, text, tags):
        note = Note(text, tags)
        self.notes.append(note)
        self.save_data()
        print("Note added successfully!")

    # Search for notes
    def search_notes(self, query):
        results = []
        for note in self.notes:
            if query.lower() in note.text.lower() or query.lower() in [tag.lower() for tag in note.tags]:
                results.append(note)
        return results

    # Edit a note
    def edit_note(self, index, text, tags):
        if index < 0 or index >= len(self.notes):
            print("Invalid note index!")
            return
        
        note = self.notes[index]
        note.text = text
        note.tags = tags
        self.save_data()
        print("Note updated successfully!")

    # Delete a note
    def delete_note(self, index):
        if index < 0 or index >= len(self.notes):
            print("Invalid note index!")
            return
        
        del self.notes[index]
        self.save_data()
        print("Note deleted successfully!")

    # Sort notes by tags
    def sort_notes_by_tags(self):
        self.notes.sort(key=lambda note: note.tags)

    # Guess user's intention and suggest a command
    def guess_intention(self, query):
        if "add" in query.lower() and "contact" in query.lower():
            return "add_contact"
        elif "search" in query.lower() and "contact" in query.lower():
            return "search_contacts"
        elif "edit" in query.lower() and "contact" in query.lower():
            return "edit_contact"
        elif "delete" in query.lower() and "contact" in query.lower():
            return "delete_contact"
        elif "birthday" in query.lower():
            return "get_upcoming_birthdays"
        elif "add" in query.lower() and "note" in query.lower():
            return "add_note"
        elif "search" in query.lower() and "note" in query.lower():
            return "search_notes"
        elif "edit" in query.lower() and "note" in query.lower():
            return "edit_note"
        elif "delete" in query.lower() and "note" in query.lower():
            return "delete_note"
        elif "sort" in query.lower() and "note" in query.lower():
            return "sort_notes_by_tags"
        else:
            return None

# Main program
def main():
    assistant = PersonalAssistant()

    while True:
        print("\nPersonal Assistant")
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Get Upcoming Birthdays")
        print("6. Add Note")
        print("7. Search Notes")
        print("8. Edit Note")
        print("9. Delete Note")
        print("10. Sort Notes by Tags")
        print("0. Exit")

        choice = input("Enter your choice (or type a query): ")

        if choice == "1":
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            birthday = input("Enter birthday (YYYY-MM-DD): ")
            assistant.add_contact(name, address, phone, email, birthday)
        elif choice == "2":
            query = input("Enter search query: ")
            results = assistant.search_contacts(query)
            if results:
                print("Search Results:")
                for i, contact in enumerate(results, start=1):
                    print(f"{i}. {contact.name} - {contact.phone}")
            else:
                print("No contacts found.")
        elif choice == "3":
            index = int(input("Enter contact index to edit: "))
            name = input("Enter updated name: ")
            address = input("Enter updated address: ")
            phone = input("Enter updated phone number: ")
            email = input("Enter updated email address: ")
            birthday = input("Enter updated birthday (YYYY-MM-DD): ")
            assistant.edit_contact(index - 1, name, address, phone, email, birthday)
        elif choice == "4":
            index = int(input("Enter contact index to delete: "))
            assistant.delete_contact(index - 1)
        elif choice == "5":
            days = int(input("Enter number of days: "))
            upcoming_birthdays = assistant.get_upcoming_birthdays(days)
            if upcoming_birthdays:
                print("Upcoming Birthdays:")
                for i, contact in enumerate(upcoming_birthdays, start=1):
                    print(f"{i}. {contact.name} - {contact.birthday}")
            else:
                print("No upcoming birthdays.")
        elif choice == "6":
            text = input("Enter note text: ")
            tags = input("Enter tags (comma-separated): ").split(",")
            assistant.add_note(text, tags)
        elif choice == "7":
            query = input("Enter search query: ")
            results = assistant.search_notes(query)
            if results:
                print("Search Results:")
                for i, note in enumerate(results, start=1):
                    print(f"{i}. {note.text} - Tags: {', '.join(note.tags)}")
            else:
                print("No notes found.")
        elif choice == "8":
            index = int(input("Enter note index to edit: "))
            text = input("Enter updated note text: ")
            tags = input("Enter updated tags (comma-separated): ").split(",")
            assistant.edit_note(index - 1, text, tags)
        elif choice == "9":
            index = int(input("Enter note index to delete: "))
            assistant.delete_note(index - 1)
        elif choice == "10":
            assistant.sort_notes_by_tags()
            print("Notes sorted by tags.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            intention = assistant.guess_intention(choice)
            if intention:
                print(f"Suggested command: {intention}")
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
