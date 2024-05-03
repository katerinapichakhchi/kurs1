#                                                Байт
s = "Hello, world!"
b = s.encode("utf-8")
print(type(b))
print(b)
s = b.decode("utf-8")
print(type(s))
print(s)

#                                               Кортеж(tuple) - не изменяемый тип данных
t = (1,)
i = (1)
print(type(t), type(i))

t = tuple("help")
print(t)

t = (1, 2, 3)
print(len(t), t[0])
t[2].append(3)
print(t)

a = 10
b = 20
a, b = b, a
print(a, b)

a = (1, 2, 3)
if 1 in a:
    print("True")

