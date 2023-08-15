class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [c.book for c in Contract.all if c.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([c.royalties for c in Contract.all if c.author == self])

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return [c.author for c in Contract.all if c.book == self]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception
        else:
            self.author = author
        if not isinstance(book, Book):
            raise Exception
        else:
            self.book = book
        if type(date) != type(' '):
            raise Exception
        else:
            self. date = date
        if type(royalties) != type(1):
            raise Exception
        else:
            self. royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key = lambda c: c.date)