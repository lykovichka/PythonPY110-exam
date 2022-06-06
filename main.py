import Fields
import json
from conf import MODEL


def generate_dict(counter: int) -> dict:
    """
    Функция - генератор словаря
    :param counter: счетчик
    :return: словарь
    """
    while True:
        books = {
            "model": MODEL,
            "pk": counter,
            "fields": {
                "title": Fields.title(),
                "year": Fields.year(),
                "pages": Fields.pages(),
                "isbn13": Fields.isbn13(),
                "rating": Fields.rating(),
                "price": Fields.price(),
                "author": Fields.author()
            }
        }
        yield books
        counter += 1


def main(num: int, pk: int = 1) -> json:
    """
    Функция, запускающая функцию-генератор generate_dict,
    формирует список словарей и записывает в json файл.
    :param num: количество книг, из которых необходимо сформировать список.
    :param pk: автоинкремент, увеличивается на 1.
    при генерации нового объекта, по умолчанию = 1.
    :return: json файл словарей книг.
    """
    list_ = []
    book = generate_dict(pk)
    for _ in range(num):
        list_.append(next(book))

    with open("Books.json", "w", encoding="utf-8") as file:
        json.dump(list_, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main(100)
