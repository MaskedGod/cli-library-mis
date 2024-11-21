from book import Book
from logic import Library
import utils


def main():
    library = Library()

    print(
        "Вас приветсвует система управления библиотекой!\nЧто бы осуществить действие введите цифру относящуюся к данной опции"
    )

    while True:
        print(utils.library_menu)
        choice = input("Выберите действие: ")
        match choice:
            case 1:
                pas


if __name__ == "__main__":
    main()
