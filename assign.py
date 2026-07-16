# ==========================================================
# Library Management System
# CS1101 Unit 5 Assignment
# ==========================================================

print("=" * 60)
print("      LIBRARY MANAGEMENT SYSTEM")
print("=" * 60)

# ==========================================================
# QUESTION 1
# ==========================================================

print("\nQUESTION 1: Managing Book Titles")

books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]

print("\nOriginal Book List")
print(books)

books.append("The Great Gatsby")
books.append("To Kill a Mockingbird")

print("\nAfter Adding Books")
print(books)

books.remove("Moby Dick")

print("\nAfter Removing Damaged Book")
print(books)

books.sort()

print("\nAlphabetically Sorted Book List")

for book in books:
    print(book)

# ==========================================================
# QUESTION 2
# ==========================================================

print("\n" + "=" * 60)
print("QUESTION 2: Borrower Details")
print("=" * 60)

borrower = ("John Doe", "B1023", "2025-10-15")

print("\nBorrower Tuple")
print(borrower)

print("\nAttempting to Modify Tuple")

try:
    borrower[0] = "Jane Doe"
except TypeError as error:
    print("Error:", error)

print("\nNumber of Fields:", len(borrower))

labels = ("Name", "Library ID", "Membership Date")

print("\nBorrower Information")

for label, value in zip(labels, borrower):
    print(label + ":", value)

# ==========================================================
# QUESTION 3
# ==========================================================

print("\n" + "=" * 60)
print("QUESTION 3: Tuple Packing and Unpacking")
print("=" * 60)

book_info = ("The Alchemist", "Paulo Coelho", 1988)

title, author, year = book_info

print("\nBook Information")
print("Title:", title)
print("Author:", author)
print("Publication Year:", year)

# ==========================================================
# QUESTION 4
# ==========================================================

print("\n" + "=" * 60)
print("QUESTION 4: Indexing and Slicing")
print("=" * 60)

borrowed_books = [23, 19, 31, 27, 22, 30, 25]

print("\nOriginal Weekly Borrowing Statistics")
print(borrowed_books)

weeks_2_to_5 = borrowed_books[1:5]

borrowed_books[0] = 20

print("\nUpdated Weekly Borrowing Statistics")
print(borrowed_books)

print("\nWeeks 2–5 Borrowing Data")
print(weeks_2_to_5)

# ==========================================================
# END OF PROGRAM
# ==========================================================

print("\n" + "=" * 60)
print("Library Management System Completed Successfully")
print("=" * 60)
