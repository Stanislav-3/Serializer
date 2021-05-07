from tests import *
from Serializer.factory.parser_factory import create_serializer

if __name__ == '__main__':

    serializer = create_serializer('json')

    res = serializer.loads(serializer.dumps(test_class_2))
    print(res.some_class_func(test_class_2))
    print(test_class_2.some_class_func(test_class_2))

    print(res('$').some_class_func())
    print(test_class_2('$').some_class_func())
