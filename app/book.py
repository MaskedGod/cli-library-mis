from enum import Enum


class Status(Enum):
    AVAILABLE = "в наличии"
    BORROWED = "выдана"


class Book:
    _id_counter = 1

    def __init__(self, title, author, year, status=Status.AVAILABLE) -> None:
        self.id: int = Book._id_counter
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: Status = status

        Book._id_counter += 1

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    def borrow_book(self) -> None:
        if self.status == Status.AVAILABLE:
            self.status = Status.BORROWED
        else:
            print("Ошибка! Книга уже выдана другому клиенту.")

    def return_book(self) -> None:
        if self.status == Status.BORROWED:
            self.status = Status.AVAILABLE
        else:
            print("Ошибка! Книга уже возвращена.")
