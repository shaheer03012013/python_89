class Book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def Borrow(self):
        if not self.is_borrowed:
         self.is_borrowed = True
        print("You have borrowed " + self.title + " by " + self.author)
    def Return(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("You have returned " + self.title + " by " + self.author)

book1 = Book("1984", "George Orwell", False)
book2 = Book("Harry Potter", "J.K. Rowling", False)
book3 = Book("All Tomorrows", "C.M. Kösemen", True)

print("Welcome to the Library System")
your_choice = input("Choose the book you want to borrow(1, 2, or 3):")
if your_choice == "1":
    print("You borrowed " + book1.title + " by " + book1.author)
elif your_choice == "2":
    print("You borrowed " + book2.title + " by " + book2.author)
elif your_choice == "3":
    print("You borrowed " + book3.title + " by " + book3.author)
if book1.is_borrowed or book2.is_borrowed or book3.is_borrowed:
    print("Sorry, this book has been borrowed already.")
    



