#Hier ist die Übersetzung Ihres Textes vom Ukrainischen ins Deutsche:

#Erstellen Sie ein Python-Programm, das die Kategorie eines Entwicklers (Junior, Middle, Senior) basierend auf seiner Berufserfahrung bestimmt.

#Aufgaben:

#1. Erhalten Sie von dem Benutzer die Berufserfahrung über die Funktion `input` und speichern Sie diesen Wert als ganze Zahl in der Variablen `work_experience`.
#2. Basierend auf dem Wert von `work_experience` müssen Sie den Entwicklungslevel festlegen und diesen als String in der Variablen `developer_type` speichern. Verwenden Sie die folgenden Regeln:
#   - Wenn die Berufserfahrung von 1 Jahr bis einschließlich 5 Jahre beträgt, sollte `developer_type` "Middle" sein.
#   - Wenn die Berufserfahrung bis zu 1 Jahr einschließlich beträgt, sollte `developer_type` "Junior" sein.
#   - Wenn die Berufserfahrung mehr als 5 Jahre beträgt, sollte `developer_type` "Senior" sein.

#Erwartetes Ergebnis:

#Das Programm sollte den Entwicklungslevel abhängig von der Berufserfahrung anzeigen, die der Benutzer eingegeben hat.

#Tipps:

#- Überprüfen Sie sorgfältig die Bedingungen in Ihrer if-elif-else-Struktur, um sicherzustellen, dass sie den Regeln für die Bestimmung des Entwicklungslevels entsprechen.
#- Vergessen Sie nicht, `int()` zu verwenden, um die vom Benutzer eingegebene Zeichenkette in eine ganze Zahl umzuwandeln.


work_experience = int(input("Enter your full work experience in years: "))

if work_experience <= 5 and work_experience > 1:
    developer_type = "Middle"
elif work_experience <= 1 :
    developer_type = "Junior"
else :
    developer_type = "Senior"