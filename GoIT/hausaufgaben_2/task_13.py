

#Aufgaben:

#1. Erstellen Sie eine Funktion `number_of_groups`, die zwei Argumente annimmt: `n` - die Gesamtzahl der Personen und `k` - die Anzahl der Gewinner.
#2. In der Funktion `number_of_groups`, verwenden Sie die Funktion `factorial` zur Berechnung der Faktoriellen gemäß der Kombinationsformel: Cnk = n! / ((n - k)! · k!).
#3. Die Berechnung erfolgt durch den Aufruf der Funktion `factorial`, um die Faktoriellen von `n`, `n - k` und `k` zu erhalten.
#4. Geben Sie das Ergebnis dieser Berechnung zurück.

#Erwartetes Ergebnis:

#Die Funktion `number_of_groups` gibt die Anzahl möglicher unterschiedlicher Gewinnerlisten zurück.

#Beachten Sie, wie groß die Werte für die Faktoriellen werden können. Rekursive Ausdrücke sollten immer vorsichtig in Berechnungen verwendet werden, um ein Speicherüberlauf zu vermeiden.



def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    # Berechnen der Faktoriellen für n, (n-k) und k
    factorial_n = factorial(n)
    factorial_n_k = factorial(n - k)
    factorial_k = factorial(k)
    
    # Anwendung der Kombinationsformel: Cnk = n! / ((n - k)! * k!)
    combination = factorial_n // (factorial_n_k * factorial_k)
    
    return combination

# Beispielaufruf der Funktion
n = 50  # Gesamtzahl der Personen
k = 7   # Anzahl der Gewinner
print(number_of_groups(n, k))

