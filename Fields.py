import random
from faker import Faker


def title() -> str:
    """
    Функция рандомного выбора названия книги из созданного списка,
    содержащего названия книг.
    :return: Случайное название книги
    """
    books = []
    with open('book.txt', 'r', encoding="utf-8") as b:
        for book in b:
            books.append(book.strip())
    return random.choice(books)

def year() -> int:
    """
    Функция генерации случайного натурального числа,
    подразумевающего год выпуска книги.
    :return: случайное целое число

    """
    return random.randint(1800, 2021)


def pages() -> int:
    """"
    Функция генерации случайного натурального числа,
    подразумевающего количество страниц в книге.
    :return: случайное целое число

    """
    return random.randint(70, 600)


def isbn13() -> str:
    """
    Функция генерации международного стандартного номера
    с использованием модуля Faker.
    :return:
    """
    f = Faker()
    return f.isbn13()


def rating() -> float:
    """"
    Функция генерации случайного числа c плавающей запятой,
    подразумевающего рейтинг книги.
    :return: случайное число с плавающей запятой
    """

    return round(random.uniform(0, 5), 1)



def price() -> float:
    """"
    Функция генерации случайного числа c плавающей запятой,
    подразумевающего цену книги.
    :return: случайное число с плавающей запятой
    """

    return round(random.uniform(500, 5000), 2)



def author() -> list:
    """
    Функция генерации списка случаных имен от 1 до 3,
    с использованием модуля Faker, подразумевающих меня авторов книг.
    :return: список имен
    """
    autor_names = []
    fake = Faker()
    for _ in range(random.randint(1, 3)):
        autor_names.append(fake.name())
    return autor_names
