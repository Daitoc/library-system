from storage import save_books

def get_valid_year(message):
    while True:
        try:
            year = int(input(message))
            return year
        except ValueError:
            print("Invalid year. Please enter a number.")

def add_book(books):
# Add a book to the library

    title = input("Title: ")
    author = input("Author: ")
    year = get_valid_year("Year: ")
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
            confirmation = input("Are you sure you want to remove this book? (Y/N)").lower()
            if confirmation == "y":
                books.remove(book)
                save_books(books)
                print("Book removed successfully!")
                break
            elif confirmation == "n":
                print("Operation cancelled")
                break
            else:
                print("Invalid option.")
                return

        
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

            new_year = get_valid_year("New year: ")
            book["year"] = new_year

            new_isbn = input("New ISBN: ")
            book["isbn"] = new_isbn

            for other_book in books:
                if other_book["isbn"] == new_isbn and other_book is not book:
                    print("This ISBN already exists")
                    return


            save_books(books)
            print("Book updated successfully!")
            break
        
    if not found:
        print("\nBook not found.\n")