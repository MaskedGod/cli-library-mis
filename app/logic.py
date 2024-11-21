import os
import json

from book import Book, Status


class Library:
    def __init__(self) -> None:
        self.filename = "library.json"
        self.books: list = self.load_books()

    def load_books(self) -> list:
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                try:
                    return [Book.from_dict(book) for book in json.load(file)]
                except json.JSONDecodeError:
                    return []
        else:
            with open(self.filename, "w") as file:
                file.write("")
        return []

    def save_books(self) -> None:
        books_dict = [book.to_dict() for book in self.books]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(books_dict, file, indent=4, ensure_ascii=False)

    def add_book(self, title, author, year) -> None:
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"{new_book.title} добавлена")

    def delete_book(self, id) -> None:
        deleted_book = (book for book in self.books if book.id == id)
        if deleted_book:
            self.books = [book for book in self.books if book.id != id]
            self.save_books()
            print(f"{deleted_book.title} удалена")
        else:
            print("Книги под этим id не существует")

    def change_book_status(self, id, status: Status) -> None:
        book_to_update = next(book for book in self.books if book.id == id)
        if book_to_update:
            if book_to_update.status == status:
                print(f"Статус книги {book_to_update.status.value} уже установлен ")
            else:
                book_to_update.status = status
                self.save_books()
                print(
                    f"Статус книги '{book_to_update.title}' обновлен на {status.value}."
                )
        else:
            print(f"Книга с id {id} не найдена.")

    @staticmethod
    def print_books(collection) -> None:
        for book in collection:
            print(
                f"id:{book.id}, '{book.title}' от {book.author} {book.year} года, {book.status}"
            )

    def list_books(self) -> None:
        if self.books:
            self.print_books(self.books)
        else:
            print("Библиотека пуста")

    def search_by_title(self, title) -> None:
        query = [book for book in self.books if book.title.lower() == title.lower()]
        self.print_books(query)

    def search_by_author(self, author) -> None:
        query = [book for book in self.books if book.author.lower() == author.lower()]
        self.print_books(query)

    def search_by_year(self, year) -> None:
        query = [book for book in self.books if book.year == year]
        self.print_books(query)
