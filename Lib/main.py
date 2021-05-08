import inspect
import builtins


if __name__ == '__main__':
    class other:
        pass

    class cl(other):
        x = 5
        def __init__(self):
            self.a = 5

        def func(self):
            return 5
    m = 2
    def f():
        a = 5 + m
        k = 123
        def innner():
            return a + 1 + k + m
        return innner

    # getfields(cl)
    l = [1, 2, 3, 4]
    print(f.__module__)



