


#Aufgaben:

#1. Erstellen Sie eine Funktion namens `invite_to_event`, die einen Parameter annimmt - `username`.
#2. Innerhalb der Funktion verwenden Sie einen f-string, um eine Nachricht mit einem personalisierten Namen zu erstellen.
#3. Die Funktion sollte den String zurückgeben: "Dear {username}, we have the honour to invite you to our event".

#Erwartetes Ergebnis:

#Die Funktion gibt einen String mit einer personalisierten Einladung zurück.

#Tipps:

#- Verwenden Sie `return`, um das Ergebnis des Funktionsaufrufs `invite_to_event` zurückzugeben.
#- Denken Sie daran, die geschweiften Klammern `{}` im f-string zu verwenden, um den Wert der Variablen einzufügen.


def invite_to_event(username):
    # Створення персоналізованого повідомлення з використанням f-рядка
    invitation = f"Dear {username}, we have the honour to invite you to our event"
    # Повернення сформованого запрошення
    return invitation

# Використання функції для створення запрошення для користувача
user_name = "John"
print(invite_to_event(user_name))
    