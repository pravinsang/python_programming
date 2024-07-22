class Book:

    '''Information about book'''


python_book = Book()
python_book.title = 'Introduction to Python Programming'
python_book.authors = ['Ram Thapa','Hari Thapa','Krishna Shrestha']
print(f"{python_book.title} by {', '.join(python_book.authors)}")