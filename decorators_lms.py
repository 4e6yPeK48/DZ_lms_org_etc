"""
написать logging_decorator, который логирует (выводит на экран)
имя исходной функции, переданные в нее аргументы и результат выполнения
"""


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        print(f'Функция {function.__name__} с аргументами {args} вернула {res}')
        return res

    return wrapper


@logging_decorator
def _sum(a, b):
    return a + b


print(_sum(3, 4))
print('-----------------')

"""
написать параметризованный volkswagen_decorator(test_mode: bool), который в зависимости от значения test_mode:
  * True - Игнорирует все исключения в исходной функции
  * False - вызывает исходную функцию как есть
"""


def volkswagen_decorator(test_mode: bool):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception as e:
                if test_mode:
                    print(f'Исключение: {e}')
                else:
                    raise e

        return wrapper

    return decorator


@volkswagen_decorator(True)
def func(a, b):
    return a / b


print(func(3, 0))
