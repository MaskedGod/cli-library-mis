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

    def __repr__(self) -> str:
        return (
            f"id: {self.id}, title: '{self.title}', author: '{self.author}', "
            f"year: {self.year}, status: {self.status.value})"
        )

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
            print("Ошибка! Книга уже выдана другому клиенту")

    def return_book(self) -> None:
        if self.status == Status.BORROWED:
            self.status = Status.AVAILABLE
        else:
            print("Ошибка! Книга уже возвращена")


if __name__ == "__main__":
    book1 = Book(title="1984", author="George Orwell", year=1945)
    book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960)
    book3 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925)

    print(book1)
    print(book2)
    print(book3)
    book2.return_book()
    book2.return_book()
