class Library:

    def __init__(self, listofbooks):
        self.books = listofbooks

    def display_available_books(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *"+book)

    def borrow_book(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 15 Days")
            self.books.remove(bookName)
            return True
        else:
            print("Soory,I think this bookis not present or This book has already bee issued to someone")
            return False

    def return_book(self, bookName):
        self.book.append(bookName)
        print("Thanks to return this book")


class Student:
    def request_book(self):
        self.book = input("Enter Name of Book you want to borrow:- ")
        return self.book
    
    def returnbook(self):
        self.book = input("Enter Name of Book you want to add/return:- ")
        return self.book


if __name__ =="__main__":
    centeral_library = Library(["C++ Language","Django Framework","C Language","Python Language","Node.js Framework"])
    # centeral_library.display_available_books()
    student = Student()
    while(True):
        WelcomeMsg = ''' 
        <--- Welcome to Central Library --->
             Please choose an options:
             1. Listing all the books.
             2. Request a book.
             3. Add/Return a book.
             4. Exit the library.
        '''
        print(WelcomeMsg)

        a = int(input("Enter a Choice:- "))
        
        if a==1:
            centeral_library.display_available_books()
        elif a==2:
            centeral_library.borrow_book(student.request_book())
        elif a==3:
            centeral_library.return_book(student.returnbook())
        elif a==4:
            print("<---Thanks for choosing this library--->")
            exit()
        else:
            print("Invalid number choose")
            print("try again.......")

        











    
