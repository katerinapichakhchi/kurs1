# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]

import random

n = random.randint(3,10)
lst = []
a = []
for i in range(n):
    lst.append(random.randint(1,9))

a.append(lst[0])
a.append(lst[2])
a.append(lst[-2])
print(lst, '=>', a)

