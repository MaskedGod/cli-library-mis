library_menu = """\nМеню библиотеки:\n1. Добавить книгу.\n2. Удалить книгу.\n3. Найти книгу.\n4. Показать все книги.\n5. Изменить статус книги.\n6. Закончить работу.\n"""


def search_books_menu(library):
    """Показывает меню поиска и обрабатывает действия пользователя для поиска книг."""
    while True:
        print(
            "1. Поиск по названию\n2. Поиск по автору\n3. Поиск по году\n4. Вернуться в главное меню\n"
        )
        search_choice = input("Выберите действие: ")

        if search_choice == "1":
            title = input("Введите название книги: ")
            library.search_by_title(title)
        elif search_choice == "2":
            author = input("Введите имя автора: ")
            library.search_by_author(author)
        elif search_choice == "3":
            try:
                year = int(input("Введите год: "))
                library.search_by_year(year)
            except ValueError:
                print("Некорректный ввод. Год должен быть числом.")
        elif search_choice == "4":
            break
        else:
            print("Некорректный выбор, попробуйте снова.")
