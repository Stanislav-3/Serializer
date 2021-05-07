import factory.parser_factory as factory
import json
import pickle
# import toml
import yaml
from factory.parser_factory import create_serializer
import logging
def get_extension(file_name: str):
    return file_name.split('.')[-1]

def convert(f1, f2):
    f1_ext = get_extension(f1)
    f2_ext = get_extension(f2)
    if f1_ext == f2_ext:
        pass
    else:
        try:
            serializer1 = create_serializer(f1_ext)
            serializer2 = create_serializer(f2_ext)
        except ValueError as e:
            logging.info(e)
        except Exception as e:
            logging.info(f'Something strange is happened here:\n{e}')
            return

        obj = serializer1.load(f1, False)
        serializer2.dump(obj, f2, False)

if __name__ == '__main__':
    serializer = factory.create_serializer("json")
    a = [1, 2, 3, 4]

    def func(x: int):
        return x + a


    class c():
        y = 2

    x = 3
    class cl(c):
        def __init__(self):
            self.a = 5 + x + self.y

    item = cl
    print(serializer.loads(serializer.dumps(cl))().a)
    # print(serializer.load("test.json"))

    # name = 'my_class'
    # bases = 'cl'
    # exec(f'class {name}({bases}):\n\tpass')
    # exec_eval = eval(f'{name}')
    # type_res = type(name + '2', (cl,), {})
    #
    # print(help(type_res))
    # print(help(exec_eval))
    #
    # print(dir(exec_eval))
    # print()
    # print(dir(type_res))

    # print("My serializer:\n", serializer.dumps(item))
    # print('*' * 25)
    # print("Json:\n", json.dumps(item))
    # print('*' * 25)
    # print("Pickle:\n", pickle.dumps(item))
    # print('*' * 25)
    # print("Yaml:\n", yaml.dump(item))
    # print('*' * 25)
    # print("Toml:\n", toml.dumps(item))