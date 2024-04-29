#Hier ist die Übersetzung Ihrer Anfrage vom Ukrainischen ins Deutsche:
#Erstellen Sie ein Python-Programm, das eine leere Liste initialisiert und diese mit bestimmten Werten an angegebenen Indizes füllt.
#Aufgaben:
#1. Erstellen Sie eine leere Liste `my_list`.
#2. Fügen Sie der Liste `my_list` folgende Elemente hinzu, indem Sie Indizes für deren Platzierung verwenden:
#   - An die Position mit dem Index 0 fügen Sie die ganze Zahl 2024 ein.
#   - An die Position mit dem Index 1 fügen Sie den String 'Python' ein.
#   - An die Position mit dem Index 2 fügen Sie die Fließkommazahl 3.12 ein.
#Erwartetes Ergebnis:
#Nach der Ausführung des Programms sollte die Liste `my_list` drei Elemente in der angegebenen Reihenfolge enthalten: eine ganze Zahl, einen String und eine Fließkommazahl.
#Tipps:
#- Sie können die Methode `insert()` verwenden, um Elemente an den entsprechenden Positionen in die Liste einzufügen.
#- Stellen Sie sicher, dass die Elemente in der richtigen Reihenfolge entsprechend den angegebenen Indizes hinzugefügt werden.

# Створення порожнього списку
my_list = []

# Додавання елементів за вказаними індексами
my_list.insert(0, 2024)   # Додаємо ціле число на позицію з індексом 0
my_list.insert(1, 'Python')  # Додаємо рядок на позицію з індексом 1
my_list.insert(2, 3.12)   # Додаємо дійсне число на позицію з індексом 2

# Виведення результату
print(my_list)