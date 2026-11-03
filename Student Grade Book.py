grade_book = ["name: Shaheer", "score: 80", "name: Arshad", "score: 75", "name: Ali", "score: 85", "name: Abdullah", "score: 70", "name: Muhammad", "score: 90"]
max_grade = max(grade_book, key=lambda x: x.split(": ")[1])
min_grade = min(grade_book, key=lambda x: x.split(": ")[1])
search = input("Enter a student to search for: ")
for student in grade_book:
    if search in student:
        print(search, "found with a grade of: ", student.split(": ")[1])
if search not in grade_book:
    print("Student not found")