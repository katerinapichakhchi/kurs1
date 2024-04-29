#string = "I like Python"
#new_string = "I like Java too!"

# string = 'I "like" Python'
# string = "I \"like\" Python"

# number = 12345
# str_number = str(number)                             # перевод в строчку
# print(str_number,type(str_number))

# print(string[0])
# print(string + new_string)                           # складывание
# print(string * 5)                                    # умножение

# for character in string:                             # каждый элемент на новой строчке
#    print(character)

# if "Python" in string:                               # поиск элемента в строчке
#   print("Yes, Python in string")

# upper_string = string.upper()                        # ВЕРХНИЙ реестр
# lower_string = string.lower()                        # нижний реестр
# title_string = string.title()                        # Каждое слово с большой буквы
# swap_string =string.swapcase()                       # противоположный реестр

# email = input("Please enter your email: ")
# print(email.strip())                                 # убирает пробелы с двух стороны
# email.lstrip()                                       # убирает пробелы слева
# email.rstrip()                                       # убирает пробелы справа

string = "I like PHP! PHP!"
new_string = string.replace("PHP", "Python", 1) # замена элемента
print(new_string)

string = " I like dogs anс cats"
array = string.split(",")                                 # строчка в список (по элементу)
print(array)

array = ["I", "like", "Python", "Python"]
joined_string = " ".join(array)                          # из списка в строчку "пунктуация".(список)
print(joined_string)
print(joined_string.find("P", 2))           # поиск элемента
print(joined_string.find("Python"))
string = "1, 2, 3, 1, 4, 5, 7"
ind = string.find("2")
print(ind)
new_ind = string.find("2", ind+1)                   # принт "-1" - не найдено
print(new_ind)


index = joined_string.count("Python")
second_find_string = joined_string.find("Python", index+1)
print(second_find_string)

# value = input("Please enter number of apple: ")
# if value.isdigit():                                      # Проверка на строчку
# if
#      print("Error. We need numbers!")
# else:
#      print(f"Yo got {value} apples")

# string = "I like Python"
# print(string.startswith("I"))                               # если начинается с
# print(string.startswith("P"))
# print(string.endswith("Python"))                            # если заканчивается на
# print(string.endswith("Like"))

