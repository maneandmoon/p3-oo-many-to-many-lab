class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    # - `contracts(self)`: This method should return a list of related contracts.
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]


#     - `books(self)`: This method should return a list of related books using the
#   `Contract` class as an intermediary.    

    def books(self):
        return [contract.book for contract in self.contracts()]

# - `sign_contract(book, date, royalties)`: This method should create and return a
#   new `Contract` object between the author and the specified book with the
#   specified date and royalties

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

# - `total_royalties()`: This method should return the total amount of royalties
#   that the author has earned from all of their contracts.

    def total_royalties(self): 
        return sum(contract.royalties for contract in self.contracts())

      

# FAILED module Test Book class has method contracts() that returns a list of its contracts - AttributeError: 'Book' object has no attribute 'contracts'
# FAILED module Test Book class has method authors() that returns a list of its authors - AttributeError: 'Book' object has no attribute 'authors'
class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]



# FAILED module Test Contract class validates author of type Author - Failed: DID NOT RAISE <class 'Exception'>
# FAILED module Test Contract class validates book of type Book - Failed: DID NOT RAISE <class 'Exception'>
# FAILED module Test Contract class validates date of type str - Failed: DID NOT RAISE <class 'Exception'>
# FAILED module Test Contract class validates royalties of type int - Failed: DID NOT RAISE <class 'Exception'>
class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, cur_author):
        if not isinstance(cur_author, Author):
            raise Exception("author property should be an instance of the Author class")
        self._author = cur_author

    @property
    def book(self):
        return self._book
    
    @book.setter 
    def book(self, cur_book):
        if not isinstance(cur_book, Book):
            raise Exception("book property should be an instance of the Book class")
        self._book = cur_book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, cur_date):
        if not isinstance(cur_date, str):
            raise Exception("date property should be a string")
        self._date = cur_date
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, cur_royalties):
        if not isinstance(cur_royalties, int):
            raise Exception("royalties property should be an integer")
        self._royalties = cur_royalties

# - A class method `contracts_by_date`(cls, date): This method should return all
#   contracts that have the same date as the date passed into the method.

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
