def summ_of_elements(x: int, y: int) -> int:
    return x + y

print(summ_of_elements(1, 2))
# print(summ_of_elements(x=1, y=0))


def summ1 (*args, **kwargs):                                                             # не указано кол-во переменной
    for arg in args:
       print(arg)

    for key, value in kwargs.items():
        print(key, value)
print(summ1( 6,'7',8,number_1=1, number_2=2, number_3=3))

def example(positional, named, *args, **kwargs):
    print(f"Positional: {positional}")
    print(f"Named: {named}")
    print(f"Additioanal position: {args}")
    print(f"Additionak named: {kwargs}")

# example("7", 8, 5, 2, 3, name=98, main=8)
example_list = [1, 2, 3]
example_dict = {"1": 1, "2": 2}
example("7", 8, *example_list, **example_dict)


def calculate_square(radius: int) -> float:
