print("input the number of students:")
no_students = int(input())
print("input the number of books:")
no_books = int(input())
div = no_students%no_books
mod = no_students//no_books
print("each student will receive", mod, "books with", div, "left over")