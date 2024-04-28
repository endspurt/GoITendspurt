import sys
from pathlib import Path
from colorama import Fore, Style, init

init()  # Initialisiert colorama, um die Farben auf der Konsole zu aktivieren

def print_directory_structure(path, indent=''):
    path = Path(path)
    if path.is_dir():
        entries = list(path.iterdir())
        entries.sort(key=lambda x: (x.is_file(), x.name))
        
        for entry in entries:
            if entry.is_dir():
                # Ausgabe für ein Verzeichnis
                print(f"{indent}{Fore.BLUE}{entry.name}{Style.RESET_ALL}")
                # Rekursiver Aufruf für das Unterverzeichnis mit erhöhter Einrückung
                print_directory_structure(entry, indent + '    ')
            else:
                # Ausgabe für eine Datei
                print(f"{indent}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Verwendung: python hw03.py <Pfad>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not Path(directory_path).is_dir():
        print(f"Der Pfad {directory_path} existiert nicht oder ist kein Verzeichnis.")
        sys.exit(1)

    print_directory_structure(directory_path)

