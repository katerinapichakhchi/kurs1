list_1 = [12, 3, 4, 10]
print("Пример 1:", list_1, "=>", end=" ")
if len(list_1)>0:
    list_1.insert(0, list_1.pop(-1))
print(list_1)

list_2 = [1]
print("Пример 2:", list_2, "=>", end=" ")
if len(list_2)>0:
    list_2.insert(0, list_2.pop(-1))
print(list_2)

list_3 = [12, 3, 4, 10, 8]
print("Пример 3:", list_3, "=>", end=" ")
if len(list_3)>0:
    list_3.insert(0, list_3.pop(-1))
print(list_3)

list_4 = []
print("Пример 4:", list_4, "=>", end=" ")
if len(list_4)>0:
    list_4.insert(0, list_4.pop(-1))
print(list_4)
