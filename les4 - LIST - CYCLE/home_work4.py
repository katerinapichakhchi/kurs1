# Напишіть програму, яка створює список з чисел від 1 до 100. При цьому замість чисел, кратних трьом,
# програма повинна додавати до списку стрічку Fizz, а замість чисел, кратних п'яти - стрічку Buzz.
# Якщо число кратне і 3, і 5, програма повинна  додавати стрічку «FizzBuzz».

lst = []
for i in range(1,100):
    if i/3 == i//3 and not i/5 == i//5:
        lst.append('Fizz')
    elif not i/3 == i//3 and i/5 == i//5:
        lst.append('Buzz')
    elif i/3 == i//3 and i/5 == i//5:
        lst.append('FizzBuzz')
    else:
        lst.append(i)
print(lst)