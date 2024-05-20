import json
import re
from datetime import datetime, timedelta

# Load data from file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save data to file
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Validate phone number
def validate_phone(phone):
    pattern = re.compile(r'^\+?[0-9]{10,15}$')
    return pattern.match(phone)

# Validate email address
def validate_email(email):
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return pattern.match(email)

# Add a contact
def add_contact(contacts, name, address, phone, email, birthday):
    if validate_phone(phone) and validate_email(email):
        contacts[name] = {
            'address': address,
            'phone': phone,
            'email': email,
            'birthday': birthday
        }
        return True
    return False

# Edit a contact
def edit_contact(contacts, name, address=None, phone=None, email=None, birthday=None):
    if name in contacts:
        if address:
            contacts[name]['address'] = address
        if phone and validate_phone(phone):
            contacts[name]['phone'] = phone
        if email and validate_email(email):
            contacts[name]['email'] = email
        if birthday:
            contacts[name]['birthday'] = birthday
        return True
    return False

# Delete a contact
def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        return True
    return False

# Search for contacts
def search_contacts(contacts, keyword):
    return {name: info for name, info in contacts.items() if keyword.lower() in name.lower()}

# Get contacts with upcoming birthdays
def upcoming_birthdays(contacts, days):
    today = datetime.today()
    upcoming = {}
    for name, info in contacts.items():
        birthday = datetime.strptime(info['birthday'], '%Y-%m-%d')
        if 0 <= (birthday - today).days <= days:
            upcoming[name] = info
    return upcoming

# Add a note
def add_note(notes, title, content, tags=None):
    notes[title] = {
        'content': content,
        'tags': tags or []
    }

# Edit a note
def edit_note(notes, title, content=None, tags=None):
    if title in notes:
        if content:
            notes[title]['content'] = content
        if tags is not None:
            notes[title]['tags'] = tags
        return True
    return False

# Delete a note
def delete_note(notes, title):
    if title in notes:
        del notes[title]
        return True
    return False

# Search for notes
def search_notes(notes, keyword):
    return {title: note for title, note in notes.items() if keyword.lower() in note['content'].lower()}

# Search for notes by tag
def search_notes_by_tag(notes, tag):
    return {title: note for title, note in notes.items() if tag in note['tags']}

# Suggest command based on input
def suggest_command(input_text):
    commands = ['add_contact', 'edit_contact', 'delete_contact', 'search_contacts', 'upcoming_birthdays',
                'add_note', 'edit_note', 'delete_note', 'search_notes', 'search_notes_by_tag']
    suggestions = [cmd for cmd in commands if cmd.startswith(input_text)]
    return suggestions

# Main function to demonstrate functionality
def main():
    contacts_file = 'contacts.json'
    notes_file = 'notes.json'
    
    contacts = load_data(contacts_file)
    notes = load_data(notes_file)
    
    # Example operations
    add_contact(contacts, 'Max Mustermann', 'Berliner Str. 1', '+4934567890', 'max.mustermann@google.de', '1975-05-20')
    add_note(notes, 'Meeting-Gespraech', 'Bespraechung.', ['meeting', 'project'])
    
    save_data(contacts_file, contacts)
    save_data(notes_file, notes)
    
    print('Contacts:', contacts)
    print('Notes:', notes)
    
    print('Upcoming Birthdays:', upcoming_birthdays(contacts, 7))
    print('Search Contacts:', search_contacts(contacts, 'Max'))
    print('Search Notes by Tag:', search_notes_by_tag(notes, 'meeting'))
    print('Command Suggestions:', suggest_command('add_'))

if __name__ == '__main__':
    main()

