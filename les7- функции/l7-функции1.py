def add_number(a, b):
    summ = a + b
    return summ


if __name__ == "__main__":
    add_number(1, 2) # вызов функции
    sum_of_elements = add_number(1, 2)        # передача функции №1
    sum_of_elements2 = add_number(b=1, a=2)         # передача функции №2
    print(sum_of_elements, sum_of_elements2)


def add_number(a, b=3):
    summ = a + b
    return summ


if __name__ == "__main__":
    sum_of_elements = add_number(1)
    print(sum_of_elements)


def append(a=[]): # не использовать с непостоянніми данніми
    a.append(1)
    return a


if __name__ == "__main__":
    lst = append()
    print(lst)
    lst = append()
    print(lst)
    lst = append()
    print(lst)


def append(a):
    a.append(1)


if __name__ == "__main__":
    new_lst = []
    lst = append(new_lst)
    print(lst)
    print(new_lst)


def append(a: int) -> int:
    return 123


if __name__ == "__main__":
    new_lst = 123
    test = append(new_lst)
    print(new_lst)
