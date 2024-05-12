class IDException(Exception):
    pass

def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("employee_id muss mit '01' beginnen")
    id_list.append(employee_id)
    return id_list

# Beispiel zur Nutzung der Funktion add_id
try:
    ids = []
    add_id(ids, '0123456')  # Korrektes Hinzufügen
    print(add_id(ids, '0123457'))  # Korrektes Hinzufügen
    print(add_id(ids, '9901234'))  # Sollte eine IDException auslösen
except IDException as e:
    print(e)  # Ausgabe der Fehlermeldung

'''Erstelle eine Klasse IDException, die von der Klasse Exception erbt. Implementiere außerdem die Funktion add_id(id_list, employee_id), 
die einen Benutzeridentifikator employee_id zur Liste id_list hinzufügt und die aktualisierte Liste id_list zurückgibt.

Die Funktion add_id wird eine eigene Ausnahme IDException auslösen, wenn employee_id nicht mit '01' beginnt, 
ansonsten wird employee_id zur Liste id_list hinzugefügt.

Die Klasse IDException erbt von Exception, was es ermöglicht, eine spezifische Ausnahme für ID-bezogene Fehler zu definieren.
Die Funktion add_id prüft, ob der employee_id mit '01' beginnt. Falls nicht, wird eine IDException mit einer passenden Fehlermeldung ausgelöst.
Wenn der employee_id korrekt ist, wird er zur Liste id_list hinzugefügt und die aktualisierte Liste zurückgegeben.
Im Beispiel wird die Funktion verwendet, um IDs hinzuzufügen und zu demonstrieren, wie die Funktion auf eine ungültige ID reagiert, indem sie eine Ausnahme auslöst.'''