
#Hier ist die Übersetzung Ihres Textes vom Ukrainischen ins Deutsche:

#Erstellen Sie ein Python-Programm, das ein leeres Wörterbuch `cat` modifiziert, indem es verschiedene Schlüssel und Werte hinzufügt, und Werte aus einem anderen Wörterbuch `info` verwendet.

#Aufgaben:

#1. Verwenden Sie das Wörterbuch `cat` zur Speicherung von Informationen über eine Katze. Fügen Sie ihm die folgenden Schlüssel und entsprechenden Werte hinzu:
#   - Schlüssel `"nick"` mit dem String-Wert des Namens der Katze (zum Beispiel "Simon").
#   - Schlüssel `"age"` mit dem ganzzahligen Wert des Alters der Katze (zum Beispiel 7).
#   - Schlüssel `"characteristics"` mit einer Liste von Charaktereigenschaften der Katze (zum Beispiel ["sanft", "beißt"]).
#2. Deklarieren Sie eine Variable `age` und verwenden Sie die Methode `get`, um das Alter der Katze aus dem Wörterbuch `cat` zu erhalten.
#3. Verwenden Sie die Methode `update`, um alle Schlüssel-Wert-Paare aus dem Wörterbuch `info` zum Wörterbuch `cat` hinzuzufügen.



# Створення порожнього словника для зберігання інформації про кота
cat = {}

# Додавання інформації до словника cat
cat['nick'] = 'Simon'  # Ім'я кота
cat['age'] = 7         # Вік кота
cat['characteristics'] = ['лагідний', 'кусається']  # Характеристики кота

# Використання методу get для отримання віку кота зі словника
age = cat.get('age')
print(f"Age of the cat: {age}")

# Створення іншого словника з додатковою інформацією
info = {
    'status': 'vaccinated',
    'breed': True
}

# Використання методу update для додавання інформації зі словника info до cat
cat.update(info)

# Вивід кінцевого стану словника cat
print("Information about the cat:")
print(cat)