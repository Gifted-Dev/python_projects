from library import *

# create a book
book1 = Book("Psychology of wealth", 'james')
book2 = Book("Richest Man in Babylon", 'Mark')
book3 = Book("Goals", "Brian Tracy")

# display book details
    # book2.display_book_details()


# create a library
library = Library()


# Create a librarian
librarian = Librarian('Peter', 'peter@gmail.com')
librarian1 = Librarian('Paul', 'paul@gmail.com')

# register librarian
library.register_librarian(librarian)
library.register_librarian(librarian1)

# check out the list of employed librarian


# Adds book to library
librarian.add_book(library, book1)
librarian.add_book(library, book2)
# librarian.add_book(library, book3)

# create a Member in Library
john = Member('john', 'john@gmail.com')
jack = Member('jack', 'jack@gmail.com')

# library.employed_librarian()


# Librarian registers member
librarian.register_member(library, john)
librarian.register_member(library, jack)

# show members in the library
# librarian.show_members(library)
library.library_members()


# Member borrows books
john.borrow(library, book1)
jack.borrow(library, book2)
    # jack.borrow(library, book3)

# Member returns book
# john.return_book(library, book2)


# Check books borrowed by Member
    # john.borrowed_books()


# Find books in library
    # library.find_book(book3)

# Library show books borrowed
    # library.books_borrowed()

# Print out books status
    # library.book_status()