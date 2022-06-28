with open("Week11/books.txt") as books_file:
    print()
    for book in books_file:
        book_strip = book.strip()
        print(book_strip)
print()