# Program to perform various operations on Python lists

# Creating a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# 1. Accessing elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# 2. Adding an element using append()
numbers.append(60)
print("After append():", numbers)

# 3. Inserting an element using insert()
numbers.insert(2, 25)
print("After insert():", numbers)

# 4. Removing an element using remove()
numbers.remove(30)
print("After remove():", numbers)

# 5. Removing the last element using pop()
numbers.pop()
print("After pop():", numbers)

# 6. Finding length using len()
print("Length of List:", len(numbers))

# 7. Sorting the list
numbers.sort()
print("After sort():", numbers)

# 8. Reversing the list
numbers.reverse()
print("After reverse():", numbers)

# 9. Counting an element
print("Count of 20:", numbers.count(20))

# 10. Finding index of an element
print("Index of 20:", numbers.index(20))

# 11. Finding maximum and minimum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# 12. Finding sum
print("Sum:", sum(numbers))