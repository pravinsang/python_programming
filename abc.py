class Book:
    '''Infromation about book
    This is a class
    '''

    def __init__(self,title,authors,isbn,publisher,price):
        self.title = title
        self.authors = authors[:]
        self.ISBN = isbn
        self.publisher = publisher
        self.price = price

    def num_authors(self):
        return len(self.authors)


authors = ["A","B","C"]
python_book = Book("IIP",authors,'1-1-1-1','XYZ','999')
print(python_book.title,python_book.authors)