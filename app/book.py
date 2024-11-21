from enum import Enum


class Status(Enum):
    AVAILABLE = "в наличии"
    BORROWED = "выдана"


class Book:
    """Класс, представляющий книгу в библиотеке.

    Attributes:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (Status): Статус книги (в наличии или выдана).
    """

    _id_counter = 1

    def __init__(self, title, author, year, status=Status.AVAILABLE) -> None:
        self.id: int = Book._id_counter
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: Status = status

        Book._id_counter += 1

    def to_dict(self) -> dict:
        """Преобразует объект книги в словарь для последующего сохранения в JSON.

        Returns:
            dict: Словарь с атрибутами книги.
        """

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }

    @staticmethod
    def from_dict(data) -> "Book":
        """Создает экземпляр книги на основе данных из словаря.

        Args:
            data (dict): Словарь с информацией о книге.

        Returns:
            Book: Новый экземпляр книги.
        """
        book = Book(data["title"], data["author"], data["year"])
        book.status = Status(data["status"])
        book.id = int(data["id"])
        return book
