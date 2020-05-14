1.
from sys import argv


def salary():
    try:
        prod, rate, prize = map(int, argv[1:])
        print(f"Заработная плата - {prod * rate + prize}")
    except ValueError:
        print("Введите 3 числа. Не строки или другие характеристики")


salary()

2.
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(new_list)

3.
new_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(new_list)

4.
from random import randint

my_list = [randint(0, 50) for i in range(15)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Случайный список\n{my_list}\nНе повторяющийся список\n{new_list}")

5.
from functools import reduce


def my_list(el_1, el_2):
    return el_1 * el_2


new_list = [el for el in range(100, 1001, 2)]
print(f"Список\n{new_list}\nПроизведение четных элементов\n{reduce(my_list, new_list)}")

6.
from itertools import count, cycle

my_list = list(input("Введите элементы списка и числа через пробел: ").split())
el = cycle(my_list)

for n in count():
    if n > 10:
        break
    else:
        print(f"{n} - {next(el)}")

7.
from itertools import count
from math import factorial


def f_gen():
    for el in count(1):
        yield factorial(el)


gen = f_gen()
n = 0
for i in gen:
    if n == 8:
        break
    else:
        n += 1
        print(f"Factorial {n}={i}")
