import string
print(string.punctuation)
a = input("Введите текст ").title()
b = "#"
for i in a:
    if len(b) < 140:
        if i not in string.punctuation and i != " ":
            b += i

print(b, len(b))

