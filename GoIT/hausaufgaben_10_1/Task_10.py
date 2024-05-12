from collections import UserList

class AmountPaymentList(UserList):
    def amount_payment(self):
        summe = 0
        for value in self.data:  # Zugriff auf die Elemente über self.data, weil UserList die Daten hier speichert
            if value > 0:
                summe += value
        return summe

# Beispiel zur Nutzung der Klasse AmountPaymentList
payments = AmountPaymentList([1, -3, 4, 5, -2, 3])
print(payments.amount_payment())  # Sollte 13 ausgeben, da nur positive Werte summiert werden

'''from collections import UserList

class AmountPaymentList(UserList):
    def amount_payment(self):
        summe = 0
        for value in self.data:  # Zugriff auf die Elemente über self.data, weil UserList die Daten hier speichert
            if value > 0:
                summe += value
        return summe

# Beispiel zur Nutzung der Klasse AmountPaymentList
payments = AmountPaymentList([1, -3, 4, 5, -2, 3])
print(payments.amount_payment())  # Sollte 13 ausgeben, da nur positive Werte summiert werden
In diesem Code:

Die Klasse AmountPaymentList erbt von UserList. Dies ermöglicht uns, die Liste von Zahlungen 
als eine Liste von Objekten zu verwalten.
Die Methode amount_payment summiert alle positiven Werte in self.data und gibt diese Summe zurück.
Ein Beispiel demonstriert, wie die Klasse verwendet wird, indem ein Objekt der Klasse AmountPaymentList 
mit einigen Zahlungen initialisiert und die amount_payment Methode aufgerufen wird.'''