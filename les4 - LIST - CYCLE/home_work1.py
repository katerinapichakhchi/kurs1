# Написати програму, яка переміщає всі нулі у кінець списку.
# Ваше завдання — змінити список так, щоб усі нулі опинилися наприкінці списку.
# Порядок ненульових чисел має зберегтися!

lst = [1, 0, 13, 0, 0, 0, 5]
a = []
n = lst.count(0)
for i in range(len(lst)):
    if not lst[i] == 0:
        a.append(lst[i])

for i in range(n):
    a.append(0)

print(lst, "=>", a)
