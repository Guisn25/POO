from dataclasses import dataclass, field
from typing import List
from enum import Enum
import datetime

@dataclass
class Book:
    title: str
    authors: List[str]
    edition: int

class Status(Enum):
    AVAILABLE = 1
    LOANED = 2
    LOST = 3

@dataclass
class BookItem:
    book: Book
    status: Status = Status.AVAILABLE
    date_borrowed: datetime.datetime = None

    def checkout(self) -> bool:
        if self.status == Status.AVAILABLE:
            self.date_borrowed = datetime.datetime.now()
            self.status = Status.LOANED
            return True
        return False

    def return_book(self) -> bool:
        if self.status == Status.LOANED:
            self.date_borrowed = None
            self.status = Status.AVAILABLE
            return True
        return False


@dataclass
class Member:
    name: str
    member_id: int
    borrowed_books: List[Book]

    def borrow_book(self, book_item: BookItem) -> bool:
        if book_item.Status == Status.AVAILABLE:
            self.borrowed_books.append(book_item.book)
            book_item.status = Status.LOANED
            book_item.date_borrowed = datetime.datetime.now()
            return True
        return False

    def return_book(self, book_item: BookItem) -> bool:
        if book_item.Status == Status.LOANED:
            self.borrowed_books.remove(book_item.book)
            book_item.status = Status.AVAILABLE 
            book_item.date_borrowed = None
            return True
        return False

@dataclass
class Library:
    Items: List[BookItem] = field(default_factory = list)
    Members: List[Members] = field(default_factory = list)

    def add_book_item(self, book_item: BookItem):
        self.Items.append(book_item)
    
    def add_member(self, member: Member):
        self.Members.append(member)




def main():
    book1 = Book(title = "The Great Gatsby", authors = ["F. Scott Fitzgerald"], edition = 1)
    book2 = Book(title = "1984", authors = ["George Orwell"], edition = 1)

    book_item1 = BookItem(book = book1)
    book_item2 = BookItem(book = book2)
    book_item3 = BookItem(book = book1)

    library = Library([book_item1,book_item2])

    library.add_book_item(book_item3)

    print(f"Checking out '{book_item1.book.title}': {book_item1.checkout()}")
    print(f"Status of '{book_item1.book.title}': {book_item1.status}")
    print(f"Checking out '{book_item1.book.title}' again: {book_item1.checkout()}")
    print(f"Returning '{book_item1.book.title}': {book_item1.return_book()}")
    print(f"Status of '{book_item1.book.title}': {book_item1.status}")
    print(f"Returning '{book_item1.book.title}' again: {book_item1.return_book()}")

if __name__ == '__main__':
   main()
