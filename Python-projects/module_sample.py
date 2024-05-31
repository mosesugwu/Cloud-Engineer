class LibraryManagementSystem:
    def __init__(self):
        self.books = {}

    def borrow_book(self, title, borrower_name):
        if title in self.books:
            if self.books[title] == "available":
                self.books[title] = borrower_name
                print(f"{title} has been borrowed by {borrower_name}.") 
            else:
                print(f"{title} is currently not available.") 
        else:
            print(f"{title} is not found in the library.") 

    def return_book(self, title):
        if title in self.books:
            if self.books[title] != "available":
                borrower_name = self.books[title]
                self.books[title] = "available"
                print(f"{title} has been returned by {borrower_name}.") 
            else:
                print(f"{title} is already available.") 
        else:
            print(f"{title} is not found in the library.")