


#Aufgaben:

#1. Erstellen Sie eine Funktion namens `first`, die einen obligatorischen Argument `size` und eine beliebige Anzahl von Positionsargumenten annimmt. Die Funktion sollte die Summe zurückgeben: `size` + Anzahl der Positionsargumente.
#2. Erstellen Sie eine Funktion namens `second`, die ebenfalls einen obligatorischen Argument `size` und eine beliebige Anzahl von Schlüsselwortargumenten annimmt. Die Funktion sollte die Summe zurückgeben: `size` + Anzahl der Schlüsselwortargumente.
#3. Verwenden Sie in beiden Funktionen die speziellen Syntaxe `*` für Positionsargumente und `**` für Schlüsselwortargumente.

#Erwartetes Ergebnis:

#Die Funktionen sollten korrekt die Summe von `size` und der Anzahl der übergebenen Argumente berechnen.

#Tipps:

#- `*args` in der Funktion `first` bedeutet, dass die Funktion eine beliebige Anzahl von Positionsargumenten annehmen kann.
#- `**kwargs` in der Funktion `second` bedeutet, dass die Funktion eine beliebige Anzahl von Schlüsselwortargumenten annehmen kann.
#- Verwenden Sie die Funktion `len`, um die Anzahl der Positions- oder Schlüsselwortargumente zu bestimmen.


def first(size, *args):
    return size + len(args)

def second(size, **kwargs):
    return size + len(kwargs)