from tests import *
from Serializer.factory.parser_factory import create_serializer
import inspect
from Serializer.packager.object_inspector import deconstruct_instance, deconstruct_class, deconstruct_func
from Serializer.packager import packer
import sys


if __name__ == '__main__':
    serializer = create_serializer('json')

    res = serializer.dump(example_func, 'func.json')

    func = serializer.load('func.json')
