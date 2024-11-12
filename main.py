'''Zadanie 1'''
import time

def dekorator(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        end = time.time()
        print(f'Czas wykonania: {end - start} sekund')
        return wynik
    return wrapper

@dekorator
def metoda1():
    for i in range(1000000):
        pass

@dekorator
def metoda2():
    for i in range(1000000):
        print(i)

metoda1()
metoda2()

'''Zadanie 2'''
class IteratorLiczb:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            liczba = self.current
            self.current += 1
            return liczba
        else:
            raise StopIteration

iterator = IteratorLiczb(5)

for liczba in iterator:
    print(liczba)

'''Zadanie 3'''
class IteratorLiczb:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            liczba = self.current
            self.current += 1
            return liczba
        else:
            raise StopIteration

iterator = IteratorLiczb(100)

for liczba in iterator:
    print(liczba)

'''Zadanie 4'''
def przechwytuj_zerowe(funkcja):
    def wrapper(self, liczba):
        if liczba == 0:
            print("Nie można dodać zera do kolekcji.")
        else:
            funkcja(self, liczba)
    return wrapper

class KolekcjaLiczb:
    def __init__(self):
        self.liczby = []

    @przechwytuj_zerowe
    def dodaj(self, liczba):
        self.liczby.append(liczba)

    def __iter__(self):
        return (liczba for liczba in self.liczby if liczba > 0)

kolekcja = KolekcjaLiczb()

kolekcja.dodaj(5)
kolekcja.dodaj(0) #Nie doda tego ez
kolekcja.dodaj(-3)
kolekcja.dodaj(7)

for liczba in kolekcja:
    print(liczba)

'''Zadanie 5'''
import random
from abc import ABC, abstractmethod

class ZestawDanych(ABC):
    @abstractmethod
    def generuj_dane(self):
        pass

class DaneLosowe(ZestawDanych):
    def __init__(self, liczba_danych, min_wartosc=0, max_wartosc=100):
        self.liczba_danych = liczba_danych
        self.min_wartosc = min_wartosc
        self.max_wartosc = max_wartosc

    def generuj_dane(self):
        for _ in range(self.liczba_danych):
            yield random.randint(self.min_wartosc, self.max_wartosc)

dane_losowe = DaneLosowe(10, 1, 50)

for liczba in dane_losowe.generuj_dane():
    print(liczba)

'''Zadanie 6'''
class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        a, b = 0, 1
        for _ in range(self.n):
            yield a
            a, b = b, a + b

fibonacci = Fibonacci(10)

for liczba in fibonacci:
    print(liczba)
