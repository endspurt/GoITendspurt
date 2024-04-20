import datetime

def get_days_from_today(date):
    """
    Berechnet die Anzahl der Tage zwischen einem gegebenen Datum und dem heutigen Datum.
    
    Parameter:
        date (str): Das Datum im Format 'JJJJ-MM-TT'.
    
    Rückgabe:
        int: Die Anzahl der Tage zwischen dem gegebenen Datum und dem heutigen Datum.
            Das Ergebnis ist negativ, wenn das gegebene Datum nach dem heutigen liegt.
    """
    # Umwandlung des Eingabestrings in ein datetime-Objekt
    input_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    # Erhalt des heutigen Datums
    today = datetime.datetime.today().date()
    # Berechnung der Differenz in Tagen
    delta = input_date - today
    return delta.days

# Beispiel zur Verwendung der Funktion
# Diese Aufrufe zeigen, wie die Funktion arbeitet. Die Ausgabe wird abhängig vom heutigen Datum variieren.
print(get_days_from_today("2020-10-09"))  # Beispieloutput könnte variieren
print(get_days_from_today("2023-12-25"))  # Beispieloutput könnte variieren
