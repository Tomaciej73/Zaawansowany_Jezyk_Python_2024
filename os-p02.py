import os
import sys

def sprawdz_plik(plik):
    """Sprawdza dostępność pliku i wypisuje odpowiednie informacje."""
    print(f"Testowanie pliku: {plik}")
    print("Plik istnieje: ", os.access(plik, os.F_OK))
    print("Plik można czytać: ", os.access(plik, os.R_OK))
    print("Plik jest zapisywalny: ", os.access(plik, os.W_OK))
    print("Plik jest wykonywalny: ", os.access(plik, os.X_OK))
    print("-" * 40)

def main():
    if len(sys.argv) < 2:
        print("Nie podano żadnych plików do sprawdzenia.")
        return

    for plik in sys.argv[1:]:
        if os.path.exists(plik):
            sprawdz_plik(plik)
        else:
            print(f"Plik {plik} nie istnieje.")
            print("-" * 40)

if __name__ == "__main__":
    main()
