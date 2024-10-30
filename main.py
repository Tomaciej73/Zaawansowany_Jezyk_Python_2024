'''Zadanie 1'''
cities = ['Warsaw', 'Krakow', 'Gdansk']
it = iter(cities)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

'''Zadanie 2'''
import sys
n = int(sys.argv[1])
print(sum(range(1, n+1)))

'''Zadanie 3'''
n = int(sys.argv[1])
print(sum(range(1, n+1)))

'''Zadanie 4'''
celsius = [0, 20, 30]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)

'''Zadanie 5'''
fahrenheit = [32, 68, 86]
celsius = list(map(lambda f: (f - 32) * 5/9, fahrenheit))
print(celsius)

'''Zadanie 6'''
from itertools import islice

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(filter(lambda x: x % 2 == 1, fibonacci(10))))

'''Zadanie 7'''
from itertools import islice

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(filter(lambda x: x % 2 == 1, fibonacci(10))))

'''Zadanie 8'''
from itertools import islice

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(filter(lambda x: x % 2 == 1, fibonacci(10))))

'''Zadanie 9'''
from functools import reduce

numbers = [3, 5, 7, 2, 8]
largest = reduce(lambda a, b: a if a > b else b, numbers)
print(largest)

'''Zadanie 10'''
from functools import reduce

numbers = [3, 5, 7, 2, 8]
largest = reduce(max, numbers)
print(largest)
