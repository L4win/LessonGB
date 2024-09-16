from itertools import count
from math import factorial


def fact_generator():
    for el in count(1):
        yield factorial(el)


generator = fact_generator()
x = 0

for i in generator:
    if x == 15:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")
