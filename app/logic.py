import os
import json


class Library:
    def __init__(self) -> None:
        self.filename = "library.json"
        self.books: list = self.load_books()

    def load_books(self) -> list:
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        else:
            with open(self.filename, "w") as file:
                file.write("")
        return []

    def save_book(self) -> None:
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, year) -> None:
        new_book = Book(title, author, year)
        self.books.append(new_book.to_dict())
        self.save_book()

    def delete_book(self):
        pass

    def list_books(self):
        pass

    def search_by_title(self):
        pass

    def search_by_author(self):
        pass

    def search_by_year(self):
        pass
