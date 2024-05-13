# LEGB
# L - Local
# E -
# G - Global
# B -

global_var = " World"

def example ():
    local_var = "Hello"
    return local_var + global_var

print(example())

def example ():
    local_var = "Hello"

    def test():
        inner = "Inner"
        print(inner)
        print(local_var)
        print(global_var)
        print()
    test()
    return local_var + global_var

print(example())