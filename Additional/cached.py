from inspect import getfullargspec


def cached(func):
    """
    Декоратор @cached, который сохраняет значение функции при каждом вызове.
    Если функция вызвана повторно с теми же аргументами, то возвращается сохраненное значение,
    а функция не вычисляется.
    """
    cache = []
    results = {}

    def resulting_func(*args, **kwargs):
        full_arg_spec = getfullargspec(func)
        args_name = full_arg_spec[0]
        arguments = {}

        kwargs_ = kwargs.copy()

        args_len = len(args)
        for i in range(min(len(args_name), args_len)):
            arguments[args_name[i]] = args[i]

        while len(args_name) - args_len > 0:
            arguments[args_name[args_len]] = kwargs[args_name[args_len]]
            del kwargs_[args_name[args_len]]
            args_len += 1

        if full_arg_spec[1] is not None:
            arguments['*args'] = args[len(args_name):]

        if full_arg_spec[2] is not None:
            arguments['**kwargs'] = kwargs_

        print(arguments)
        if arguments in cache:
            print('Cached:', end=' ')
            res = results[cache.index(arguments)]
        else:
            print('Not cached:', end=' ')
            res = func(*args, **kwargs)
            cache.append(arguments)
            results[len(cache) - 1] = res
        return res

    return resulting_func
