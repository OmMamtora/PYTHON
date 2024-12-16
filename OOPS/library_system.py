# Implement a Library system where users can borrow and return books. 
# Track which books are available and which are checked out using classes.

class Library:

    def __init__(self):
        # self.books_details = [{"book_id":id,"book_title":title,"book_author":author,"available_status":status}]

        self.books_details = [
            {"book_id": 1, "book_title": "To Kill a Mockingbird", "book_author": "Harper Lee", "available_status": True},
            {"book_id": 2, "book_title": "1984", "book_author": "George Orwell", "available_status": True},
            {"book_id": 3, "book_title": "Moby Dick", "book_author": "Herman Melville", "available_status": True},
            {"book_id": 4, "book_title": "The Great Gatsby", "book_author": "F. Scott Fitzgerald", "available_status": True},
            {"book_id": 5, "book_title": "Pride and Prejudice", "book_author": "Jane Austen", "available_status": True}
        ]

    def borrow(self,book_title):
        for books in self.books_details:
            if books["book_title"].lower() == book_title.lower():
                if books["available_status"] == True:
                    print(f"You have borrowed '{books['book_title']}' by {books['book_author']}.")
                    return self.books_details[{"available_status":True}]
                else:
                    print(f"Sorry, '{books['book_title']}' is already checked out.")
                    return

        print("Book not found in library..")

    def return_book(self,book_title):
        for books in self.books_details:
            if books["book_title"].lower() == book_title.lower():
                if not books["available_status"]: 
                    books["available_status"] = True
                    print(f"Book '{books['book_title']}' by {books['book_author']}' is now returned. It is available for others to borrow.")
                    return
                else:
                    print(f"The book '{books['book_title']}' by {books['book_author']}' was not checked out, so it cannot be returned.")
                    return

        print("Book not found in the library. Please check the book ID.")


    def booksAvailable(self):
        available_books = [book for book in self.books_details]
        if available_books:
            print("Books available for borrowing:")
            for book in available_books:
                print(f"ID: {book['book_id']}, Title: {book['book_title']}, Author: {book['book_author']}")
        else:
            print("No books are currently available for borrowing.")

library = Library()
    
while True:
    print("\nLibrary System")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. View available books")
    print("4. Exit")
        
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        search_choice = input("Enter book name to borrow: ").strip()
        library.borrow(search_choice)
        
    elif choice == "2":
        search_choice = input("Enter name to return: ").strip()
        library.return_book(search_choice)
        
    elif choice == "3":
        library.booksAvailable()
        
    elif choice == "4":
        print("Exiting the library system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")