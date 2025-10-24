"""
Lecture 3: For Loops
This file demonstrates how to use for loops to iterate over sequences in Python.
"""

# ============================================
# BASIC FOR LOOP WITH LIST
# ============================================
print("=== Basic For Loop with List ===")

fruits = ["apple", "banana", "cherry", "orange"]

for fruit in fruits:
    print(f"I like {fruit}s")

print()

# ============================================
# FOR LOOP WITH NUMBERS
# ============================================
print("=== For Loop with Numbers ===")

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"Number: {num}, Squared: {num ** 2}")

print()

# ============================================
# ITERATING OVER A STRING
# ============================================
print("=== Iterating Over a String ===")

message = "Python"

for letter in message:
    print(f"Letter: {letter}")

print()

# ============================================
# USING RANGE() WITH FOR LOOPS
# ============================================
print("=== Using range() ===")

# range(stop) - counts from 0 to stop-1
print("Counting 0 to 4:")
for i in range(5):
    print(i, end=" ")
print("\n")

# range(start, stop) - counts from start to stop-1
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

# range(start, stop, step) - counts with custom increment
print("Counting by 2s:")
for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

print()

# ============================================
# COUNTING BACKWARDS
# ============================================
print("=== Counting Backwards ===")

for i in range(10, 0, -1):
    print(i, end=" ")
print("Blast off!")

print()

# ============================================
# ITERATING WITH INDEX
# ============================================
print("=== Iterating with Index ===")

colors = ["red", "green", "blue", "yellow"]

for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")

print()

# ============================================
# ENUMERATE - GETTING INDEX AND VALUE
# ============================================
print("=== Using enumerate() ===")

programming_languages = ["Python", "JavaScript", "Java", "C++"]

for index, language in enumerate(programming_languages):
    print(f"{index + 1}. {language}")

print()

# Starting enumerate from a different number
for index, language in enumerate(programming_languages, start=1):
    print(f"Language #{index}: {language}")

print()

# ============================================
# NESTED FOR LOOPS
# ============================================
print("=== Nested For Loops ===")

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()

# ============================================
# ITERATING OVER MULTIPLE LISTS WITH ZIP
# ============================================
print("=== Using zip() with Multiple Lists ===")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

print()

# ============================================
# ACCUMULATING VALUES IN A LOOP
# ============================================
print("=== Accumulating Values ===")

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num
    print(f"Added {num}, running total: {total}")

print(f"Final total: {total}")

print()

# ============================================
# BUILDING A LIST WITH A LOOP
# ============================================
print("=== Building a List ===")

squares = []

for i in range(1, 6):
    squares.append(i ** 2)

print(f"Squares: {squares}")

print()

# ============================================
# LIST COMPREHENSION (ADVANCED)
# ============================================
print("=== List Comprehension (Quick Way) ===")

# Same as above, but in one line
squares_compact = [i ** 2 for i in range(1, 6)]
print(f"Squares: {squares_compact}")

# With a condition
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

print()

# ============================================
# PRACTICAL EXAMPLE: PROCESSING DATA
# ============================================
print("=== Practical Example: Processing User Data ===")

users = [
    {"name": "Alice", "age": 25, "role": "admin"},
    {"name": "Bob", "age": 30, "role": "user"},
    {"name": "Charlie", "age": 35, "role": "user"},
    {"name": "Diana", "age": 28, "role": "admin"}
]

print("Admin users:")
for user in users:
    if user["role"] == "admin":
        print(f"  - {user['name']} (age {user['age']})")

print()

# ============================================
# PRACTICAL EXAMPLE: COUNTING ITEMS
# ============================================
print("=== Practical Example: Counting Occurrences ===")

responses = ["yes", "no", "yes", "yes", "no", "yes", "maybe"]

yes_count = 0
no_count = 0
maybe_count = 0

for response in responses:
    if response == "yes":
        yes_count += 1
    elif response == "no":
        no_count += 1
    elif response == "maybe":
        maybe_count += 1

print(f"Results: {yes_count} yes, {no_count} no, {maybe_count} maybe")

print()

# ============================================
# PRACTICAL EXAMPLE: FINDING MAX VALUE
# ============================================
print("=== Practical Example: Finding Maximum ===")

scores = [85, 92, 78, 95, 88]

max_score = scores[0]  # Start with first score

for score in scores:
    if score > max_score:
        max_score = score

print(f"Scores: {scores}")
print(f"Highest score: {max_score}")

print()

# ============================================
# PRACTICAL EXAMPLE: STRING MANIPULATION
# ============================================
print("=== Practical Example: String Manipulation ===")

sentence = "Python automation is powerful"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1

print(f"Sentence: '{sentence}'")
print(f"Number of vowels: {vowel_count}")
