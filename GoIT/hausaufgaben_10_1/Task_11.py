from collections import UserString

class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:  # Zugriff auf den String über self.data
            if char.isdigit():
                count += 1
        return count

# Beispiel zur Nutzung der Klasse NumberString
example_string = NumberString("Hallo 1234 Welt 567")
print(example_string.number_count())  # Sollte 7 ausgeben

'''Übersetzte Anweisung:
Erstelle eine Klasse NumberString, die von der Klasse UserString erbt. Definiere für sie eine Methode number_count(self), die die Anzahl der Ziffern im String zählt.

Python-Code:

Zuerst müssen wir die Klasse UserString aus dem Modul collections importieren, um von deren Funktionalitäten zu profitieren.
In diesem Code:

Die Klasse NumberString erbt von UserString. Dies ermöglicht eine einfache Erweiterung der String-Funktionalitäten.
Die Methode number_count durchläuft jeden Charakter in self.data, prüft, ob es sich um eine Ziffer handelt (isdigit()), und zählt diese.
Ein Beispiel demonstriert die Verwendung der Klasse NumberString, indem ein Objekt mit einem String initialisiert wird, der Buchstaben und Zahlen enthält. 
Die Methode number_count wird aufgerufen, um die Anzahl der Ziffern im String zu bestimmen.'''