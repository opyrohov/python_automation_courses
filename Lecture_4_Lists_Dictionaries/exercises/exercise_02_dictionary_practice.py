"""
Exercise 2: Dictionary Practice
Practice creating dictionaries, accessing values, and using dictionary methods.
"""

# ============================================
# EXERCISE 1: Create a User Profile
# ============================================
print("=== Exercise 1: User Profile ===")
# TODO: Create a dictionary called 'user' with:
# - name: your name
# - age: your age
# - email: your email
# - city: your city
# TODO: Print the entire dictionary

# Your code here:


print()

# ============================================
# EXERCISE 2: Access Dictionary Values
# ============================================
print("=== Exercise 2: Access Values ===")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "occupation": "Engineer"
}

# TODO: Print the person's name
# TODO: Print the person's occupation
# TODO: Try to get 'phone' using .get() method (it doesn't exist)
# TODO: Get 'phone' with a default value of "Not provided"

# Your code here:


print()

# ============================================
# EXERCISE 3: Modify Dictionary
# ============================================
print("=== Exercise 3: Modify Dictionary ===")
student = {
    "name": "Bob",
    "grade": "A",
    "age": 20
}

# TODO: Change the grade to "A+"
# TODO: Add a new key 'major' with value "Computer Science"
# TODO: Print the updated dictionary

# Your code here:


print()

# ============================================
# EXERCISE 4: Dictionary Methods
# ============================================
print("=== Exercise 4: Dictionary Methods ===")
config = {
    "timeout": 5000,
    "headless": True,
    "viewport": {"width": 1920, "height": 1080}
}

# TODO: Print all keys in the dictionary
# TODO: Print all values in the dictionary
# TODO: Print all key-value pairs using .items()

# Your code here:


print()

# ============================================
# EXERCISE 5: Loop Through Dictionary
# ============================================
print("=== Exercise 5: Loop Through Dictionary ===")
prices = {
    "apple": 1.20,
    "banana": 0.50,
    "orange": 1.50,
    "grape": 2.00
}

# TODO: Loop through and print each item and its price
# Format: "apple costs $1.20"

# Your code here:


print()

# ============================================
# EXERCISE 6: Check if Key Exists
# ============================================
print("=== Exercise 6: Check Key Existence ===")
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 40
}

# TODO: Check if "apples" exists in inventory
# TODO: Check if "grapes" exists in inventory
# TODO: Print appropriate messages for each

# Your code here:


print()

# ============================================
# EXERCISE 7: Update Dictionary
# ============================================
print("=== Exercise 7: Update Dictionary ===")
user_settings = {
    "theme": "dark",
    "notifications": True
}

new_settings = {
    "language": "English",
    "timezone": "UTC"
}

# TODO: Use .update() to add new_settings to user_settings
# TODO: Print the combined dictionary

# Your code here:


print()

# ============================================
# EXERCISE 8: Remove Items
# ============================================
print("=== Exercise 8: Remove Items ===")
cart = {
    "laptop": 999,
    "mouse": 25,
    "keyboard": 75,
    "monitor": 300
}

# TODO: Remove "mouse" using .pop() and store the price
# TODO: Print the removed item's price
# TODO: Print the updated cart

# Your code here:


print()

# ============================================
# EXERCISE 9: Nested Dictionaries
# ============================================
print("=== Exercise 9: Nested Dictionaries ===")
company = {
    "employee1": {
        "name": "Alice",
        "position": "Developer",
        "salary": 80000
    },
    "employee2": {
        "name": "Bob",
        "position": "Designer",
        "salary": 70000
    }
}

# TODO: Print employee1's name
# TODO: Print employee2's position
# TODO: Print employee1's salary

# Your code here:


print()

# ============================================
# CHALLENGE: Count Word Frequency
# ============================================
print("=== CHALLENGE: Word Frequency ===")
text = "apple banana apple cherry banana apple"
words = text.split()

# TODO: Create a dictionary that counts how many times each word appears
# Example output: {"apple": 3, "banana": 2, "cherry": 1}

# Your code here:


print()

# ============================================
# CHALLENGE: Merge Two Dictionaries
# ============================================
print("=== CHALLENGE: Merge Dictionaries ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"a": 10, "e": 5}  # Note: 'a' exists in dict1

# TODO: Merge all three dictionaries into one
# If a key exists in multiple dicts, the last value should win
# Hint: Use .update() or the | operator (Python 3.9+)

# Your code here:


print()

# ============================================
# CHALLENGE: Dictionary from Two Lists
# ============================================
print("=== CHALLENGE: Create Dictionary from Lists ===")
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]

# TODO: Create a dictionary using the keys and values lists
# Hint: Use zip() function

# Your code here:


print()
print("🎉 Excellent work! You've mastered dictionaries!")
