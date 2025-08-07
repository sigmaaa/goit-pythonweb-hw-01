from abc import ABC, abstractmethod


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: str) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books = []

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.books.append(book)

    def remove_book(self, title: str) -> bool:
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
                break

    def show_books(self) -> None:
        for book in self.books:
            print(
                f'Title: {book.get_title()}, Author: {book.get_author()}, Year: {book.get_year()}')


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def get_year(self) -> str:
        return self.year


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        self.library.add_book(title, author, year)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input(
            "Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
