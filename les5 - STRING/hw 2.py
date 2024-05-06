y = 0
while y == 0:
    a = int(input("Введите первое число: "))
    c = input("Выберите действие: + , -, *, / : ")
    b = int(input("Введите второе число: "))
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
    it = input("Хотите продолжить работу калькулятора? y/n: ")
    if it == "y":
        y = 0
    else:
        y = 1
        print("Спасибо!")