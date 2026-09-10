# Student Data System
# Aim: To understand Python building blocks, data types,
# and basic input-output operations.

print("===== STUDENT DATA SYSTEM =====")

# Taking input from the user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
age = int(input("Enter age: "))
course = input("Enter course: ")
marks = float(input("Enter marks: "))

# Calculating result
if marks >= 40:
    result = "Pass"
else:
    result = "Fail"

# Displaying student information
print("\n===== STUDENT DETAILS =====")
print("Name       :", name)
print("Roll No.   :", roll_no)
print("Age        :", age)
print("Course     :", course)
print("Marks      :", marks)
print("Result     :", result)

# Demonstrating different data types
print("\n===== DATA TYPES =====")
print("Name data type   :", type(name))
print("Roll No. type    :", type(roll_no))
print("Age data type    :", type(age))
print("Marks data type  :", type(marks))
print("Result data type :", type(result))

print("\nStudent data recorded successfully!")