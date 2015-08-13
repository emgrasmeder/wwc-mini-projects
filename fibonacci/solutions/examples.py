import time

# a recursive solution
def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fib_recursive(n-1) + fib_recursive(n-2)

# a solution using overwriting variable assignment
def fib_assignment(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# a solution using matrix algebra identities
def fib_identity(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib_identity(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

# this function compares the processing times of the different functions, try it with some very large numbers (keep it under 1,000,000,000)!
def compare(n):
    print("for n = ", n,)
    s3 = time.clock()
    v3 = fib_identity(n)
    e3 = time.clock()
    print("identity took", (e3 - s3) * 1000, "milliseconds")
    if n<=1000000:
        s2 = time.clock()
        v2 = fib_assignment(n)
        e2 = time.clock()
        print("assignment took", (e2 - s2) * 1000, "milliseconds")
    else:
        print("pick a n <= 1,000,000, assignment gets linearly worse")
    if n <= 35:
        s1 = time.clock()
        v1 = fib_recursive(n)
        e1 = time.clock()
        print("recursive took", (e1 - s1) * 1000, "milliseconds")
    else:
        print("pick a n <= 35, recursive gets exponentially worse")

compare(25)
compare(10000)
