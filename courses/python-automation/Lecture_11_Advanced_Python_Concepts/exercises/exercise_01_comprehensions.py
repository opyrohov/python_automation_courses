"""
Exercise 1: List and Dictionary Comprehensions

Instructions:
1. Complete each task below by writing the appropriate comprehension
2. Run the file to check your results
3. Try to solve each task using comprehensions (not traditional loops)

Estimated time: 20-25 minutes
"""

# ============================================
# TASK 1: Basic List Comprehension
# ============================================
# Create a list of squares for numbers 1 through 10
# YOUR CODE HERE:
squares = []  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 1: Squares")
print("=" * 50)
print(f"Squares 1-10: {squares}")
print(f"Expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]")
print()

# ============================================
# TASK 2: List Comprehension with Condition
# ============================================
# Create a list of even numbers from 1 to 20
# YOUR CODE HERE:
evens = []  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 2: Even Numbers")
print("=" * 50)
print(f"Evens 1-20: {evens}")
print(f"Expected: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]")
print()

# ============================================
# TASK 3: List Comprehension with If-Else
# ============================================
# Create a list that labels numbers 1-10 as "even" or "odd"
# YOUR CODE HERE:
labels = []  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 3: Even/Odd Labels")
print("=" * 50)
print(f"Labels: {labels}")
print(f"Expected: ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']")
print()

# ============================================
# TASK 4: Transform Strings
# ============================================
# Convert all names to uppercase using list comprehension
names = ["alice", "bob", "charlie", "david"]
# YOUR CODE HERE:
uppercase_names = []  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 4: Uppercase Names")
print("=" * 50)
print(f"Original: {names}")
print(f"Uppercase: {uppercase_names}")
print(f"Expected: ['ALICE', 'BOB', 'CHARLIE', 'DAVID']")
print()

# ============================================
# TASK 5: Filter and Transform
# ============================================
# Get lengths of words that are longer than 3 characters
words = ["hi", "hello", "hey", "python", "code"]
# YOUR CODE HERE:
long_word_lengths = []  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 5: Long Word Lengths")
print("=" * 50)
print(f"Words: {words}")
print(f"Long word lengths: {long_word_lengths}")
print(f"Expected: [5, 6, 4]")
print()

# ============================================
# TASK 6: Nested List Comprehension
# ============================================
# Flatten this 2D list using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# YOUR CODE HERE:
flattened = []  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 6: Flatten Matrix")
print("=" * 50)
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")
print(f"Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]")
print()

# ============================================
# TASK 7: Dictionary Comprehension
# ============================================
# Create a dictionary mapping numbers 1-5 to their cubes
# YOUR CODE HERE:
cubes_dict = {}  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 7: Cubes Dictionary")
print("=" * 50)
print(f"Cubes: {cubes_dict}")
print(f"Expected: {{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}}")
print()

# ============================================
# TASK 8: Dictionary from Two Lists
# ============================================
# Create a dictionary mapping keys to values using comprehension
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
# YOUR CODE HERE:
person = {}  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 8: Person Dictionary")
print("=" * 50)
print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Person: {person}")
print(f"Expected: {{'name': 'Alice', 'age': 25, 'city': 'NYC'}}")
print()

# ============================================
# TASK 9: Filter Dictionary
# ============================================
# Create a new dictionary with only items where value > 50
scores = {"Alice": 85, "Bob": 45, "Charlie": 92, "David": 38}
# YOUR CODE HERE:
high_scores = {}  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 9: High Scores")
print("=" * 50)
print(f"All scores: {scores}")
print(f"High scores (>50): {high_scores}")
print(f"Expected: {{'Alice': 85, 'Charlie': 92}}")
print()

# ============================================
# TASK 10: Test Data Generation (Practical)
# ============================================
# Generate test user data: create a list of dictionaries
# Each dictionary should have "id" (1-5) and "email" (user{id}@test.com)
# YOUR CODE HERE:
test_users = []  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("TASK 10: Test User Data")
print("=" * 50)
print("Generated test users:")
for user in test_users:
    print(f"  {user}")
print("Expected:")
print("  {'id': 1, 'email': 'user1@test.com'}")
print("  {'id': 2, 'email': 'user2@test.com'}")
print("  ... etc")
print()

# ============================================
# BONUS TASK: Extract File Extensions
# ============================================
# Extract unique file extensions from this list
filenames = ["doc.pdf", "image.jpg", "script.py", "data.csv", "photo.jpg", "report.pdf"]
# YOUR CODE HERE (use set comprehension):
extensions = set()  # Replace with comprehension

# Test your code (don't modify this)
print("=" * 50)
print("BONUS: Unique Extensions")
print("=" * 50)
print(f"Filenames: {filenames}")
print(f"Unique extensions: {extensions}")
print(f"Expected: {{'pdf', 'jpg', 'py', 'csv'}} (order may vary)")
print()

print("=" * 50)
print("Congratulations! You completed Exercise 1!")
print("=" * 50)
