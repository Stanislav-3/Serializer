from cached import cached

@cached
def f(*args, **kwargs):
    values = [*args, *list(kwargs.values())]

    print('Sum( ', end='')
    sum = 0
    for i in range(len(values)):
        print(values[i], end=' ')
        sum += values[i]
    print(') = ', sum)

    return sum

if __name__ == '__main__':
    f(1, 2, f=3)
    f(1, 2, f=4)
    f(1, 2, f=3)

