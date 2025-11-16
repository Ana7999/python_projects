book = input()
found_book = ""
book_counter = 0

while book != found_book or found_book != "No More Books":
    found_book = input()
    if found_book == "No More Books":
        print(f"The book you search is not here!\n You checked {book_counter} books.")
        break

    if found_book == book:
        print(f"You checked {book_counter} books and found it.")
        break


    book_counter += 1