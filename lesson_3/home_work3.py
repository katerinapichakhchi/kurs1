lst = [1, 2, 3, 4, 5, 6]
a = len(lst)/2
list = []
if a == int(a):
    list.append(lst[:int(a)])
    list.append(lst[int(a):])
else:
    list.append(lst[:int(a+1)])
    list.append(lst[int(a+1):])
print(lst, "=>", list)

lst1 = [1, 2, 3, 4, 5, 6, 7]
a1 = len(lst1)/2
list1 = []
if a1 == int(a1):
    list1.append(lst1[:int(a1)])
    list1.append(lst1[int(a1):])
else:
    list1.append(lst1[:int(a1+1)])
    list1.append(lst1[int(a1+1):])
print(lst1, "=>", list1)

lst2 = [1]
a2 = len(lst2)/2
list2 = []
if a2 == int(a2):
    list2.append(lst2[:int(a2)])
    list2.append(lst2[int(a2):])
else:
    list2.append(lst2[:int(a2+1)])
    list2.append(lst2[int(a2+1):])
print(lst2, "=>", list2)

lst3 = []
a3 = len(lst3)/2
list3 = []
if a3 == int(a3):
    list3.append(lst3[:int(a3)])
    list3.append(lst3[int(a3):])
else:
    list3.append(lst3[:int(a3+1)])
    list3.append(lst3[int(a3+1):])
print(lst3, "=>", list3)