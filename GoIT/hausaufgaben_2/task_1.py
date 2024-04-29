#Hier ist die Übersetzung Ihres Textes vom Ukrainischen ins Deutsche:

#Erstellen Sie ein Python-Programm, das bestimmt, ob ein Kandidat aufgrund der von ihm im Test erreichten Punktzahl in die nächste Runde des Vorstellungsgesprächs gelangt.

#Aufgaben:

#1. Erfassen Sie die vom Kandidaten im Test erreichten Punkte über die Funktion `input` und speichern Sie sie als ganze Zahl in der Variablen `num`.
#2. Verwenden Sie die If-Else-Kontrollstruktur, um zu bestimmen, ob der Kandidat in die nächste Runde kommt. Wenn `num` größer oder gleich 83 ist, weisen Sie der Variablen `is_next` den Wert `True` zu. Andernfalls weisen Sie ihr den Wert `False` zu.

#Erwartetes Ergebnis:

#Das Programm sollte die vom Kandidaten erreichten Punkte erhalten und ausgeben, ob der Kandidat in die nächste Runde kommt.

#Tipps:

#- Verwenden Sie `int()`, um die Eingabezeichenfolge in eine ganze Zahl umzuwandeln.
#- Der bedingte Operator If-Else hilft zu bestimmen, welche Aktion durchgeführt werden soll, abhängig davon, ob die Bedingung erfüllt ist.


is_next = None
num = int(input("Enter the number of points: "))
if num >= 83 :
    is_next = True
else:
    is_next = False
print (" f")
    