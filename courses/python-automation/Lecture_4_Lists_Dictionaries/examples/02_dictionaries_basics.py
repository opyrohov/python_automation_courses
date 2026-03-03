"""
Example 2: Dictionaries Basics
Demonstrates creating, accessing, and modifying dictionaries in Python.
"""

print("=" * 60)
print("DICTIONARIES BASICS EXAMPLES")
print("=" * 60)
print()

# ============================================
# Creating Dictionaries
# ============================================
print("1. CREATING DICTIONARIES")
print("-" * 40)

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with values
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person: {person}")

# Using dict() constructor
car = dict(brand="Toyota", model="Camry", year=2023)
print(f"Car: {car}")

# Dictionary with different value types
user = {
    "username": "john_doe",
    "age": 30,
    "is_active": True,
    "hobbies": ["reading", "coding", "gaming"],
    "address": {
        "street": "123 Main St",
        "city": "Boston"
    }
}
print(f"User: {user}")
print()

# ============================================
# Accessing Values
# ============================================
print("2. ACCESSING VALUES")
print("-" * 40)

student = {
    "name": "Bob",
    "grade": "A",
    "age": 20,
    "major": "Computer Science"
}

# Using bracket notation
print(f"Name: {student['name']}")
print(f"Grade: {student['grade']}")

# Using get() method (safer)
print(f"Age: {student.get('age')}")
print(f"Email (doesn't exist): {student.get('email')}")
print(f"Email with default: {student.get('email', 'not provided')}")

# Check if key exists
print(f"Has 'name' key? {'name' in student}")
print(f"Has 'email' key? {'email' in student}")
print()

# ============================================
# Adding and Modifying
# ============================================
print("3. ADDING AND MODIFYING")
print("-" * 40)

config = {
    "timeout": 5000,
    "headless": True
}
print(f"Initial config: {config}")

# Add new key-value pair
config["url"] = "https://example.com"
print(f"After adding 'url': {config}")

# Modify existing value
config["timeout"] = 10000
print(f"After modifying 'timeout': {config}")

# Update multiple values at once
config.update({
    "browser": "chrome",
    "viewport": {"width": 1920, "height": 1080}
})
print(f"After update(): {config}")
print()

# ============================================
# Removing Items
# ============================================
print("4. REMOVING ITEMS")
print("-" * 40)

inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 40,
    "grapes": 25
}
print(f"Initial inventory: {inventory}")

# pop() - Remove and return value
apples_count = inventory.pop("apples")
print(f"Removed apples: {apples_count}")
print(f"After pop('apples'): {inventory}")

# popitem() - Remove and return last item (Python 3.7+)
last_item = inventory.popitem()
print(f"Removed last item: {last_item}")
print(f"After popitem(): {inventory}")

# del statement
del inventory["bananas"]
print(f"After del inventory['bananas']: {inventory}")

# clear() - Remove all items
backup = inventory.copy()
inventory.clear()
print(f"After clear(): {inventory}")
print(f"Backup: {backup}")
print()

# ============================================
# Dictionary Methods
# ============================================
print("5. DICTIONARY METHODS")
print("-" * 40)

colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF"
}

# keys() - Get all keys
print(f"Keys: {list(colors.keys())}")

# values() - Get all values
print(f"Values: {list(colors.values())}")

# items() - Get all key-value pairs
print(f"Items: {list(colors.items())}")

# copy() - Create a copy
colors_copy = colors.copy()
colors_copy["yellow"] = "#FFFF00"
print(f"Original: {colors}")
print(f"Copy: {colors_copy}")

# setdefault() - Get value or set default
result = colors.setdefault("purple", "#800080")
print(f"setdefault result: {result}")
print(f"After setdefault: {colors}")
print()

# ============================================
# Looping Through Dictionaries
# ============================================
print("6. LOOPING THROUGH DICTIONARIES")
print("-" * 40)

prices = {
    "apple": 1.20,
    "banana": 0.50,
    "orange": 1.50,
    "grape": 2.00
}

# Loop through keys (default)
print("Loop through keys:")
for key in prices:
    print(f"  {key}")

print("\nLoop through values:")
for value in prices.values():
    print(f"  ${value}")

print("\nLoop through both keys and values:")
for key, value in prices.items():
    print(f"  {key}: ${value}")

print("\nLoop with enumeration:")
for index, (fruit, price) in enumerate(prices.items(), 1):
    print(f"  {index}. {fruit}: ${price}")
print()

# ============================================
# Nested Dictionaries
# ============================================
print("7. NESTED DICTIONARIES")
print("-" * 40)

employees = {
    "emp001": {
        "name": "Alice Johnson",
        "position": "Developer",
        "salary": 80000,
        "skills": ["Python", "JavaScript", "SQL"]
    },
    "emp002": {
        "name": "Bob Smith",
        "position": "Designer",
        "salary": 70000,
        "skills": ["Photoshop", "Illustrator", "Figma"]
    },
    "emp003": {
        "name": "Carol Williams",
        "position": "Manager",
        "salary": 90000,
        "skills": ["Leadership", "Planning", "Communication"]
    }
}

# Access nested values
print(f"Employee 001 name: {employees['emp001']['name']}")
print(f"Employee 002 position: {employees['emp002']['position']}")
print(f"Employee 001 first skill: {employees['emp001']['skills'][0]}")

print("\nAll employees:")
for emp_id, emp_data in employees.items():
    print(f"{emp_id}: {emp_data['name']} - {emp_data['position']}")
print()

# ============================================
# Dictionary Comprehensions
# ============================================
print("8. DICTIONARY COMPREHENSIONS (BONUS)")
print("-" * 40)

# Create dictionary from list
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}
print(f"Squares dictionary: {squares_dict}")

# Filter dictionary
all_scores = {"Alice": 85, "Bob": 92, "Carol": 78, "David": 95, "Eve": 88}
high_scores = {name: score for name, score in all_scores.items() if score >= 90}
print(f"High scores (>=90): {high_scores}")

# Transform dictionary values
celsius = {"morning": 20, "afternoon": 25, "evening": 18}
fahrenheit = {time: (temp * 9/5) + 32 for time, temp in celsius.items()}
print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")
print()

# ============================================
# Common Patterns
# ============================================
print("9. COMMON PATTERNS")
print("-" * 40)

# Check if dictionary is empty
my_dict = {}
if not my_dict:
    print("Dictionary is empty")

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(f"Merged (Python 3.9+): {merged}")

# Merge using update (works in all versions)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(f"Merged using update: {dict1}")

# Count occurrences
text = "hello world hello python python python"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"\nWord count: {word_count}")

# Default dictionary pattern
from collections import defaultdict
scores = defaultdict(list)
scores["Alice"].append(85)
scores["Alice"].append(90)
scores["Bob"].append(78)
print(f"\nDefaultdict scores: {dict(scores)}")

print()
print("=" * 60)
print("✅ Dictionaries basics examples completed!")
print("=" * 60)
