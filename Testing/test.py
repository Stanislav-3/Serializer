import pytest
from Serializer.factory.parser_factory import create_serializer
from tests import *


serializer = create_serializer('json')


class TestPrimitives:
    def test_invalid_serializer(self):
        try:
            invalid_serializer = create_serializer('* Something wrong *')
        except Exception as e:
            assert type(e) == ValueError

    def test_invalid_json(self):
        pass

    def test_None(self):
        assert serializer.loads(serializer.dumps(test_None)) == test_None

    def test_bool(self):
        assert serializer.loads(serializer.dumps(test_bool)) == test_bool

    def test_int(self):
        assert serializer.loads(serializer.dumps(test_int)) == test_int

    def test_float(self):
        assert serializer.loads(serializer.dumps(test_float)) == test_float

    def test_string(self):
        assert serializer.loads(serializer.dumps(test_string)) == test_string

    def test_tuple(self):
        assert serializer.loads(serializer.dumps(test_tuple)) == test_tuple

    def test_frozenset(self):
        assert serializer.loads(serializer.dumps(test_frozenset)) == test_frozenset

    def test_list(self):
        assert serializer.loads(serializer.dumps(test_list)) == test_list

    def test_set(self):
        assert serializer.loads(serializer.dumps(test_set)) == test_set

    def test_datetime(self):
        assert serializer.loads(serializer.dumps(test_datetime)) == test_datetime

    def test_dict(self):
        assert serializer.loads(serializer.dumps(test_dict)) == test_dict


class TestFunctions:
    def test_lambda(self):
        assert serializer.loads(serializer.dumps(test_lambda))('$') == test_lambda('$')

    def test_simple_func(self):
        assert serializer.loads(serializer.dumps(test_func))(5) == test_func(5)

    def test_recursion_func(self):
        assert serializer.loads(serializer.dumps(test_recursion))(7) == test_recursion(7)

    def test_with_inner_func(self):
        assert serializer.loads(serializer.dumps(test_with_inner_func))(9) == test_with_inner_func(9)

    def test_return_func(self):
        assert serializer.loads(serializer.dumps(test_func_return_func))()() == test_func_return_func()()

    def test_generator(self):
        res = serializer.loads(serializer.dumps(test_generator))
        assert [item for item in res(10)] == [item for item in test_generator(10)]


class TestClass:
    def test_class_1(self):
        res = serializer.loads(serializer.dumps(test_class_1))
        assert dir(res) == dir(test_class_1)
        assert res.a == test_class_1.a
        assert res.c == test_class_1.c

    def test_instance_1(self):
        res = serializer.loads(serializer.dumps(test_instance_1))
        assert dir(res) == dir(test_instance_1)
        assert res.a == test_instance_1.a
        assert res.b == test_instance_1.b
        assert res.c == test_instance_1.c
        assert res.d == test_instance_1.d
        assert isinstance(res, test_class_1)

    def test_class_2(self):
        res = serializer.loads(serializer.dumps(test_class_2))
        assert dir(res) == dir(test_class_2)
        assert res.a == test_class_2.a
        assert res.c == test_class_2.c
        #instances comparison
        assert isinstance(res('~$~'), test_class_2)
        assert res.some_class_func(res) == test_class_2.some_class_func(test_class_2)
        assert res('$').some_class_func() == test_class_2('$').some_class_func()
        assert res('a string').e == test_class_2('a string').e

