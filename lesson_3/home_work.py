a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = input("Выберите действие: + , -, *, / : ")
if c == "+":
    print(a, "+", b, "=", a + b)
elif c == "-":
    print(a, "-", b, "=", a - b)
elif c == "*":
    print(a, "*", b, "=", a * b)
elif c == "/" and not b == 0:
    print(a, "/", b, "=", a / b)
elif c == "/" and b == 0:
    print("На ноль делить нельзя")
else:
    print("Не верно выбрана команда")
