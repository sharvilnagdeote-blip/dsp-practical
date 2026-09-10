# Program to perform operations on Tuple, Set and Dictionary

# ---------------- TUPLE ----------------
print("----- TUPLE OPERATIONS -----")

t = (10, 20, 30, 40, 50)

print("Original Tuple:", t)
print("First Element:", t[0])
print("Last Element:", t[-1])
print("Length:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# ---------------- SET ----------------
print("\n----- SET OPERATIONS -----")

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print("Set 1:", s1)
print("Set 2:", s2)

print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference:", s1.difference(s2))

s1.add(70)
print("After adding 70:", s1)

s1.remove(20)
print("After removing 20:", s1)

# ---------------- DICTIONARY ----------------
print("\n----- DICTIONARY OPERATIONS -----")

student = {
    "name": "Sonal",
    "age": 20,
    "course": "BSc"
}

print("Original Dictionary:", student)

# Accessing values
print("Name:", student["name"])

# Adding a new key-value pair
student["marks"] = 85
print("After adding marks:", student)

# Updating a value
student["age"] = 21
print("After updating age:", student)

# Removing a key-value pair
student.pop("course")
print("After removing course:", student)

# Displaying keys and values
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())