"""
Lecture 11: List and Dictionary Comprehensions
This file demonstrates how to use comprehensions for efficient data transformation.
"""

# ============================================
# LIST COMPREHENSIONS - BASICS
# ============================================
print("=" * 60)
print("LIST COMPREHENSIONS - BASICS")
print("=" * 60)

# Traditional way - using a for loop
traditional = []
for x in range(5):
    traditional.append(x * 2)
print(f"Traditional loop: {traditional}")

# List comprehension - more concise
comprehension = [x * 2 for x in range(5)]
print(f"List comprehension: {comprehension}")
print()

# Creating a list of squares
squares = [x ** 2 for x in range(1, 11)]
print(f"Squares: {squares}")

# Creating a list of strings
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase: {uppercase_words}")
print()

# ============================================
# LIST COMPREHENSIONS - WITH CONDITIONS
# ============================================
print("=" * 60)
print("LIST COMPREHENSIONS - WITH CONDITIONS")
print("=" * 60)

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Filter odd numbers
odds = [x for x in numbers if x % 2 != 0]
print(f"Odd numbers: {odds}")

# Filter numbers greater than 5
greater_than_five = [x for x in numbers if x > 5]
print(f"Greater than 5: {greater_than_five}")
print()

# ============================================
# LIST COMPREHENSIONS - WITH IF-ELSE
# ============================================
print("=" * 60)
print("LIST COMPREHENSIONS - WITH IF-ELSE")
print("=" * 60)

# Label numbers as even or odd
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(f"Labels: {labels}")

# Replace negative numbers with 0
numbers_with_negatives = [5, -3, 8, -1, 0, 4]
non_negative = [x if x >= 0 else 0 for x in numbers_with_negatives]
print(f"Non-negative: {non_negative}")

# Categorize ages
ages = [15, 25, 35, 10, 45, 20]
categories = ["adult" if age >= 18 else "minor" for age in ages]
print(f"Categories: {categories}")
print()

# ============================================
# NESTED LIST COMPREHENSIONS
# ============================================
print("=" * 60)
print("NESTED LIST COMPREHENSIONS")
print("=" * 60)

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# Create multiplication table
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication Table:")
for row in multiplication_table:
    print(row)
print()

# ============================================
# DICTIONARY COMPREHENSIONS - BASICS
# ============================================
print("=" * 60)
print("DICTIONARY COMPREHENSIONS - BASICS")
print("=" * 60)

# Create dictionary from range
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Squares dictionary: {squares_dict}")

# Create dictionary from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
print(f"People: {people}")

# Reverse a dictionary
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Reversed: {reversed_dict}")
print()

# ============================================
# DICTIONARY COMPREHENSIONS - WITH CONDITIONS
# ============================================
print("=" * 60)
print("DICTIONARY COMPREHENSIONS - WITH CONDITIONS")
print("=" * 60)

# Filter dictionary by value
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(f"All scores: {scores}")
print(f"High scores (>=90): {high_scores}")

# Filter dictionary by key
data = {"name": "Alice", "age": 25, "city": "NYC", "country": "USA"}
location_only = {k: v for k, v in data.items() if k in ["city", "country"]}
print(f"\nAll data: {data}")
print(f"Location only: {location_only}")
print()

# ============================================
# SET COMPREHENSIONS
# ============================================
print("=" * 60)
print("SET COMPREHENSIONS")
print("=" * 60)

# Create set of unique values
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_squares = {x ** 2 for x in numbers_with_duplicates}
print(f"Original with duplicates: {numbers_with_duplicates}")
print(f"Unique squares: {unique_squares}")

# Set comprehension with condition
words = ["hello", "world", "python", "hi", "programming"]
long_words = {word.upper() for word in words if len(word) > 4}
print(f"\nWords: {words}")
print(f"Long words (>4 chars) in uppercase: {long_words}")
print()

# ============================================
# PRACTICAL EXAMPLES
# ============================================
print("=" * 60)
print("PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Clean and process user input
user_inputs = ["  Alice  ", " bob ", "CHARLIE ", "  david"]
cleaned_names = [name.strip().title() for name in user_inputs]
print(f"User inputs: {user_inputs}")
print(f"Cleaned names: {cleaned_names}")

# Example 2: Extract file extensions
filenames = ["document.pdf", "image.jpg", "script.py", "data.csv"]
extensions = [filename.split('.')[-1] for filename in filenames]
print(f"\nFilenames: {filenames}")
print(f"Extensions: {extensions}")

# Example 3: Convert string numbers to integers
string_numbers = ["10", "20", "30", "40", "50"]
int_numbers = [int(num) for num in string_numbers]
print(f"\nString numbers: {string_numbers}")
print(f"Integer numbers: {int_numbers}")

# Example 4: Create lookup dictionary
products = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Mouse", "price": 25},
    {"id": 3, "name": "Keyboard", "price": 75}
]
product_lookup = {p["id"]: p["name"] for p in products}
print(f"\nProducts: {products}")
print(f"Product lookup: {product_lookup}")

# Example 5: Filter and transform in one step
test_scores = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]
passing_students = [student["name"] for student in test_scores if student["score"] >= 80]
print(f"\nTest scores: {test_scores}")
print(f"Passing students (>=80): {passing_students}")
print()

# ============================================
# PERFORMANCE COMPARISON
# ============================================
print("=" * 60)
print("PERFORMANCE NOTE")
print("=" * 60)
print("List comprehensions are typically faster than traditional loops")
print("because they are optimized at the C level in Python.")
print("\nComprehensions also:")
print("  ✓ Are more concise and readable")
print("  ✓ Follow Python best practices (Pythonic code)")
print("  ✓ Reduce the chance of errors")
print("  ✓ Make code easier to maintain")
