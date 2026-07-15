print("===== Library Management System =====")

books = []

print("1 - Add Book")
print("2 - List Books")
print("3 - Exit")

option = input("Choose an option: ")

print(option)

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

    print("Book added successfully!")



elif option == "2":
    print("Listing books...")
elif option == "3":
    print("Bye!")
else:
    print("Invalid option.")


'''
books = []
book = {
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "year": 1997,
        "isbn": "978..."
    }
books.append(book)
book = {
        "title": "The Hobbit",
        "author": "J.R.R Tolkien",
        "year": 1937,
        "isbn": "978..."
    }
books.append(book)

for book in books:
    print(book["title"])
'''