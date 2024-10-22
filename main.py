import random
import math
import re
'''Zadanie 1.1'''
def func(a,b=4,c=5):
    print(a,b,c)
func(1,2)
#output: 1 2 5

'''Zadanie 1.2'''
def func(a,b,c=5):
    print(a,b,c)
func(1,c=3,b=2)
#output: 1 2 3

'''Zadanie 1.3'''
def func(a,*args):
    print(a,args)
func(1,2,3)
#output: 1 (2, 3)

'''Zadanie 1.4'''
def func(a,**kwargs):
    print(a,kwargs)
func(a=1,c=3,b=2)
#output: 1 {'c': 3, 'b': 2}

'''Zadanie 1.5'''
def func(a,b,c=3,d=4):
    print(a,b,c,d)
func(1,*(5,6))
#output: 1 5 6 4

#====================================================================================

'''Zadanie 2.1'''
def mult(iterable):
    if not iterable:
        raise ValueError("Argument nie może być pusty.")
    product = 1
    for element in iterable:
        product *= element
    return product
def main():
    wynik1 = mult([3, 5, 7])
    wynik2 = mult(range(2, 8, 2))
    print(f"Iloczyn elementów [3, 5, 7] to: {wynik1}")
    print(f"Iloczyn elementów range(2, 8, 2) to: {wynik2}")
''' output:
Iloczyn elementów [3, 5, 7] to: 105
Iloczyn elementów range(2, 8, 2) to: 48
'''
if __name__ == "__main__":
    main()

'''Zadanie 2.2'''
def mult_ints(iterable):
    if not iterable:
        raise ValueError("Argument nie może być pusty.")
    product = 1
    has_int = False
    for element in iterable:
        if isinstance(element, int):
            product *= element
            has_int = True
    if not has_int:
        raise ValueError("Brak liczb całkowitych w podanym iterowalnym obiekcie.")
    return product
def main():
    try:
        wynik1 = mult_ints((3, 3.14, 5, "abc", 7))
        print(f"Iloczyn liczb całkowitych w (3, 3.14, 5, 'abc', 7) to: {wynik1}")
    except ValueError as e:
        print(e)

    try:
        wynik2 = mult_ints([1, 2, 3, 4.5, 5])  # Lista
        print(f"Iloczyn liczb całkowitych w [1, 2, 3, 4.5, 5] to: {wynik2}")
    except ValueError as e:
        print(e)

    try:
        wynik3 = mult_ints({2, 3, 4, 5.5, 6})  # Zbiór
        print(f"Iloczyn liczb całkowitych w {2, 3, 4, 5.5, 6} to: {wynik3}")
    except ValueError as e:
        print(e)

    try:
        wynik4 = mult_ints(range(1, 5))
        print(f"Iloczyn liczb całkowitych w range(1, 5) to: {wynik4}")
    except ValueError as e:
        print(e)
''' output:
Iloczyn liczb całkowitych w (3, 3.14, 5, 'abc', 7) to: 105
Iloczyn liczb całkowitych w [1, 2, 3, 4.5, 5] to: 30
Iloczyn liczb całkowitych w (2, 3, 4, 5.5, 6) to: 144
Iloczyn liczb całkowitych w range(1, 5) to: 24
'''

if __name__ == "__main__":
    main()

'''Zadanie 2.3'''
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
def main():
    print(multiply(3, 5, 7))
#output: 105
if __name__ == "__main__":
    main()

'''Zadanie 2.4'''
def multiply_ints(*args):
    result = 1
    for num in args:
        if isinstance(num, int):
            result *= num
    return result
def main():
    print(multiply_ints(3, 3.14, 5, "abc", 7))
#output: 105
if __name__ == "__main__":
    main()

'''Zadanie 2.5'''
def make_car(firma, model, **kwargs):
    car = {'firma': firma, 'model': model}
    car.update(kwargs)
    return car
def main():
    cars = [
        make_car("Kia", "Picanto", kolor="cafe mocca", poj_silnika=900),
        make_car("Toyota", "Corolla", kolor="czerwony", rok=2020),
        make_car("Ford", "Focus", kolor="niebieski", poj_silnika=1600)
    ]
    for car in cars:
        print(car)
''' output:
{'firma': 'Kia', 'model': 'Picanto', 'kolor': 'cafe mocca', 'poj_silnika': 900}
{'firma': 'Toyota', 'model': 'Corolla', 'kolor': 'czerwony', 'rok': 2020}
{'firma': 'Ford', 'model': 'Focus', 'kolor': 'niebieski', 'poj_silnika': 1600}
'''
if __name__ == "__main__":
    main()

