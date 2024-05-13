import random
a = []

# def common_elements():
for _ in range(100):
    a.append(random.randint(1, 100))
for i in a:
    if i // 3 == i / 3 and i // 5 == i / 5 :
        print(a)





# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}