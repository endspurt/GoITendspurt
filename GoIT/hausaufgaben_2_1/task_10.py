
#Aufgaben:

#1. Erstellen Sie eine Funktion namens `get_fullname`, die drei Argumente annimmt: `first_name`, `last_name` und `middle_name`. Machen Sie `middle_name` zu einem optionalen Argument mit dem Standardwert `""`.
#2. Wenn `middle_name` übergeben wird, sollte die Funktion den vollständigen Namen im Format 'first_name middle_name last_name' zurückgeben.
#3. Wenn `middle_name` nicht übergeben wird, sollte die Funktion den vollständigen Namen im Format 'first_name last_name' zurückgeben.
#4. Verwenden Sie einen f-string, um den vollständigen Namen zu bilden.

#Erwartetes Ergebnis:

#Die Funktion gibt einen String mit dem vollständigen Namen des Benutzers zurück, abhängig davon, ob ein Mittelname übergeben wurde.

#Tipps:

#- Verwenden Sie eine bedingte Anweisung `if`, um zu prüfen, ob `middle_name` nicht leer ist.
#- Verwenden Sie einen f-string, um die Variablenwerte einzufügen und den vollständigen Namen zu erstellen.




def get_fullname(first_name, last_name, middle_name=""):
    # Перевірка чи middle_name не є порожнім
    if middle_name:
        # Якщо middle_name передано, повертаємо повне ім'я з middle_name
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        # Якщо middle_name не передано, повертаємо повне ім'я без middle_name
        full_name = f"{first_name} {last_name}"
    return full_name

# Приклади використання функції
print(get_fullname("John", "Doe", "Michael"))  # Вивід: John Michael Doe
print(get_fullname("John", "Doe"))            # Вивід: John Doe