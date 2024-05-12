from collections import UserDict

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:  # self.data, da UserDict das Wörterbuch in der Eigenschaft 'data' speichert
            if self.data[key] == value:
                keys.append(key)
        return keys

# Beispiel zur Nutzung der Klasse LookUpKeyDict
my_dict = LookUpKeyDict(one=1, two=2, three=3, another_one=1)
print(my_dict.lookup_key(1))  # Sollte ['one', 'another_one'] ausgeben
print(my_dict.lookup_key(2))  # Sollte ['two'] ausgeben

'''Zuerst müssen wir sicherstellen, dass wir die UserDict Klasse aus 
dem Modul collections importieren, da diese eine bequemere und objektorientierte Möglichkeit bietet, Wörterbücher zu verwalten.
In diesem Code:

Die Klasse LookUpKeyDict erbt von UserDict, was die Verwaltung von Schlüsseln 
und Werten in der Klasse einfacher macht.
Die Methode lookup_key durchsucht das interne Wörterbuch self.data nach allen Schlüsseln, 
die mit dem angegebenen Wert übereinstimmen.
Ein Beispiel demonstriert, wie die Klasse verwendet wird, indem ein Objekt der Klasse LookUpKeyDict 
mit einigen Schlüssel-Wert-Paaren initialisiert und die lookup_key Methode aufgerufen wird.'''
