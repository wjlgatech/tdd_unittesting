def add1(x):
    return x + 1


def square(x):
    return x**2


def is_even(x):
    return x % 2 == 0


def get_odds(nums):
    return [x for x in nums if x % 2 != 0]


def dot_product(v1, v2):
    return sum([x*y for x, y in zip(v1, v2)])
