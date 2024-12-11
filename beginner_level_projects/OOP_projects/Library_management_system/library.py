# Library features
class Book:
   # initialize with properties, title, author, genre, availability
    def __init__(self, title, author):
       self.title = title
       self.author = author
       self.available = True
       
    # mark book as borrowed
    def mark_book_as_borrowed(self):
        self.available = False
    
    # mark book as returned
    def mark_book_as_returned(self):
        self.available = True
        
    # display book details
    def display_book_details(self):
        print(f"Title: {self.title},\
              \n Author: {self.author},\
              \n Available: {self.available}")
class Person:
    # initiatlize a person class to take name, email, phone number
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Librarian(Person):
    # init employee_id
    id = 0
    def __init__(self, name, email,):
        super().__init__(name, email)
        Librarian.id += 1
        self.employee_id = Librarian.id
        
    # Method: Add book
    def add_book(self, library, book):
        if book not in library.books:
            library.books.append(book)
            print(f"The book '{book.title}' has been added to the library")
        else:
            print(f"{book.title} is already in the libary")
    
    # Method: Remove Book
    def remove_book(self, library, book):
        if book in library.books:
            library.books.remove(book)
        else:
            print(f"The book '{book}' is not in the library")
    
    # Method: Register Member
    def register_member(self, library, member):
        if member not in library.member:
            library.member.append((member, member.member_id))
            print(f"The member {member.name} has been sucessfully registed to the library")
        else:
            print(f"The member {member.name} has already been registed to the library")
            
    def show_members(self, library):
        print('These are the members registered in the library:')
        for index, member in enumerate(library.member):
            print(f"{index + 1}. {member[0].name} with the id_number of {member[1]}")
        
           

class Member(Person):
    id = 0
    # init member_id, borrowed_books, borrow_limit
    def __init__(self, name, email, limit=3):
        super().__init__(name, email)
        self.limit = limit
        self.books_borrowed = [] 
        Member.id += 1
        self.member_id = Member.id
    
    # Method: Borrow Book
    def borrow(self, library, book):
        if len(self.books_borrowed) < self.limit:
            if book in library.books: # check if books is in library
                if book.available: # check if book is available
                    book.mark_book_as_borrowed() # Mark book as borrowed
                    self.books_borrowed.append(book)   
                else:
                    print("book is not available")
            else:
                print(f"The book '{book.title}' is not yet in the library collection")
        else:
            print(f"{self.name} has reached the \
                limit of books to borrow")
    
   
    
    # Method: Return Book   
    def return_book(self, library, book):
        if book in library.books:
            if not book.available:
                book.mark_book_as_returned()
                self.books_borrowed.remove(book)
                print(f"The book '{book.title}' has been returned back to the library")
            else:
                print(f"The book '{book.title}' is still available in the library")
        else:
            print(f"There is no record of the library having this book '{book.title}")
    
    def borrowed_books(self):
        if self.books_borrowed:
            for index, book in enumerate(self.books_borrowed):
                print(f"Here are the books borrowed:\
                        \n{index + 1}. {book.title}")
        else:
            print("no books has been borrowed")

class Library:
    # init books, members, librarians
    def __init__(self):
       self.books = []
       self.member = []
       self.librarians = []
    
    # Method: Handle Borrowed Books
    def books_borrowed(self):
        for member in self.member:
            if member[0].books_borrowed: #accessing the borrowd books list in member class
                print(f"{member[0].name} borrowed the following books:")
                for book in member[0].books_borrowed:
                    print(book.title)
            else:
                print(f"'{member[0].name} has not borrowed any books")
        
    # Method: Add Member
    def register_member(self, member):
        if member not in (m[0] for m in self.member):
            self.member.append((member, member.member_id))
        else:
            print("Member is already registered")
        
    # Method: Add librarian
    def register_librarian(self, librarian):
        if librarian not in (l[0] for l in self.librarians):
            self.librarians.append((librarian, librarian.employee_id))
        else:
            print("Librarian already registered")
    
    # Method: Print out members in the library
    def library_members(self):
        for member in self.member:
            print(f"{member[0].name} with the id_number of {member[1]}")
            
    # Method: Print out the Librarians in the library
    def employed_librarian(self):
        print("Here are the list of employed librarians:")
        for index, librarians in enumerate(self.librarians):
            print(f"{index + 1}. {librarians[0].name} Id No: {librarians[1]}")


    # Method Print out Books in the library with its status:
    def book_status(self):
        for book in self.books:
            print(f"{book.title} is available: {book.available}")
