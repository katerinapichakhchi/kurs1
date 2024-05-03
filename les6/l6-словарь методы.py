a = dict.fromkeys([1, "a", 2, "b"], "test")
print(a)

d = {}
for elem in [1, "a", 2, "b"]:
    d[elem] = []
print(d)

d["a"].append(1)
print(a)

d = {
    "name": "Eugene"
}
d["age"] = 27                           # добавить/заменить в словарь
print(d.get("age", 27))                 # добавить/заменить в словарь
print(d.items())
print(d.keys())

for key, value in d.items():
    print(key)
    print(value)

print(d.values())
print(d.pop("name"))                           # удалить ключ
print(d)

import collections

d = collections.OrderedDict({                   # порядок
    "name": "Eugene",
    "age": "27"
})
d.popitem(last=False)                           # удаляет пару
print(d)

Point = collections.namedtuple("Point", "x y")
p = Point(1, 2)
print(type(p))
print(p.x)
print(p.y)


