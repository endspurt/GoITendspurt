

#Schreiben Sie ein Python-Programm, das die Eigenschaften einer eingegebenen Zahl bestimmt: ob sie positiv und gerade, positiv und ungerade, negativ oder null ist.

#Aufgaben:

#1. Fordern Sie den Benutzer auf, eine ganze Zahl einzugeben, und speichern Sie diese in der Variablen `num`.
#2. Verwenden Sie verschachtelte Bedingungen, um die Zahl zu analysieren:
#   - Wenn die Zahl größer als 0 ist, überprüfen Sie, ob sie gerade oder ungerade ist:
#     - Wenn die Zahl gerade ist, d.h., der Rest der Division durch 2 gleich 0 ist, speichern Sie in der Variablen `result` den String "Positive even number".
 #    - Wenn die Zahl ungerade ist, d.h., der Rest der Division durch 2 gleich 1 ist, speichern Sie in der Variablen `result` den String "Positive odd number".
 #  - Wenn die Zahl kleiner als 0 ist, speichern Sie in der Variablen `result` den String "Negative number".
 #  - Wenn die Zahl gleich 0 ist, speichern Sie in der Variablen `result` den String "It is zero".

num = int(input("Enter a number: "))

if num > 0 :
    if num%2 != 0:
        result = "Positive odd number"
    else:
        result = "Positive even number"

elif num < 0: 
    result = "Negative number"
else:
    result = "It is zero"
