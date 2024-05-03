#                                                       Словарь
import copy

a = {
    "name": "Eugene",
    "age": 27,
    "favorite_fruits": ["apple", "banana"]
}
print(a["name"])                 # по ключу
print(len(a))                    # кол-во ключей
print("name" in a)               # проверка ключа в словаре

b = dict(name="Eugene", age=27)
print(b)

print(hash("Hello"))

import copy
a = {
    "name": "Eugene",
    "fruites": {
        "sort": "red apple"
    }
}
print(a["fruites"]["sort"])

b = a.copy()
b = copy.deepcopy(a)
