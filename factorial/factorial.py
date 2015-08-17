# Edit this file in your text editor or IDE and run it from the command line

def fact(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 6
    elif x == 4:
        return 24


if __name__ == "__main__":
    import math
    for i in range(100):
        assert fact(i) == math.factorial(i),\
        "fact({}) != math.factorial({}) ==> {} != {}".format(i, i, fact(i), math.factorial(i))
