import os
import json

from book import Book, Status


class Library:
    """Класс, представляющий библиотеку, которая управляет коллекцией книг.

    Attributes:
        filename (str): Имя файла для сохранения и загрузки данных.
        books (list): Список книг в библиотеке.
    """

    def __init__(self, filename="library.json") -> None:
        self.filename = filename
        self.books: list = self.load_books()

    def load_books(self) -> list:
        """Загружает книги из файла JSON.

        Returns:
            list: Список книг, загруженных из файла.
        """
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
        """Сохраняет текущую коллекцию книг в файл JSON."""
        books_dict = [book.to_dict() for book in self.books]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(books_dict, file, indent=4, ensure_ascii=False)

    def add_book(self, title, author, year) -> None:
        """Добавляет новую книгу в библиотеку.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """
        if title and author and year:
            new_book = Book(title, author, year)
            self.books.append(new_book)
            self.save_books()
            print(f"'{new_book.title}' добавлена")
        else:
            print("Ошибка: Книга не может быть добавлена с пустыми данными")

    def delete_book(self, id) -> None:
        """Удаляет книгу по ее идентификатору.

        Args:
            id (int): Уникальный идентификатор книги.
        """
        deleted_book = next((book for book in self.books if book.id == id), None)
        if deleted_book:
            self.books = [book for book in self.books if book.id != id]
            self.save_books()
            print(f"'{deleted_book.title}' удалена")
        else:
            print("Книга с id {id} не найдена.")

    def change_book_status(self, id, status: Status) -> None:
        """Изменяет статус книги по ее идентификатору.

        Args:
            id (int): Уникальный идентификатор книги.
            status (Status): Новый статус книги.
        """
        book_to_update = next((book for book in self.books if book.id == id), None)
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
        """Печатает информацию о книгах из переданной коллекции.

        Args:
            collection (list): Коллекция книг для вывода.
        """
        for book in collection:
            print(
                f"id:{book.id}, '{book.title}' от {book.author} {book.year} года, {book.status.value}"
            )

    def list_books(self) -> None:
        """Выводит список всех книг в библиотеке."""
        if self.books:
            self.print_books(self.books)
        else:
            print("Библиотека пуста")

    def search_by_title(self, title) -> None:
        """Ищет книги по названию и выводит результат.

        Args:
            title (str): Название книги для поиска.
        """
        query = [book for book in self.books if book.title.lower() == title.lower()]
        if query:
            self.print_books(query)
        else:
            print("Книги не найдены")

    def search_by_author(self, author) -> None:
        """Ищет книги по автору и выводит результат.

        Args:
            author (str): Имя автора для поиска.
        """
        query = [book for book in self.books if book.author.lower() == author.lower()]
        if query:
            self.print_books(query)
        else:
            print("Книги не найдены")

    def search_by_year(self, year) -> None:
        """Ищет книги по году издания и выводит результат.

        Args:
            year (int): Год издания для поиска.
        """
        query = [book for book in self.books if book.year == year]
        if query:
            self.print_books(query)
        else:
            print("Книги не найдены")
