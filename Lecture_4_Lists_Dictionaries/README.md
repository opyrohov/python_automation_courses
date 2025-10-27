# Lecture 4: Lists & Dictionaries

Welcome to the fourth lecture of the Python Automation Course! In this lecture, you'll learn how to work with Python's two most important data structures - essential for organizing and managing test data in automation.

## Table of Contents
1. [Lists](#lists)
2. [Dictionaries](#dictionaries)
3. [Combining Lists and Dictionaries](#combining-lists-and-dictionaries)
4. [Why This Matters for Playwright](#why-this-matters-for-playwright)
5. [Practice Exercises](#practice-exercises)

## Lists

Lists are ordered collections that allow you to store multiple values in a single variable.

### Key Concepts:
- **Creating lists**: Empty lists, lists with values, nested lists
- **Accessing items**: Indexing (positive and negative), length
- **Slicing**: Getting subsets of lists
- **Adding items**: append(), insert(), extend()
- **Removing items**: remove(), pop(), clear()
- **List methods**: sort(), reverse(), count(), index()
- **List comprehensions**: Creating lists in a concise way

See `examples/01_lists_basics.py` for code examples.

## Dictionaries

Dictionaries store data as key-value pairs, allowing fast lookups and organized data storage.

### Key Concepts:
- **Creating dictionaries**: Empty dicts, dicts with values
- **Accessing values**: Bracket notation vs .get() method
- **Adding/modifying**: Setting new keys, updating values
- **Removing items**: pop(), popitem(), del, clear()
- **Dictionary methods**: keys(), values(), items(), update()
- **Looping**: Iterating through keys, values, or both
- **Nested dictionaries**: Dictionaries within dictionaries

See `examples/02_dictionaries_basics.py` for code examples.

## Combining Lists and Dictionaries

The real power comes from combining these structures for complex data organization.

### Key Patterns:
- **List of dictionaries**: Multiple records with the same structure
- **Dictionary of lists**: Grouping items by category
- **Nested structures**: Complex data hierarchies
- **Real-world data**: JSON-like structures
- **Data transformation**: Converting between formats

See `examples/03_combining_lists_dicts.py` for code examples.

## Why This Matters for Playwright

Lists and dictionaries are fundamental to organizing test data and making your automation code maintainable and scalable.

### Lists in Automation:
- **Multiple URLs**: Test multiple pages in a loop
- **Test data sets**: Run the same test with different inputs
- **Locator collections**: Store multiple selectors
- **Expected results**: Compare actual vs expected lists
- **Navigation paths**: Define sequences of actions

### Dictionaries in Automation:
- **Form data**: Organize field names and values
- **Configuration**: Store test settings and environment configs
- **Page objects**: Map element names to selectors
- **User credentials**: Store login information
- **API responses**: Parse and validate JSON data

### Common Automation Patterns:
- **Data-driven testing**: List of test case dictionaries
- **Form filling**: Dictionary mapping fields to values
- **Multi-environment testing**: Dictionary of environment configs
- **Test results**: Dictionary tracking passed/failed/skipped tests
- **Element collections**: List of elements to interact with

See `examples/04_playwright_examples.py` for practical automation examples.

## Practice Exercises

Complete the exercises in the `exercises/` folder to reinforce what you've learned:
- `exercise_01_list_practice.py` - List operations and methods
- `exercise_02_dictionary_practice.py` - Dictionary manipulation
- `exercise_03_playwright_scenarios.py` - Automation-focused exercises

Solutions are available in `exercises/SOLUTIONS.md`.

## Running Your Code

```bash
# Run any Python file
python filename.py

# Or
python3 filename.py
```

## Quick Reference

### Lists
```python
# Create
my_list = [1, 2, 3]

# Access
first = my_list[0]
last = my_list[-1]

# Add
my_list.append(4)
my_list.extend([5, 6])

# Remove
my_list.remove(2)
item = my_list.pop()

# Slice
subset = my_list[1:3]
```

### Dictionaries
```python
# Create
my_dict = {"name": "Alice", "age": 25}

# Access
name = my_dict["name"]
age = my_dict.get("age")

# Add/Modify
my_dict["city"] = "NYC"
my_dict["age"] = 26

# Remove
city = my_dict.pop("city")

# Loop
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

## Next Steps

After completing this lecture, you should be comfortable with:
- Creating and manipulating lists
- Working with dictionaries and key-value pairs
- Combining lists and dictionaries for complex data structures
- Using these structures to organize test data
- Understanding how they enable data-driven testing

Move on to Lecture 5 when you're ready!
