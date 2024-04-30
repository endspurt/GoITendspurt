


#Aufgaben:

#1. Mit den gegebenen Variablen `message`, ein String, in dem die Suche durchgeführt wird, und `search`, ein Zeichen, das gesucht wird, zählen Sie, wie oft das Zeichen `search` im String `message` vorkommt.
#2. Verwenden Sie eine `for`-Schleife, die durch jedes Zeichen in `message` geht.
#3. Wenn das aktuelle Zeichen mit dem Zeichen in der Variablen `search` übereinstimmt, erhöhen Sie die Variable `result` um 1.
#4. Speichern Sie die endgültige Anzahl der Vorkommen in der Variablen `result`.

#Erwartetes Ergebnis:

#Das Programm soll in der Variablen `result` die Anzahl der Male speichern, die das Zeichen `search` im String `message` vorkommt.

#Tipps:

#- Verwenden Sie `==`, um das aktuelle Zeichen mit dem gesuchten Zeichen zu vergleichen.
#- Denken Sie daran, dass eine `for`-Schleife automatisch durch jedes Zeichen im String geht.



message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for i in message :
    if search == i:
        result +=1
print ( result)
    