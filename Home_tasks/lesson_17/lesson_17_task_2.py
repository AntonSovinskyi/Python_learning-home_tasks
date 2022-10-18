"""Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

"""


class Author:
    def __init__(self, name, country, birthday):
        self.author_name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f'Author name is {self.author_name}, from {self.country}. Birthday data: {self.birthday}.'

    def __repr__(self):
        return f'Author name is {self.author_name}, from {self.country}. Birthday data: {self.birthday}.'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):

        new_book = Book(name, year, author)
        self.books.append(new_book)
        if author not in self.authors:
            self.authors.append(author)
        return new_book

    def group_by_author(self, author):
        book_list = []
        for book in self.books:
            if book.author.author_name == author.author_name:
                book_list.append(book.book_name)
        return book_list

    def group_by_year(self, year):
        books_by_year = []
        for book in self.books:
            if year == book.year:
                books_by_year.append(book.book_name)
        return books_by_year

    def __str__(self):
        return f'Library name is {self.name}.'

    def __repr__(self):
        return f'Library name is {self.name}.'


class Book:
    all_books = 0

    def __init__(self, name, year, author):
        self.book_name = name
        self.year = year
        self.author = author
        self.all_books += 1

    def __str__(self):
        return f'Book name is {self.book_name}, and year is {self.year}.'

    def __repr__(self):
        return f'Book name is {self.book_name}, and year is {self.year}.'


lib = Library('NewLib')
author = Author('Roger Joseph Zelazny', 'USA', '13.05.1937')
book = Book('Guns of Avalon', 1980, author)


print(lib.new_book('Witcher', 1995, author))
print(lib.books)
print(lib.group_by_author(author))
print(lib.group_by_year(1995))
# print(book.book_name)
# print(book.year)
