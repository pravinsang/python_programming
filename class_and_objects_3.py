class Book:

    '''Information about book'''
    def num_authors(self):
        '''Returns the number of authors of the book'''
        return len(self.authors)

python_book = Book()
python_book.title = 'Introduction to Python Programming'
python_book.authors = ['Ram Thapa','Hari Thapa','Krishna Shrestha']
print(Book.num_authors(python_book))
print(python_book.num_authors())