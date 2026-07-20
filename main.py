import json

def save_books(books):
    with open("library.json", "w") as file:
        json.dump(books, file, indent=4)

def load_books():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]


def add_book(books):
# Add a book to the library

    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))
    isbn = input("ISBN: ")

    for book in books:
        if book["isbn"] == isbn:
            print("This ISBN already exists.")
            return

    book = {
        "title": title,
        "author": author,
        "year": year,
        "isbn": isbn
    }
    books.append(book)

    save_books(books)
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
    
    search = input("Enter the title: ").lower()
    found = False

    for book in books:
        if search == book["title"].lower():
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

    search = input("Enter the title of the book you want to remove: ").lower()
    found = False

    for book in books:
        if search == book["title"].lower():
            found = True
            books.remove(book)
            save_books(books)
            print("Book removed successfully!")
            break
        
    if not found:
        print("\nBook not found.\n")

def edit_book(books):
# Edit a book from the library

    search = input("Enter the title of the book that you want to edit: ").lower()
    found = False
    for book in books:
        if search == book["title"].lower():
            found = True
            new_title = input("New title: ")
            book["title"] = new_title

            new_author = input("New author: ")
            book["author"] = new_author

            new_year = int(input("New year: "))
            book["year"] = new_year

            new_isbn = input("New ISBN: ")
            book["isbn"] = new_isbn

            save_books(books)
            print("Book updated successfully!")
            break
        
    if not found:
        print("\nBook not found.\n")
        


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