"""
Example 1: Lists Basics
Demonstrates creating, accessing, and modifying lists in Python.
"""

print("=" * 60)
print("LISTS BASICS EXAMPLES")
print("=" * 60)
print()

# ============================================
# Creating Lists
# ============================================
print("1. CREATING LISTS")
print("-" * 40)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with numbers
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# List with strings
fruits = ["apple", "banana", "cherry", "date"]
print(f"Fruits: {fruits}")

# Mixed types (not recommended but possible)
mixed = [1, "hello", 3.14, True, None]
print(f"Mixed types: {mixed}")

# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix:\n{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
print()

# ============================================
# Accessing List Items
# ============================================
print("2. ACCESSING LIST ITEMS")
print("-" * 40)

colors = ["red", "green", "blue", "yellow", "purple"]

# Access by index (starts at 0)
print(f"First color: {colors[0]}")
print(f"Third color: {colors[2]}")

# Negative indexing (from the end)
print(f"Last color: {colors[-1]}")
print(f"Second from last: {colors[-2]}")

# Get length
print(f"Total colors: {len(colors)}")

# Check if item exists
print(f"Is 'blue' in colors? {'blue' in colors}")
print(f"Is 'orange' in colors? {'orange' in colors}")
print()

# ============================================
# List Slicing
# ============================================
print("3. LIST SLICING")
print("-" * 40)

numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Get first 3 items
print(f"First 3: {numbers[0:3]}")
print(f"First 3 (shorthand): {numbers[:3]}")

# Get items from index 5 to end
print(f"From index 5: {numbers[5:]}")

# Get last 3 items
print(f"Last 3: {numbers[-3:]}")

# Get every other item
print(f"Every other item: {numbers[::2]}")

# Get every third item
print(f"Every third item: {numbers[::3]}")

# Reverse a list
print(f"Reversed: {numbers[::-1]}")

# Get items from index 2 to 7
print(f"Index 2 to 7: {numbers[2:8]}")
print()

# ============================================
# Adding Items to Lists
# ============================================
print("4. ADDING ITEMS")
print("-" * 40)

shopping_cart = ["milk", "bread"]
print(f"Initial cart: {shopping_cart}")

# append() - Add to end
shopping_cart.append("eggs")
print(f"After append('eggs'): {shopping_cart}")

# insert() - Add at specific position
shopping_cart.insert(1, "butter")
print(f"After insert(1, 'butter'): {shopping_cart}")

# extend() - Add multiple items
shopping_cart.extend(["cheese", "yogurt"])
print(f"After extend(['cheese', 'yogurt']): {shopping_cart}")

# Using + operator
more_items = ["apples", "bananas"]
shopping_cart = shopping_cart + more_items
print(f"After + operator: {shopping_cart}")
print()

# ============================================
# Removing Items from Lists
# ============================================
print("5. REMOVING ITEMS")
print("-" * 40)

todo_list = ["task1", "task2", "task3", "task4", "task5"]
print(f"Initial list: {todo_list}")

# remove() - Remove first occurrence
todo_list.remove("task2")
print(f"After remove('task2'): {todo_list}")

# pop() - Remove and return last item
last_task = todo_list.pop()
print(f"Popped task: {last_task}")
print(f"After pop(): {todo_list}")

# pop(index) - Remove and return item at index
second_task = todo_list.pop(1)
print(f"Popped task at index 1: {second_task}")
print(f"After pop(1): {todo_list}")

# clear() - Remove all items
backup = todo_list.copy()
todo_list.clear()
print(f"After clear(): {todo_list}")
print(f"Backup kept: {backup}")
print()

# ============================================
# Modifying Lists
# ============================================
print("6. MODIFYING LISTS")
print("-" * 40)

scores = [85, 72, 90, 68, 95]
print(f"Original scores: {scores}")

# Change single item
scores[1] = 78
print(f"After changing index 1: {scores}")

# Change multiple items
scores[2:4] = [92, 75]
print(f"After changing slice [2:4]: {scores}")

# Sort in place
scores.sort()
print(f"After sort(): {scores}")

# Sort in reverse
scores.sort(reverse=True)
print(f"After sort(reverse=True): {scores}")

# Reverse the list
scores.reverse()
print(f"After reverse(): {scores}")
print()

# ============================================
# List Methods
# ============================================
print("7. USEFUL LIST METHODS")
print("-" * 40)

numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"Numbers: {numbers}")

# count() - Count occurrences
count_of_2 = numbers.count(2)
print(f"Count of 2: {count_of_2}")

# index() - Find position of item
position_of_4 = numbers.index(4)
print(f"Position of 4: {position_of_4}")

# copy() - Create a copy
numbers_copy = numbers.copy()
numbers_copy.append(100)
print(f"Original: {numbers}")
print(f"Copy: {numbers_copy}")

# min(), max(), sum()
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print()

# ============================================
# List Comprehensions (Preview)
# ============================================
print("8. LIST COMPREHENSIONS (BONUS)")
print("-" * 40)

# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# List comprehension way
squares = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares}")

# With condition
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Transform strings
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(f"Uppercase fruits: {uppercase_fruits}")
print()

# ============================================
# Common Patterns
# ============================================
print("9. COMMON PATTERNS")
print("-" * 40)

# Check if list is empty
my_list = []
if not my_list:
    print("List is empty")

# Iterate with index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print()

# Join list into string
words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(f"Joined: {sentence}")

# Split string into list
text = "apple,banana,cherry"
fruits_list = text.split(",")
print(f"Split: {fruits_list}")

print()
print("=" * 60)
print("✅ Lists basics examples completed!")
print("=" * 60)
