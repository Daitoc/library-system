#Save books in the library
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