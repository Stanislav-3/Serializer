from cached import cached


@cached
def f(x, y, *args, **kwargs):
    sum_ = x + y
    sum_ += sum(args)
    sum_ += sum(kwargs.values())

    return sum_

if __name__ == '__main__':
    print(f(1, 2))
    print(f(1, y=2))
    print(f(x=1, y=2))

    print(f(1, 2, 3))
    print(f(1, 2, other=3))
    print(f(1, 2, 3, other=4))
