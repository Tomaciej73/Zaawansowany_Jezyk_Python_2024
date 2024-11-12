import os
import sys
import time

def wypisz_statystyki(nazwa_pliku):
    """Funkcja wypisuje statystyki dla podanego pliku."""
    try:
        stat_info = os.stat(nazwa_pliku)
        print(f"os.stat({nazwa_pliku}):")
        print("\tRozmiar:", stat_info.st_size)
        print("\tWłaściciel, użytkownik o numerze UID=", stat_info.st_uid)
        print("\tUrządzenie:", stat_info.st_dev)
        print("\tOstatnio modyfikowany:", time.ctime(stat_info.st_mtime))
        print("-" * 40)
    except FileNotFoundError:
        print(f"Plik {nazwa_pliku} nie istnieje.")
        print("-" * 40)

def main():
    if len(sys.argv) < 2:
        print("Nie podano plików do sprawdzenia.")
        return

    for nazwa_pliku in sys.argv[1:]:
        wypisz_statystyki(nazwa_pliku)

if __name__ == "__main__":
    main()
