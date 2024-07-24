class Book:
    '''Information about book'''

    def __init__(self, title, authors, publisher, price, isbn):
        self.title = title
        self.authors = authors[:]
        self.publisher = publisher
        self.price = price
        self.isbn = isbn

    def authors_num(self):
        return len(self.authors)
    
    def display_info(self):
        print(f"Title: {self.title} Price: {self.price}")

python_book = Book("IPP", ["R", "H", "S"], "ABC", 123, '1-1-1-1')
maths_book = Book("IM", ["X", "Y", "X"], "ABC", 123, '1-1-1-2')
maths_book.display_info()
