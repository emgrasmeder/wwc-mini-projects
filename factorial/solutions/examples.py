def fact(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return (x * fact(x-1))


if __name__ == "__main__":
    import math
    count = 100
    for i in range(count):
        assert fact(i) == math.factorial(i)
    print("Factorials calculated to i = {} without error.".format(count))
