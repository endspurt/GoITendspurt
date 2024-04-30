

#Aufgaben:

#1. Fordern Sie den Benutzer auf, eine ganze Zahl zwischen 0 und 100 einzugeben. Speichern Sie diese Zahl in der Variablen `num`.
#2. Verwenden Sie eine `while`-Schleife, um die Summe aller Zahlen von 1 bis zur eingegebenen Zahl einschließlich zu berechnen.
#3. Speichern Sie das Ergebnis in der Variablen `sum`.

#Erwartetes Ergebnis:

#Das Programm soll die Summe aller Zahlen von 1 bis `num` einschließlich berechnen und diese Summe in der Variablen `sum` speichern.

#Tipps:

#Initialisieren Sie die Variable `sum` mit dem Wert 0 vor Beginn der Schleife.

num = int(input("Enter the integer (0 to 100): "))
sum = 0

while num !=0 :
    
    sum=sum+num
    num= num-1 
    