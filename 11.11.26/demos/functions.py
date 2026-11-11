def my_fun(num: int):
    print(num)


my_fun(3)


def riddle(num: int):
    yield from range(num)


gen = riddle(1_000_000_000)

# 0
print(next(gen))

# 0
print(next(gen))


# print(list(gen))


a = None
print(type(a))


def my_other_fun(x=None):
    if x is None:
        print("yes")
    else:
        print("no")


# fact(5) = 5 * 4!
# fact(n) = n * fact(n-1)

def factorial(n:int):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)  # Output: 120