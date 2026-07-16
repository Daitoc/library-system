def add_book(books):
# Adds books to the library

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

print("===== Library Management System =====")

books = []


while True:

# user choices

    print("1 - Add Book")
    print("2 - List Books")
    print("3 - Exit")

    option = input("Choose an option: ")

# Add a Book in Library

    if option == "1":
        add_book(books)

# Shows the books in library

    elif option == "2":
        list_books(books)
        
    elif option == "3":
        print("Bye!")
        break
    else:
        print("\nInvalid option.\n")