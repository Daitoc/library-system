print("Library Management System")

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
