from datetime import datetime

example_None = None
example_bool = True
example_int = 123
example_float = 0.12345
example_string = 'It\'s a string'
example_tuple = (1, 2, 3)
example_frozenset = {1, 2, 3, 4, 5}

example_list = ['Just a string', None, False, (None, False, 'null')]
example_set = {1, 2, 3, 4, 5}

example_datetime = datetime(2001, 11, 14)
example_dict = {'3': [1, 2, 3],
             '0.23': 32,
             'key': (5, 'info', 8)}


example_lambda = lambda s: f'hello from lamda! {s}'


def example_func(val: int):
    return val + example_int


def example_recursion(val: int):
    if val == 0:
        return 0

    return example_recursion(val - 1) + 1


def example_with_inner_func(val: int):
    def inner_func(val):
        return -1 * val

    return inner_func(val - inner_func(val))

def example_func_return_func():
    def inner_func():
        return 'Just a random string'

    return inner_func


def example_generator(val: int):
    for i in range(val):
        yield i


class example_class_1():
    a = 2
    def __init__(self):
        self.b = 10


example_class_1.c = 'new class field'

example_instance_1 = example_class_1()
example_instance_1.d = 'new instance field'


class example_class_2(example_class_1):
    def __init__(self, s):
        super().__init__()
        self.e = str(s) + self.c

    def some_class_func(self):
        one = 'i\'m doing something...'
        two = 'other string'
        return one + two




