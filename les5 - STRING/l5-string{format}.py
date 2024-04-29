name = "Eugene"
age = 25
height = 1.81

# string = "%s is %d years old and %f meters tall" % (name, age, height) # "%"(место для переменной) - форматирование
#                                                                       %s - строчка, %d - число, %f - число с точкой
string = "{} is {} years old and {} meters tall".format(name, age, height)
print(string)

string = "{NAME} is {AGE} years old and {HEIG} meters tall".format(NAME=name, HEIG=height, AGE=age)
print(string)

string = f"{name} is {age} years old and {height} meters tall"
print(string)

string = f"{name.upper()} is {age+10} years old and {height} meters tall"
print(string)

print(ord("A"))
print(ord("А"))
print(ord("a"))

print(chr(65))
print(chr(1045))
print(chr(8800))
