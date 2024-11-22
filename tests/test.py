import pytest
from app.book import Status
from app.logic import Library


@pytest.fixture
def temp_library(tmpdir) -> Library:
    test_file = tmpdir.join("test_library.json")
    library = Library(str(test_file))
    return library


def test_add_book(temp_library, capsys) -> None:
    temp_library.add_book("Test book", "Test author", 2095)

    func_stndout = capsys.readouterr()
    assert "'Test book' добавлена" in func_stndout.out

    assert len(temp_library.books) == 1
    assert temp_library.books[0].id == 1
    assert temp_library.books[0].title == "Test book"
    assert temp_library.books[0].author == "Test author"
    assert temp_library.books[0].year == 2095
    assert temp_library.books[0].status.value == "в наличии"


def test_delete_book(temp_library, capsys) -> None:
    temp_library.add_book("Test book", "Test author", 2095)
    temp_library.delete_book(2)

    func_stdout = capsys.readouterr()
    assert "'Test book' удалена" in func_stdout.out


def test_search_book_by_title(temp_library, capsys) -> None:
    temp_library.add_book("Test book", "Test author", 2095)
    temp_library.search_by_title("Test book")

    func_stndout = capsys.readouterr()
    assert "id:3, 'Test book' от Test author 2095 года, в наличии" in func_stndout.out


def test_search_book_by_author(temp_library, capsys) -> None:
    temp_library.add_book("Test book", "Test author", 2095)
    temp_library.search_by_author("Test author")

    func_stndout = capsys.readouterr()
    assert "id:4, 'Test book' от Test author 2095 года, в наличии" in func_stndout.out


def test_search_book_by_year(temp_library, capsys) -> None:
    temp_library.add_book("Test book", "Test author", 2095)
    temp_library.search_by_year(2095)

    func_stndout = capsys.readouterr()
    assert "id:5, 'Test book' от Test author 2095 года, в наличии" in func_stndout.out


def test_list_all_books(temp_library, capsys) -> None:
    for i in range(1, 5):
        temp_library.add_book(f"Test book{i}", f"Test author{i}", 2095)

    temp_library.list_books()

    func_stndout = capsys.readouterr()
    assert "Test book1" in func_stndout.out
    assert "Test book2" in func_stndout.out
    assert "Test book3" in func_stndout.out
    assert "Test book4" in func_stndout.out

    assert len(temp_library.books) == 4


def test_change_book_status(temp_library, capsys) -> None:
    temp_library.add_book("Test book", "Test author", 2095)

    temp_library.change_book_status(10, Status.BORROWED)

    func_stndout = capsys.readouterr()

    assert "Статус книги 'Test book' обновлен на выдана." in func_stndout.out
    assert temp_library.books[0].status.value == "выдана"


def test_add_book_with_empty_data(temp_library, capsys) -> None:
    temp_library.add_book("", "", 0)

    func_stndout = capsys.readouterr()
    assert "Ошибка: Книга не может быть добавлена с пустыми данными" in func_stndout.out
    assert len(temp_library.books) == 0


def test_delete_book_with_non_existent_id(temp_library, capsys) -> None:
    temp_library.delete_book(999)

    func_stdout = capsys.readouterr()
    assert "Книга с id {id} не найдена." in func_stdout.out


def test_change_status_of_non_existent_book(temp_library, capsys) -> None:
    temp_library.add_book("Test book", "Test author", 2095)
    temp_library.change_book_status(999, Status.BORROWED)

    func_stndout = capsys.readouterr()
    assert "Книга с id 999 не найдена" in func_stndout.out


def test_search_with_empty_title(temp_library, capsys) -> None:
    temp_library.search_by_title("")

    func_stndout = capsys.readouterr()
    assert "Книги не найдены" in func_stndout.out


def test_search_with_empty_author(temp_library, capsys) -> None:
    temp_library.search_by_author("")

    func_stndout = capsys.readouterr()
    assert "Книги не найдены" in func_stndout.out


def test_search_with_non_existent_year(temp_library, capsys) -> None:
    temp_library.search_by_year(2100)

    func_stndout = capsys.readouterr()
    assert "Книги не найдены" in func_stndout.out


def test_empty_library_output(temp_library, capsys) -> None:
    temp_library.list_books()

    func_stndout = capsys.readouterr()
    assert "Библиотека пуста" in func_stndout.out
