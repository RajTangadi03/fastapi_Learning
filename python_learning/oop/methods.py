class Books:
    # class variable
    section_id = 1234
    all_books = {}
    
    # constructor (dunder method)
    def __init__(self, book_id, book_name, book_author):
        self.book_id = book_id # accessing the instance variable we need instance name here self is used + "." operator
        self.book_name = book_name
        self.book_author = book_author
        Books.all_books[book_id] = [book_name, book_author] # accessing the class variable needs class name + "." operator

    # instance method -> we can access all instance variable through this (by using instance like here self)
    def printBookDetails(self):
        print("ID:", self.book_id, "Name:", self.book_name, "Authors:", self.book_author)
    
    # Class method -> we can access all class variables through this
    @classmethod
    def printAllBooksDetails(cls):
        print(cls.all_books)
    
    # static method -> with this we don't need any accessing method like above; We can directly use variables names
    @staticmethod
    def printApproxDiscount(age, time, orgPrice):
        print(f"Discount on original book price {orgPrice}: {(time+orgPrice)/age}")
    
def main():
    books = [
        Books(1, "A", "a"),
        Books(2, "B", "b"),
        Books(3, "C", "c"),
        Books(4, "D", "d"),
        Books(5, "E", "e")
    ]

    for book in books:
        book.printBookDetails()
    print()
    books[1].printAllBooksDetails()
    print()
    books[1].printApproxDiscount(10, 5, 500)

if __name__ == "__main__":
    main()