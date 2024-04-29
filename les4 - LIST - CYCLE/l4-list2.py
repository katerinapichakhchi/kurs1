first_list = [ 8, 2, 4, 5, 6, 7, 6]
#first_list = [bool(8), 2, 4, 5, 6, 7, False]
#first_list.sort()                 # - сортировка списка

#first_list = [2, 4, 5, 6, 7]
#first_list = first_list[1:3]      #list_ part срез
first_list[1:3] = [6, 7, 8]       # change element замена елемента
#print(first_list)
#####
#count
#print(first_list.count(6))        # count element = 6
#print(first_list.index(6))        # find index element
#first_list.sort()                 # sorting

import copy                        # - библиотека для копирования
#second_list = first_list.copy()    # - копирование в новую ячейку (разные id)
#second_list = copy.deepcopy(first_list)
#second_list.clear()               # -очистка списка
#print(min(first_list))             # - минимальное значение
#print(max(first_list))             # - максимальное значение
#print(all(first_list))
#print(any(first_list))
print(first_list)
#print(second_list)
#print(id(first_list) == id(second_list))
#print(id(first_list[-1]) == id(second_list[-1]))



