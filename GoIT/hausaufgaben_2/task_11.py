


#Aufgaben:

#1. Erstellen Sie eine Funktion namens `format_string`, die zwei Argumente annimmt: `string` – der zu formatierende Text und `length` – die Länge, innerhalb derer der Text zentriert werden soll.
#2. Wenn die Länge von `string` größer oder gleich `length` ist, geben Sie den Text unverändert zurück.
#3. Wenn die Länge von `string` kleiner als `length` ist, fügen Sie vor dem Text Leerzeichen hinzu, sodass der Text innerhalb von `length` zentriert ist. Bestimmen Sie die Anzahl der Leerzeichen mit der Formel `(length - len(string)) // 2`.
#4. Geben Sie aus der Funktion den formatierten Text zurück, der innerhalb von `length` zentriert ist.

#Erwartetes Ergebnis:

#Die Funktion `format_string` gibt den formatierten Text gemäß den angegebenen Regeln zurück.

#Tipps:

#- Verwenden Sie `len()` zur Bestimmung der Länge des Textes.
#- Verwenden Sie `" " * anzahl_leerzeichen`, um einen Text mit Leerzeichen zu erstellen.



def format_string(string, length):
    if len(string) >= length:
        return string
    spaces_needed = (length - len(string)) // 2
    centered_string = " " * spaces_needed + string
    return centered_string
