import pytest
from app.logic import Library


@pytest.fixture
def temp_library(tmpdir) -> Library:
    test_file = tmpdir.join("test_library.json")
    library = Library(str(test_file))
    return library


def test_add_book(temp_library, capsys) -> None:
    temp_library.add_book("Правила Космического Движения", "А.П. Гураев", 2056)

    func_stndout = capsys.readouterr()
    assert "'Правила Космического Движения' добавлена" in func_stndout.out

    assert len(temp_library.books) == 1
    assert temp_library.books[0].id == 1
    assert temp_library.books[0].title == "Правила Космического Движения"
    assert temp_library.books[0].author == "А.П. Гураев"
    assert temp_library.books[0].year == 2056
    assert temp_library.books[0].status.value == "в наличии"


def test_find_book_by_title(temp_library, capsys) -> None:
    temp_library.add_book("Правила Космического Движения", "А.П. Гураев", 2056)
    temp_library.search_by_title("Правила Космического Движения")

    func_stndout = capsys.readouterr()
    assert (
        "id:2, 'Правила Космического Движения' от А.П. Гураев 2056 года, в наличии"
        in func_stndout.out
    )
