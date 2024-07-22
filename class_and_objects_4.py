class Book:

    """Information about a book, including title, list of authors,
    publisher, ISBN, and price.
    """

    def __init__(self, title, authors, publisher, isbn, price):
        """Create a new book entitled title, written by the people in authors,
        published by publisher, with ISBN isbn and costing price dollars.
        >>> python_book = Book( \
            'Practical Programming', \
            ['Campbell', 'Gries', 'Montojo'], \
            'Pragmatic Bookshelf', \
            '978-1-6805026-8-8', \
            25.0)
        """
        self.title = title
        # Copy the authors list in case the caller modifies that list later.
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price

    def __str__(self):
        """Return a human-readable string representation of this Book.
        """
        return f'''Title: {self.title}
Author: {', '.join(self.authors)}
Publisher: {self.publisher}
ISBN: {self.ISBN}
Price: Rs.{self.price}
'''
    
    def num_authors(self):
        '''Returns the number of authors of the book'''
        return len(self.authors)

python_book = Book(
    'Practical Programming',
    ['Campbell', 'Gries', 'Montojo'],
    'Pragmatic Bookshelf',
    '978-1-6805026-8-8',
    25.0)

#print(python_book.ISBN, python_book.title, python_book.authors)
print(python_book)