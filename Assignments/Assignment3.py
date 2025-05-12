# Base class:Books
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}"

# Derived class EBooks
class EBook(Book):
    def __init__(self, title, author, file_type):
        super().__init__(title, author)
        self.file_type = file_type

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, File Type: {self.file_type}"
class Library:
    book_count = 0  # class variable

    def __init__(self):
        self.books=[]
    
    #Add Books
    def add_Books(self,book):
        self.books.append(book)
        Library.book_count +=1
        print(f"Book added successfully, The Library has {Library.book_count} books.")  
    #display books
    def display_Books(self):
        if not self.books:
            print("No Books to display")
        else:
            for b in self.books:
                print(b.get_info())


def main():
    library =Library()

    #add books
    book1 = Book("The Alchemist", "Paulo Coelho")
    ebook1 = EBook("Clean Code", "Robert C. Martin", "PDF")

    library.add_Books(book1)
    library.add_Books(ebook1)

    #display books
    library.display_Books()

if __name__=="__main__":
    main()


