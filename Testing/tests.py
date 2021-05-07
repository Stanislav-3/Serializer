from datetime import datetime

test_None = None
test_bool = True
test_int = 123
test_float = 0.12345
test_string = 'It\'s a string'
test_tuple = (1, 2, 3)
test_frozenset = {1, 2, 3, 4, 5}

test_list = ['Just a string', None, False, (None, False, 'null')]
test_set = {1, 2, 3, 4, 5}

test_datetime = datetime(2001, 11, 14)
test_dict = {'3': [1, 2, 3],
             '0.23': 32,
             'key': (5, 'info', 8)}


test_lambda = lambda s: f'hello from lamda! {s}'


def test_func(val: int):
    return val + test_int


def test_recursion(val: int):
    if val == 0:
        return 0

    return test_recursion(val - 1) + 1


def test_with_inner_func(val: int):
    def inner_func(val):
        return -1 * val

    return inner_func(val - inner_func(val))

def test_func_return_func():
    def inner_func():
        return 'Just a random string'

    return inner_func


def test_generator(val: int):
    for i in range(val):
        yield i


class test_class_1():
    a = 2
    def __init__(self):
        self.b = 10


test_class_1.c = 'new class field'

test_instance_1 = test_class_1()
test_instance_1.d = 'new instance field'


class test_class_2(test_class_1):
    def __init__(self, s):
        super().__init__()
        self.e = str(s) + self.c

    def some_class_func(self):
        one = 'i\'m doing something...'
        two = 'other string'
        return one + two




