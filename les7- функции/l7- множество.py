if __name__ == "__main__":
    my_set ={1, 2, 3, 4, 1, 2, 3, 4}
    my_set.add(5)                                                                       # добавить элемент
    my_set.remove(5)                                                                    # удалить элемент
    my_set.discard(6)
    my_set.pop()
    print(my_set)

first_set = {1, 2, 3, 4}
second_set = {4, 5, 6}

new_set = first_set.union(second_set)                                               # уникальные элементы с двух множеств
print(new_set)

new_set = first_set.intersection(second_set)                                           # сравнение
print(new_set)
new_set = first_set.difference(second_set)
print(new_set)
first_set.clear()

lst = [1, 2, 3, 1, 2, 3]                                                                 # из листа в множество
new_set = set(lst)
print(new_set)

fros = frozenset([1, 2, 3, 1, 2, 3])                                                     # неизменная
print(fros)