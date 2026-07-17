def add_book(books):
# Add a book to the library

    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))
    isbn = input("ISBN: ")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn
    }
    books.append(book)

    print("\nBook added successfully!\n")

def list_books(books):
# Shows the books that are in the library

    if len(books) == 0:
        print("\nNo books found\n")
    else:
        print("\n===== Books =====\n")
        for book in books:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            print("ISBN:", book["isbn"])
            print("\n----------------------\n")

def search_book(books):
# Search for a book in the library
    
    search = input("Enter the title: ")
    found = False

    for book in books:
        if search == book["title"]:
            found = True
            print("\n===== Book Found =====\n")
            print("Book found: ")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            print("ISBN:", book["isbn"])
            print("\n---------------------------------------")
            break
        
    if not found:
        print("\nBook not found.\n")

def remove_book(books):
# Remove the book that is on the list

    search = input("Enter the title of the book you want to remove: ")
    found = False

    for book in books:
        if search == book["title"]:
            found = True
            books.remove(book)
            print("Book removed successfully!")
            break
        
    if not found:
        print("\nBook not found.\n")
    
        



print("===== Library Management System =====")

books = []


while True:

# user choices

    print("1 - Add Book")
    print("2 - List Books")
    print("3 - Search Books")
    print("4 - Remove Book")
    print("5 - Exit")

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

# Exit the program
    elif option == "5":
        print("Bye!")
        break

# Invalid option
    else:
        print("\nInvalid option.\n")