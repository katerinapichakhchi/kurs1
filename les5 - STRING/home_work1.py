import string
a = input("Name: ")
n = 0
if a[0].isdigit() == False and a == a.lower():
    for i in a:
            if i in string.punctuation and i == "_":
                n += 1
            elif i in string.punctuation and i != "_":
                n += 2
    if n < 2:
        print(True)
    else:
        print(False)
else:
    print(False)

