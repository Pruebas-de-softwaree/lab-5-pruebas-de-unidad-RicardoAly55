from library import Library
from book import Book
from user import User

if __name__ == "__main__":
    liba = Library()
    libro = Book("To Kill a Mockingbird", "Harper Lee", 1960, "ISBN002")
    liba.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960, "ISBN002"))
    libro.borrow()