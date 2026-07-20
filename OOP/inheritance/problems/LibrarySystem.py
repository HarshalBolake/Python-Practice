class LibraryItem:
    def __init__(self,title):
        self.title = title
        self.borrower = None
    
    def borrow(self, borrower):
        self.borrower = borrower
        print(f"{self.title} borrowed by {borrower}")

    def return_item(self):
        self.borrower = None
        print(f"{self.title}Item returned")
        

class Book(LibraryItem):
    def read(self):
        print(f"Reading: {self.title}")

class Magazine(LibraryItem):
    def latest_issue(self):
        print(f"{self.title}Magazine latest issued")

class DVD(LibraryItem):
    def play(self):
        print(f"Playing: {self.title}")

B1 = Book("Python Programming")
M1 = Magazine("National Geographic")
D1 = DVD("Avenger")

B1.borrow("Harshal")
B1.read()
B1.return_item()

M1.borrow("John")
M1.latest_issue()

D1.borrow("Tom")
D1.play()