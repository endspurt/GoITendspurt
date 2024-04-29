#Hier ist die Übersetzung Ihres Textes vom Ukrainischen ins Deutsche:

#Erstellen Sie ein Python-Programm, das eine Reihe von Operationen mit zwei Listen durchführt, wobei deren Inhalt und die Reihenfolge der Elemente geändert werden.

#Aufgaben:

#1. Mit zwei Listen `my_list` und `some_data`, verwenden Sie die Methode `extend`, um alle Elemente aus der Liste `some_data` am Ende der Liste `my_list` hinzuzufügen.
#2. Verwenden Sie die Methode `insert`, um den String 'Python' an der Position mit dem Index 1 in der Liste `my_list` hinzuzufügen.
#3. Verwenden Sie die Methode `reverse`, um die Reihenfolge der Elemente in der Liste `my_list` umzukehren.

#Erwartetes Ergebnis:

#Nach der Ausführung des Programms sollte die Liste `my_list` die angegebenen Änderungen anzeigen.

# Визначення двох списків
my_list = [2024, 3.12]
some_data = ['Python']

# Додавання всіх елементів з some_data до кінця my_list за допомогою методу extend
my_list.extend(some_data)

# Додавання 'Python' на позицію з індексом 1 у списку my_list
my_list.insert(1, 'Python')

# Розвертання порядку елементів у списку my_list за допомогою методу reverse
my_list.reverse()

# Вивід кінцевого стану списку my_list
print(my_list)
