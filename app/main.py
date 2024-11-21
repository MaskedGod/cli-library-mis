from logic import Library
from book import Status
import utils


def main():
    library = Library()

    print(
        "Вас приветсвует система управления библиотекой!\nЧто бы осуществить действие введите цифру относящуюся к данной опции."
    )

    while True:
        print(utils.library_menu)
        choice = input("Выберите действие: ")
        print("")
        match choice:
            case "1":  # Добавить книгу
                title = input("Название книги: ")
                author = input("Автор книги: ")
                while True:
                    try:
                        year = int(input("Год выпуска: "))
                        break
                    except ValueError:
                        print("Некорректные данные, введите число")

                if title and author:
                    library.add_book(title, author, year)
                else:
                    print("Некорректные данные, укажите название и автора")

            case "2":  # Удалить книгу
                while True:
                    try:
                        id = int(input("Введите id книги для удаления: "))
                        break
                    except ValueError:
                        print("Некорректные данные, введите число")
                library.delete_book(id)

            case "3":  # Найти книгу
                pass
            case "4":  # Показать все книги
                library.list_books()
            case "5":  # Изменить статус книги
                while True:
                    try:
                        id = int(input("Введите id книги для изменения статуса: "))
                        print("Выберите статус: \n1. В наличии\n2. Выдана\n")
                        status_choice = input("Введите номер статуса (1 или 2): ")
                        if status_choice == "1":
                            status = Status.AVAILABLE
                        elif status_choice == "2":
                            status = Status.BORROWED
                        else:
                            print(
                                "Некорректный выбор статуса. Пожалуйста, выберите 1 или 2."
                            )
                            continue

                        library.change_book_status(id, status)
                        break

                    except ValueError:
                        print("Некорректные данные, введите число.")

            case "6":  # Выйти из программы
                print("Выход...")
                break
            case default:
                print("Некорректный выбор, попробуйте ещё раз. Введите номер действия.")


if __name__ == "__main__":
    main()
