from tests import *
from Serializer.factory.parser_factory import create_serializer

if __name__ == '__main__':

    serializer = create_serializer('json')

    res = serializer.dump(example_func, 'func.json')

    func = serializer.load('func.json')
    print(func(5))

