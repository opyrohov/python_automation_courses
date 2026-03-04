# Lecture 4: Lists and Dictionaries

Data collections in Python.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_4_Lists_Dictionaries/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_4_Lists_Dictionaries/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_4_Lists_Dictionaries/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- Lists
- List methods
- Dictionaries
- Dictionary methods
- Tuples and sets

## Lists

```python
# Creation
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]
empty = []

# Access by index
first = fruits[0]    # "apple"
last = fruits[-1]    # "cherry"

# Slice
subset = fruits[0:2]  # ["apple", "banana"]
```

## List Methods

```python
fruits = ["apple", "banana"]

# Adding
fruits.append("cherry")        # ["apple", "banana", "cherry"]
fruits.insert(1, "orange")     # ["apple", "orange", "banana", "cherry"]
fruits.extend(["grape", "kiwi"])

# Removing
fruits.remove("banana")        # removes first occurrence
popped = fruits.pop()          # removes and returns last item
del fruits[0]                  # removes by index
fruits.clear()                 # clears the list

# Searching
index = fruits.index("apple")  # index of element
count = fruits.count("apple")  # number of occurrences
exists = "apple" in fruits     # True/False

# Sorting
numbers.sort()                 # sorts in place
numbers.sort(reverse=True)     # reverse order
sorted_list = sorted(numbers)  # returns a new list

# Other
numbers.reverse()              # reverses the list
length = len(numbers)          # length
```

## Dictionaries

```python
# Creation
user = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Access
name = user["name"]           # KeyError if not found
name = user.get("name")       # None if not found
name = user.get("name", "N/A") # default value

# Modifying/Adding
user["age"] = 31
user["phone"] = "123-456"

# Removing
del user["phone"]
age = user.pop("age")
```

## Dictionary Methods

```python
user = {"name": "John", "age": 30}

# Keys, values, pairs
keys = user.keys()       # dict_keys(['name', 'age'])
values = user.values()   # dict_values(['John', 30])
items = user.items()     # dict_items([('name', 'John'), ('age', 30)])

# Iteration
for key in user:
    print(f"{key}: {user[key]}")

for key, value in user.items():
    print(f"{key}: {value}")

# Checking
"name" in user           # True
"email" in user          # False

# Updating
user.update({"age": 31, "city": "NYC"})

# Copying
user_copy = user.copy()
```

## Tuples

```python
# Immutable sequence
point = (10, 20)
single = (42,)  # comma is required for a single element

# Unpacking
x, y = point

# As dictionary keys (because they are immutable)
locations = {
    (0, 0): "origin",
    (1, 0): "right"
}
```

## Sets

```python
# Unique elements
numbers = {1, 2, 3, 3, 2, 1}  # {1, 2, 3}

# Operations
a = {1, 2, 3}
b = {2, 3, 4}

a | b  # union: {1, 2, 3, 4}
a & b  # intersection: {2, 3}
a - b  # difference: {1}
a ^ b  # symmetric difference: {1, 4}
```

## Exercises

::: tip Exercise 1
Create a dictionary with information about 3 books (title, author, year).
:::

::: tip Exercise 2
Write a function to count the frequency of words in a text.
:::

[Code examples on GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_4_Lists_Dictionaries/examples)
