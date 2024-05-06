import string
import keyword
a = input("Name: ")
n = 0
k = 0
if a[0].isdigit() == False and a == a.lower() and a not in keyword.kwlist:
    for i in a:
            if i in string.punctuation and i == "_":
                n += 1
            elif i in string.punctuation and i != "_":
                k += 1
    if n < len(a) and k == 0:
        print(True)
    else:
        print(False)
else:
    print(False)
