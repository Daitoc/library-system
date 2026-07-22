from storage import save_books, load_books
from library import (
    add_book,
    list_books,
    search_book,
    remove_book,
    edit_book,
)


# Start of the program
print("===== Library Management System =====")

books = load_books()


while True:

# user choices

    print("1 - Add Book")
    print("2 - List Books")
    print("3 - Search Books")
    print("4 - Remove Book")
    print("5 - Edit book")
    print("6 - Exit")

    option = input("Choose an option: ")

# Add a Book in Library
    if option == "1":
        add_book(books)

# Shows the books in library
    elif option == "2":
        list_books(books)

# Search a book in library
    elif option == "3":    
        search_book(books)
    
# Remove a book in library
    elif option == "4":
        remove_book(books)

    elif option == "5":
        edit_book(books)

# Exit the program
    elif option == "6":
        print("Bye!")
        break

# Invalid option
    else:
        print("\nInvalid option.\n")