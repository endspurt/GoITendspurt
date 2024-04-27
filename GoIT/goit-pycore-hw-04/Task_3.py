import sys
from pathlib import Path
from colorama import Fore, Style

def print_directory_structure(path, prefix=''):
    path = Path(path)
    entries = list(path.iterdir())

    for entry in entries:
        connector = "┣" if entry != entries[-1] else "┗"
        if entry.is_dir():
            # Ausgabe für ein Verzeichnis
            print(f"{prefix}{connector} {Fore.BLUE}{entry.name}{Style.RESET_ALL}")
            # Rekursiver Aufruf für das Unterverzeichnis
            print_directory_structure(entry, prefix=prefix + " ┃ ")
        else:
            # Ausgabe für eine Datei
            print(f"{prefix}{connector} {Fore.GREEN}{entry.name}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bitte geben Sie den Pfad zum Verzeichnis als Argument an.")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    if not Path(directory_path).is_dir():
        print(f"Der Pfad {directory_path} existiert nicht oder ist kein Verzeichnis.")
        sys.exit(1)

    print_directory_structure(directory_path)
