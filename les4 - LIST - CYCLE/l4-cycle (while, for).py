# ЦИКЛ
# WHILE по условию:                             (while n < 10:  )
first_list = [8, "4", 6, False]
# while n < 10:
# continue                                      # - пропуск условия
# break                                         # - остановка цикла

i = 0
while i < len(first_list):
    print(first_list[i])
    i += 1
# _______________________________________________________________
# FOR по количеству:                            (for elem in x:  )

#                                                for elem in range(10):
# x = range(5)                                   # x = [0, 1, 2, 3, 4,]
# x = range(2, 4)                                # x = [2, 3]
# x = range(5, 10, 2)                            # x = [5, 7, 9]

# for elem in x:
#   print(elem)
# else:                                          # сработает в конце цикла
#   print("end")

# x = enumerate(first_list)                      # индекс + значение
# x = [(0, 8), (1, "4"), (2, 6), (3, False)]     - print()

# for index, elem in enumerate(first_list):
#   print(index, "->", elem)
# 0 -> 8
# 1 -> 4
# 2 -> 6
# 3 -> False
# _______________________________________________________________
import random                                      #  random

# for _ in range(4):
#    print(random.randint(1, 100))                  # рандом по числам
#    print(random.choice(first_list))               # рандом одного элемента из списка
#    random.shuffle(first_list)                     # рандом списка
#    print(first_list)