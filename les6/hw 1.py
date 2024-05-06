import string
print(string.ascii_letters)
a = input("Введите две буквы через дефис: ")
print(string.ascii_letters[string.ascii_letters.find(a[0]):string.ascii_letters.find(a[2])+1])
