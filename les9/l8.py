def add(x: int, y: int) -> int:                                                                             # Пример 1
    return x + y


sum_of_two_elements = add                                                                   # отправка для функции
print(add(1, 2))
print(sum_of_two_elements(1, 2))


from typing import Callable                                                                                 # Пример 2


def apply_operation(data: list, operation: Callable) -> list:                               # функция в функции
    res = []
    for element in data:
        res.append(operation(element))
    return res


def square(number: int) -> int:
    return number**2


def double(number: int) -> int:
    return number*2


numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_operation(numbers, square)
double_numbers = apply_operation(numbers, double)

print(squared_numbers)
print(double_numbers)
# ____________________________________________________________________________________________________________________________
print("          ****                 ___2_")                # 6 ! = 1*2*3*4*5*6                           # Факториал


def factorial(number: int) -> int:
    print(number)
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)


print(factorial(4))
# ____________________________________________________________________________________________________________________________
print("          ****                 ___3_")                                              # Анонимные функции / lambda

double = lambda x: x**2             # тоже самое что _____|     def double(x):
print(double(5))                    #                     |         return x * 2

chek_even = lambda x: True if x % 2 == 0 else False
print(chek_even(2))
print(chek_even(3))

numbers = [1, 2, 3, 4, 5]
square_numbers = map(lambda x: x**2, numbers)                                                          # метод     map
result = list(square_numbers)
print(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filters_numbers = filter(lambda x: x % 2 == 0, numbers)                                              # метод    filter
result = list(filters_numbers)
print(result)

ages = [21, 22, 23]
names = ["Andriy", "Alexandr", "Katya"]
test = ["1", "2", "3"]
zipped = zip(names, ages, test)                                                                        # метод     zip
result = list(zipped)
print(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filters_numbers = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
result = list(filters_numbers)
print(result)
# ____________________________________________________________________________________________________________________________
print("          ****                 ___4_")                                                     # Генераторы / yield

def my_generator():
    yield 1
    yield 2
    yield 3


def fibonachi_generator(n):                                                                    # Генератор Фибоначи
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


fibonachi = fibonachi_generator(50)

for value in fibonachi:
    print(value, end=" ")