#====================================================================================

'''Zadanie 3.1'''
divisible_by_7 = [num for num in range(1, 1001) if num % 7 == 0]
print(divisible_by_7)
#output: [7, 14, 21, 28, 35, 42, 49....]

'''Zadanie 3.2'''
contains_3 = [num for num in range(1, 1001) if '3' in str(num)]
print(contains_3)
#output: [3, 13, 23, 30, 31, 32, 33....]

'''Zadanie 3.3'''
text = "Karkulowski Tomasz"
space_count = text.count(' ')
print(space_count)
#output: 1

'''Zadanie 3.4'''
text = "Tomasz Karkulowski raz dwa trzy"
short_words = [word for word in text.split() if len(word) < 4]
print(short_words)
#output: ['raz', 'dwa']

'''Zadanie 3.5'''
lista_a = [1, 2, 3, 4]
lista_b = [2, 3, 4, 5]
common_numbers = [num for num in lista_a if num in lista_b]
print(common_numbers)
#output: [2, 3, 4]

'''Zadanie 3.6'''
n = 20
divisible_by_3_or_5 = [num for num in range(1, n + 1) if num % 3 == 0 or num % 5 == 0]
print(divisible_by_3_or_5)
#output: [3, 5, 6, 9, 10, 12, 15, 18, 20]

'''Zadanie 3.7'''
n = 10
lista = [round(random.uniform(0, 100), 2) for _ in range(n)]
print(lista)
#output: [24.43, 91.93, 25.16, 7.83, 38.59, 29.96, 93.57, 6.94, 14.81, 0.05]

positive_numbers = [num for num in lista if num > 0]
print(positive_numbers)
#output: [24.43, 91.93, 25.16, 7.83, 38.59, 29.96, 93.57, 6.94, 14.81, 0.05]

int_numbers = [int(num) for num in lista if num > 0]
print(int_numbers)
#output: [24, 91, 25, 7, 38, 29, 93, 6, 14, 0]

floor_values = [math.floor(num) for num in lista]
print(floor_values)
#output: [24, 91, 25, 7, 38, 29, 93, 6, 14, 0]

ceil_values = [math.ceil(num) for num in lista]
print(ceil_values)
#output: [25, 92, 26, 8, 39, 30, 94, 7, 15, 1]

log_values = [math.log(num) for num in lista if num > 0]
print(log_values)
#output: [3.195811885269649, 4.521027417875663 .....]

#====================================================================================

'''Zadanie 4.1'''
text = "Żółte jaki lubią krzyczeć i ziewać, a wczoraj jodłowały podczas jedzenia batatów."
consonants = [char for char in text if char.isalpha() and char.lower() not in 'aeiouyąęó']
print(consonants)
#output: ['Ż', 'ł', 't', 'j', 'k', 'l', 'b', 'k', 'r', 'z', 'c', 'z', 'ć', 'z', 'w', 'ć', 'w', 'c', 'z', 'r', 'j', 'j', 'd', 'ł', 'w', 'ł', 'p', 'd', 'c', 'z', 's', 'j', 'd', 'z', 'n', 'b', 't', 't', 'w']

'''Zadanie 4.2'''
elements = ["hi", 4, 8.99, "apple", ("t,b", "n")]
index_value_tuples = [(index, value) for index, value in enumerate(elements)]
print(index_value_tuples)
#output: [(0, 'hi'), (1, 4), (2, 8.99), (3, 'apple'), (4, ('t,b', 'n'))]

'''Zadanie 4.3'''
sentence = "W 1984 roku w 13 przypadkach doszło do protestu, w którym wzięło udział ponad 1000 osób."
numbers = re.findall(r'\d+', sentence)
print(numbers)
#output: ['1984', '13', '1000']

'''Zadanie 4.4'''
numbers = [6, 8, 11]
even_odd_list = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(even_odd_list)
#output: ['even', 'even', 'odd']

'''Zadanie 4.5'''
lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_b = [2, 7, 1, 12]
matching_tuples = [(a, a) for a in lista_a for b in lista_b if a == b]
print(matching_tuples)
#output: [(1, 1), (2, 2), (7, 7)]

'''Zadanie 4.6'''
divisible_numbers = [num for num in range(1, 1001) if any(num % d == 0 for d in range(2, 10))]
print(divisible_numbers)
#output: [2, 3, 4, 5, 6, 7, 8, 9, 10, 12....]

