class Library:
    def __init__(self, books):
        self.books = books
        self.lend_data = {}

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book not in self.lend_data:
                print(f" - {book}")
        print()

    def lend_book(self, book, user):
        if book in self.books:
            if book not in self.lend_data:
                self.lend_data[book] = user
                print(f"\nBook '{book}' has been lent to {user}.\n")
            else:
                print(f"\nSorry, '{book}' is already lent to {self.lend_data[book]}.\n")
        else:
            print(f"\nBook '{book}' is not in the library.\n")

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"\nBook '{book}' has been added to the library.\n")
        else:
            print(f"\nBook '{book}' already exists in the library.\n")

    def return_book(self, book):
        if book in self.lend_data:
            del self.lend_data[book]
            print(f"\nBook '{book}' has been returned.\n")
        else:
            print(f"\nBook '{book}' was not lent out.\n")


def main():
    library = Library(["Python Programming", "Data Science 101", "Machine Learning", "AI Basics"])
    
    while True:
        print("\n--- Library Menu ---")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            library.lend_book(book, user)
        elif choice == "3":
            book = input("Enter the name of the book to add: ")
            library.add_book(book)
        elif choice == "4":
            book = input("Enter the name of the book to return: ")
            library.return_book(book)
        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please select between 1-5.")

if __name__ == "__main__":
    main()
