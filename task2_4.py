def task2(function):
    """Декоратор, который проводить валидацию названия книги.
     В случае, если длина названия книги больше заданного (max_len) значения,
     то ошибка ValueError.
    """
    def wrapper():
        max_len = 25
        if len(function()) > max_len:
            raise ValueError('Слишком длинное название книги... надоест читать :)')

        return function

    return wrapper


def task4(max_len_: int):
    """Фабрика декораторов task2,
     принимает значение максимальной длины как параметр."""
    def task_2(func):
        def wrapper():
            if len(func()) > max_len_:
                raise ValueError('Опять слишком длинное название книги')

            return func()

        return wrapper

    return task_2
