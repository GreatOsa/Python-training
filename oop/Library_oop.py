

class Book :
    def __init__(self,title,author, isbn):
        self.title = title
        self.author = author
        self.available=True
        self.isbn=isbn
       

    def __str__(self):
        return f"Book: {self.title} by {self.author} {self.isbn}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
       self.available = True


class Member():
    def __init__(self, name, member_id):
       self.name=name
       self.member_id=member_id
       self.borrowed_books=[]

    def borrow_book(self,book:Book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print("not available")
        
    def return_book(self,book:Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"You dont have '{book.title}'")
        

class Library():
    def __init__(self, name):
        self.name = name 
        self.books = []

    def list_books (self):
        if not self.books:
            print("No books in the librery")
        
    def find_book(self,book:Book):
      for library_bookisbn in self.books:
        if  book.isbn in library_bookisbn:
            return "Available"
        else:
            return "Not found"

class Librarian(Member):
    def __init__(self , name, member_id):
        self.name=name
        self.member_id=member_id
    
    def add_book(self, library:Library, book:Book):
        library.books.append(book)
        print(f"Librarian {self.name} added '{book.title}' to {library.name}")


    def remove_book(self, library:Library, book:Book):
        if book in library.books:
            library.books.remove(book)
            print(f"Librarian {self.name} removed '{book.title}' from {library.name}")
        else:
            print(f"'{book.title}' not found in {library.name}")


     





library = Library("City Library")

book1 = Book("1984", "George Orwell", "ISBN001")
book2 = Book("Python 101", "John Doe", "ISBN002")

print(book1.__str__())

librarian = Librarian("Alice", "L001")
librarian.add_book(library, book1)
librarian.add_book(library, book2)

member = Member("Bob", "M001")
library.list_books()

member.borrow_book(book1)
member.borrow_book(book1)   # should say "not available"
library.list_books()

member.return_book(book1)
library.list_books()