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

# Shows the books in library

    elif option == "2":
        if len(books) == 0:
            print("\nno books found\n")
        else:
            print("\n===== Books =====\n")
            for book in books:
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Year:", book["year"])
                print("ISBN:", book["isbn"])
                print("\n----------------------\n")

        
    elif option == "3":
        print("Bye!")
        break
    else:
        print("\nInvalid option.\n")