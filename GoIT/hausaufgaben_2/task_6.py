
#Aufgaben:

#1. Sie haben eine Variable `pool`, die 1000 entspricht - die Anzahl der SMS, die zum Senden verfügbar sind.
#2. Fordern Sie den Marketingmitarbeiter auf, die Anzahl der Sendungen `quantity` einzugeben.
#3. Berechnen Sie die Größe des SMS-Pakets für jede Sendung, Variable `chunk`, indem Sie `pool` durch `quantity` teilen.
#4. Verwenden Sie einen try-except-Block, um einen möglichen `ZeroDivisionError` zu behandeln, der auftreten kann, wenn `quantity` gleich 0 ist.
#5. Falls ein `ZeroDivisionError` auftritt, geben Sie eine Nachricht aus, die besagt, dass eine Teilung durch Null nicht möglich ist.

#Erwartetes Ergebnis:

#Das Programm sollte die Größe des SMS-Pakets für die Sendung berechnen oder eine Fehlermeldung ausgeben, wenn ein Versuch zur Teilung durch Null unternommen wird.

#Tipps:

#- Platzieren Sie im try-Block den Code, der einen Fehler verursachen könnte.
#- Geben Sie im except-Block den Typ des erwarteten Fehlers an und die Maßnahmen, die im Falle seines Auftretens ergriffen werden sollten.


pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError :
    print('Divide by zero completed!')