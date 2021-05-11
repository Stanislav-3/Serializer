def cached(func):
    """
    Декоратор @cached, который сохраняет значение функции при каждом вызове.
    Если функция вызвана повторно с теми же аргументами, то возвращается сохраненное значение,
    а функция не вычисляется. Учесть как позиционные, так и именованные аргументы.
    """
    cache = []
    results = {}
    def resulting_func(*args, **kwargs):

        if (args, kwargs) in cache:
            print('Cached: ', results[cache.index((args, kwargs))])
        else:
            print('Not cached:', end=' ')
            cache.append((args, kwargs))
            res = func(*args, **kwargs)
            results[len(cache) - 1] = res

    return resulting_func