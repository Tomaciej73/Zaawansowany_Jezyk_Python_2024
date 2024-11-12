import os

def main():
    print("Separator ścieżek: ", os.path.pathsep)
    print("Separator katalogów w ścieżce: ", os.path.sep)
    print("Separator nazwy pliku i jego rozszerzenia: ", os.path.extsep)
    print("Oznaczenie bieżącego katalogu: ", os.path.curdir)
    print("Oznaczenie nadrzędnego katalogu: ", os.path.pardir)
    print("Ścieżka do pustego urządzenia: ", os.path.devnull)
    print("Domyślne     ścieżki dla plików wykonywalnych: ", os.path.defpath)

if __name__ == "__main__":
    main()