# Lecture 3: Exercise Solutions

This file contains complete solutions for all exercises in Lecture 3.

---

## Exercise 1: Loop Practice

### Exercise 1: Print Numbers
```python
print("=== Exercise 1: Print Numbers ===")
for i in range(1, 11):
    print(i)
```

### Exercise 2: Print Fruits
```python
print("=== Exercise 2: Print Fruits ===")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(fruit)
```

### Exercise 3: Sum of Numbers
```python
print("=== Exercise 3: Sum of Numbers ===")
numbers = [10, 20, 30, 40, 50]

total = 0
for num in numbers:
    total += num

print(f"Total: {total}")
```

### Exercise 4: Count Even Numbers
```python
print("=== Exercise 4: Count Even Numbers ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1

print(f"Even numbers: {even_count}")
```

### Exercise 5: Multiplication Table
```python
print("=== Exercise 5: Multiplication Table ===")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
```

### Exercise 6: Countdown
```python
print("=== Exercise 6: Countdown ===")
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Liftoff!")
```

### Exercise 7: Find First Negative
```python
print("=== Exercise 7: Find First Negative ===")
numbers = [5, 12, 3, -7, 9, -2, 4]

for num in numbers:
    if num < 0:
        print(f"First negative number: {num}")
        break
```

### Exercise 8: Skip Multiples of 3
```python
print("=== Exercise 8: Skip Multiples of 3 ===")
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()
```

### Exercise 9: List of Squares
```python
print("=== Exercise 9: List of Squares ===")
squares = []
for i in range(1, 11):
    squares.append(i ** 2)

print(f"Squares: {squares}")
```

### Exercise 10: Count Vowels
```python
print("=== Exercise 10: Count Vowels ===")
text = "Python automation is awesome"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"Text: '{text}'")
print(f"Vowels: {vowel_count}")
```

### Exercise 11: Even Numbers with Range
```python
print("=== Exercise 11: Even Numbers with Range ===")
for i in range(0, 21, 2):
    print(i, end=" ")
print()
```

### Exercise 12: Pattern Printing
```python
print("=== Exercise 12: Pattern Printing ===")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

### Exercise 13: Double Until Limit
```python
print("=== Exercise 13: Double Until Limit ===")
number = 1
while number <= 1000:
    print(number)
    number *= 2
```

### Exercise 14: Find Name
```python
print("=== Exercise 14: Find Name ===")
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
search_name = "Charlie"

for index, name in enumerate(names):
    if name == search_name:
        print(f"Found {search_name} at index {index}")
        break
else:
    print(f"{search_name} not found")
```

### Exercise 15: Validate Emails
```python
print("=== Exercise 15: Validate Emails ===")
emails = [
    "user@example.com",
    "invalid-email",
    "another@test.com",
    "bad@",
    "good@domain.org"
]

for email in emails:
    if "@" in email and "." in email:
        print(f"Valid: {email}")
    else:
        print(f"Invalid: {email}")
```

### BONUS: FizzBuzz
```python
print("=== BONUS: FizzBuzz ===")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

---

## Exercise 2: Loops Combined with Logic

### Exercise 1: Calculate Grades
```python
print("=== Exercise 1: Calculate Grades ===")
scores = [85, 92, 78, 95, 88, 76, 90, 82]

a_count = 0
b_count = 0
c_count = 0
below_c = 0

for score in scores:
    if score >= 90:
        a_count += 1
    elif score >= 80:
        b_count += 1
    elif score >= 70:
        c_count += 1
    else:
        below_c += 1

print(f"A grades: {a_count}")
print(f"B grades: {b_count}")
print(f"C grades: {c_count}")
print(f"Below C: {below_c}")
```

### Exercise 2: Find Long Words
```python
print("=== Exercise 2: Find Long Words ===")
words = ["cat", "elephant", "dog", "programming", "hi", "automation", "test", "python"]

long_words = []
for word in words:
    if len(word) > 5:
        long_words.append(word)

print(f"Original: {words}")
print(f"Long words: {long_words}")
```

### Exercise 3: Validate Usernames
```python
print("=== Exercise 3: Validate Usernames ===")
usernames = ["john_doe", "ab", "jane-smith", "validuser123", "x", "test_user_name"]

for username in usernames:
    if len(username) < 3:
        print(f"Invalid: {username} (too short)")
    elif len(username) > 15:
        print(f"Invalid: {username} (too long)")
    elif not username.replace("_", "").isalnum():
        print(f"Invalid: {username} (invalid characters)")
    else:
        print(f"Valid: {username}")
```

### Exercise 4: Calculate Total with Discount
```python
print("=== Exercise 4: Calculate Total with Discount ===")
items = [
    {"name": "Laptop", "price": 999.99, "quantity": 1},
    {"name": "Mouse", "price": 29.99, "quantity": 2},
    {"name": "Keyboard", "price": 79.99, "quantity": 1},
    {"name": "Monitor", "price": 299.99, "quantity": 2}
]

total = 0
for item in items:
    subtotal = item["price"] * item["quantity"]
    print(f"{item['name']}: ${subtotal:.2f}")
    total += subtotal

print(f"Total before discount: ${total:.2f}")

if total > 1000:
    discount = total * 0.10
    total -= discount
    print(f"Discount (10%): -${discount:.2f}")

print(f"Final total: ${total:.2f}")
```

### Exercise 5: Check Password Strength
```python
print("=== Exercise 5: Check Password Strength ===")
passwords = [
    "abc123",
    "StrongPass123!",
    "weakpass",
    "MyP@ssw0rd",
    "12345678"
]

for password in passwords:
    criteria_met = 0

    # Check length
    if len(password) >= 8:
        criteria_met += 1

    # Check for uppercase
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        criteria_met += 1

    # Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        criteria_met += 1

    if criteria_met == 3:
        strength = "Strong"
    elif criteria_met == 2:
        strength = "Medium"
    else:
        strength = "Weak"

    print(f"{password}: {strength}")
```

### Exercise 6: Clean Data
```python
print("=== Exercise 6: Clean Data ===")
data = ["  apple  ", "BANANA", "  Cherry ", "ORANGE  ", "grape"]

cleaned_data = []
for item in data:
    cleaned = item.strip().lower().capitalize()
    cleaned_data.append(cleaned)

print(f"Original: {data}")
print(f"Cleaned: {cleaned_data}")
```

### Exercise 7: Find Matching Products
```python
print("=== Exercise 7: Find Matching Products ===")
products = [
    {"name": "Laptop", "category": "Electronics", "price": 999.99, "in_stock": True},
    {"name": "Desk", "category": "Furniture", "price": 299.99, "in_stock": True},
    {"name": "Mouse", "category": "Electronics", "price": 29.99, "in_stock": False},
    {"name": "Chair", "category": "Furniture", "price": 199.99, "in_stock": True},
    {"name": "Keyboard", "category": "Electronics", "price": 79.99, "in_stock": True}
]

print("Electronics products in stock under $100:")
for product in products:
    if product["category"] == "Electronics" and product["in_stock"] and product["price"] < 100:
        print(f"  {product['name']}: ${product['price']}")
```

### Exercise 8: Count by Category
```python
print("=== Exercise 8: Count by Category ===")
items = [
    "apple", "banana", "carrot", "broccoli",
    "cherry", "spinach", "orange", "lettuce"
]

fruits = ["apple", "banana", "cherry", "orange"]
fruit_count = 0
vegetable_count = 0

for item in items:
    if item in fruits:
        fruit_count += 1
    else:
        vegetable_count += 1

print(f"Fruits: {fruit_count}")
print(f"Vegetables: {vegetable_count}")
```

### Exercise 9: Find Min and Max
```python
print("=== Exercise 9: Find Min and Max ===")
temperatures = [72, 68, 75, 70, 80, 65, 78, 73]

min_temp = temperatures[0]
max_temp = temperatures[0]
total_temp = 0

for temp in temperatures:
    if temp < min_temp:
        min_temp = temp
    if temp > max_temp:
        max_temp = temp
    total_temp += temp

print(f"Temperatures: {temperatures}")
print(f"Min: {min_temp}°F")
print(f"Max: {max_temp}°F")
print(f"Average: {total_temp / len(temperatures):.1f}°F")
```

### Exercise 10: Analyze Sentences
```python
print("=== Exercise 10: Analyze Sentences ===")
sentences = [
    "Python is great for automation",
    "Testing is important",
    "I love coding",
    "Playwright makes testing easy"
]

for sentence in sentences:
    word_count = len(sentence.split())
    is_test_related = "test" in sentence.lower()

    print(f"'{sentence}'")
    print(f"  Words: {word_count}")
    print(f"  Test-related: {is_test_related}")
```

### Exercise 11: Test Results Summary
```python
print("=== Exercise 11: Test Results Summary ===")
test_results = [
    {"name": "Login Test", "status": "pass", "duration": 2.5},
    {"name": "Checkout Test", "status": "fail", "duration": 5.2},
    {"name": "Search Test", "status": "pass", "duration": 1.8},
    {"name": "Profile Test", "status": "pass", "duration": 3.1},
    {"name": "Cart Test", "status": "fail", "duration": 4.0}
]

passed = 0
failed = 0
total_duration = 0

for test in test_results:
    if test["status"] == "pass":
        passed += 1
    else:
        failed += 1
    total_duration += test["duration"]

average_duration = total_duration / len(test_results)

print(f"Total tests: {len(test_results)}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Total duration: {total_duration:.1f}s")
print(f"Average duration: {average_duration:.1f}s")
```

### Exercise 12: Process User Orders
```python
print("=== Exercise 12: Process User Orders ===")
users = [
    {"name": "Alice", "orders": [50, 75, 100]},
    {"name": "Bob", "orders": [25, 30]},
    {"name": "Charlie", "orders": [200, 150, 100, 50]}
]

grand_total = 0

for user in users:
    user_total = 0
    for order in user["orders"]:
        user_total += order

    print(f"{user['name']}: ${user_total}")
    grand_total += user_total

print(f"Grand total: ${grand_total}")
```

### BONUS: Comprehensive Data Validation
```python
print("=== BONUS: Comprehensive Data Validation ===")
form_submissions = [
    {"name": "John Doe", "email": "john@example.com", "age": 25, "country": "USA"},
    {"name": "Jane", "email": "invalid-email", "age": 17, "country": ""},
    {"name": "Bob Smith", "email": "bob@test.com", "age": 30, "country": "UK"},
    {"name": "X", "email": "x@y.com", "age": 150, "country": "Canada"}
]

for i, submission in enumerate(form_submissions, 1):
    print(f"\nSubmission {i}:")
    errors = []

    if len(submission["name"]) < 3:
        errors.append("Name too short")

    if "@" not in submission["email"] or "." not in submission["email"]:
        errors.append("Invalid email")

    if submission["age"] < 18 or submission["age"] > 120:
        errors.append("Age out of range")

    if submission["country"] == "":
        errors.append("Country required")

    if len(errors) == 0:
        print("  ✓ Valid")
    else:
        print("  ✗ Invalid:")
        for error in errors:
            print(f"    - {error}")
```

---

## Exercise 3: Playwright Automation Scenarios

### Exercise 1: Navigate Through Menu
```python
print("=== Exercise 1: Navigate Through Menu ===")
menu_items = ["Home", "Products", "Services", "About", "Contact"]

for item in menu_items:
    print(f"Clicking: {item}")
```

### Exercise 2: Complete Registration Form
```python
print("=== Exercise 2: Complete Registration Form ===")
form_data = {
    "First Name": "John",
    "Last Name": "Doe",
    "Email": "john.doe@example.com",
    "Phone": "555-1234",
    "Address": "123 Main St"
}

for field, value in form_data.items():
    print(f"Filling {field}: {value}")

print("Form submitted")
```

### Exercise 3: Check Page Elements
```python
print("=== Exercise 3: Check Page Elements ===")
expected_elements = [
    {"type": "heading", "text": "Welcome"},
    {"type": "button", "text": "Sign In"},
    {"type": "button", "text": "Register"},
    {"type": "link", "text": "Forgot Password"}
]

found_elements = ["Welcome", "Sign In", "Register"]

for element in expected_elements:
    element_text = element["text"]
    if element_text in found_elements:
        print(f"✓ Found {element['type']}: {element_text}")
    else:
        print(f"✗ Missing {element['type']}: {element_text}")
```

### Exercise 4: Extract Product Information
```python
print("=== Exercise 4: Extract Product Information ===")
products_table = [
    {"id": 1, "name": "Laptop", "price": 999, "stock": 5},
    {"id": 2, "name": "Mouse", "price": 29, "stock": 50},
    {"id": 3, "name": "Keyboard", "price": 79, "stock": 0},
    {"id": 4, "name": "Monitor", "price": 299, "stock": 10}
]

print("Out of stock products:")
for product in products_table:
    if product["stock"] == 0:
        print(f"  {product['name']}")

available_count = 0
for product in products_table:
    if product["stock"] > 0:
        available_count += 1

print(f"\nAvailable products: {available_count}")

max_price = 0
most_expensive = None
for product in products_table:
    if product["price"] > max_price:
        max_price = product["price"]
        most_expensive = product["name"]

print(f"Most expensive: {most_expensive} (${max_price})")
```

### Exercise 5: Configure Preferences
```python
print("=== Exercise 5: Configure Preferences ===")
preferences = [
    {"id": "news", "label": "Email Newsletter", "default": True},
    {"id": "promo", "label": "Promotional Offers", "default": False},
    {"id": "update", "label": "Product Updates", "default": True},
    {"id": "survey", "label": "Surveys", "default": False}
]

for pref in preferences:
    if pref["default"]:
        print(f"☑ Selecting: {pref['label']}")
    else:
        print(f"☐ Skipping: {pref['label']}")
```

### Exercise 6: Find and Click Search Result
```python
print("=== Exercise 6: Find and Click Search Result ===")
search_results = [
    "Python Tutorial for Beginners",
    "JavaScript Basics Guide",
    "Playwright Automation Testing",
    "Selenium WebDriver Tips",
    "Python Automation Tools"
]

target_keyword = "Playwright"

found = False
for result in search_results:
    if target_keyword in result:
        print(f"Clicking on: {result}")
        found = True
        break

if not found:
    print(f"No results found for: {target_keyword}")
```

### Exercise 7: Run Multiple Login Tests
```python
print("=== Exercise 7: Run Multiple Login Tests ===")
test_cases = [
    {"username": "valid@user.com", "password": "Pass123!", "should_succeed": True},
    {"username": "invalid@user.com", "password": "wrong", "should_succeed": False},
    {"username": "admin@site.com", "password": "Admin123!", "should_succeed": True}
]

for i, test in enumerate(test_cases, 1):
    print(f"\nTest {i}:")
    print(f"  Username: {test['username']}")
    print(f"  Password: {'*' * len(test['password'])}")

    # Simulate login
    actual_result = test["should_succeed"]  # In real test, this would be actual result

    if actual_result == test["should_succeed"]:
        print("  ✓ Test passed")
    else:
        print("  ✗ Test failed")
```

### Exercise 8: Crawl Website Pages
```python
print("=== Exercise 8: Crawl Website Pages ===")
pages = [
    {"url": "/home", "title": "Home Page"},
    {"url": "/products", "title": "Products"},
    {"url": "/about", "title": "About Us"},
    {"url": "/contact", "title": "Contact"}
]

for page in pages:
    print(f"Navigating to: {page['url']}")
    print(f"Verifying title: {page['title']}")
    print("✓ Page verified")
    print()
```

### Exercise 9: Retry Click with Timeout
```python
print("=== Exercise 9: Retry Click with Timeout ===")
element_name = "Submit Button"
max_retries = 5
attempts_until_success = 3

success = False
for attempt in range(1, max_retries + 1):
    print(f"Attempt {attempt}...")

    if attempt >= attempts_until_success:
        print(f"✓ Successfully clicked {element_name}")
        success = True
        break
    else:
        print("Element not ready, retrying...")

if not success:
    print(f"✗ Failed to click after {max_retries} attempts")
```

### Exercise 10: Wait for Loading Spinner
```python
print("=== Exercise 10: Wait for Loading Spinner ===")
spinner_disappears_at = 4
max_wait_seconds = 10

for second in range(1, max_wait_seconds + 1):
    print(f"Waiting... {second}s")

    if second >= spinner_disappears_at:
        print("✓ Spinner disappeared")
        break
else:
    print("⚠ Timeout: Spinner still visible")
```

### Exercise 11: Collect Data from Pagination
```python
print("=== Exercise 11: Collect Data from Pagination ===")
pages_data = [
    ["Product A", "Product B", "Product C"],
    ["Product D", "Product E", "Product F"],
    ["Product G", "Product H"]
]

all_products = []

for page_num, products in enumerate(pages_data, 1):
    print(f"Page {page_num}: Found {len(products)} products")
    all_products.extend(products)

print(f"Total products collected: {len(all_products)}")
print(f"Products: {all_products}")
```

### Exercise 12: Check All Links on Page
```python
print("=== Exercise 12: Check All Links on Page ===")
links = [
    {"text": "Home", "href": "/home", "should_exist": True},
    {"text": "Blog", "href": "/blog", "should_exist": True},
    {"text": "Admin", "href": "/admin", "should_exist": False},
    {"text": "Help", "href": "/help", "should_exist": True}
]

issues = 0

for link in links:
    if link["should_exist"]:
        print(f"✓ Link '{link['text']}' exists")
    else:
        print(f"⚠ Link '{link['text']}' should not be visible!")
        issues += 1

print(f"\nValidation issues: {issues}")
```

### Exercise 13: Register Multiple Users
```python
print("=== Exercise 13: Register Multiple Users ===")
users_to_register = [
    {"name": "Alice Johnson", "email": "alice@example.com", "role": "user"},
    {"name": "Bob Smith", "email": "bob@example.com", "role": "admin"},
    {"name": "Charlie Brown", "email": "charlie@example.com", "role": "user"}
]

for i, user in enumerate(users_to_register, 1):
    print(f"\nRegistering user {i}/{len(users_to_register)}")
    print(f"  Name: {user['name']}")
    print(f"  Email: {user['email']}")
    print(f"  Role: {user['role']}")
    print("  Filling form and submitting...")
    print("  ✓ User registered successfully")
```

### Exercise 14: Click Only Enabled Buttons
```python
print("=== Exercise 14: Click Only Enabled Buttons ===")
buttons = [
    {"id": "save", "text": "Save", "enabled": True},
    {"id": "delete", "text": "Delete", "enabled": False},
    {"id": "edit", "text": "Edit", "enabled": True},
    {"id": "cancel", "text": "Cancel", "enabled": True},
    {"id": "submit", "text": "Submit", "enabled": False}
]

clicked_count = 0

for button in buttons:
    if not button["enabled"]:
        print(f"Skipping disabled: {button['text']}")
        continue

    print(f"Clicking: {button['text']}")
    clicked_count += 1

print(f"\nClicked {clicked_count} buttons")
```

### Exercise 15: Check Form Validation
```python
print("=== Exercise 15: Check Form Validation ===")
validation_errors = [
    {"field": "email", "message": "Invalid email format"},
    {"field": "password", "message": "Password too short"},
    {"field": "age", "message": "Must be 18 or older"}
]

expected_errors = ["email", "password", "age", "phone"]

print("Errors found:")
error_fields = []
for error in validation_errors:
    print(f"  {error['field']}: {error['message']}")
    error_fields.append(error["field"])

print("\nMissing expected errors:")
for expected in expected_errors:
    if expected not in error_fields:
        print(f"  {expected}")
```

### BONUS: End-to-End Shopping Test
```python
print("=== BONUS: End-to-End Shopping Test ===")
products_to_add = [
    {"name": "Laptop", "quantity": 1, "price": 999},
    {"name": "Mouse", "quantity": 2, "price": 29},
    {"name": "Keyboard", "quantity": 1, "price": 79}
]

shipping_info = {
    "name": "John Doe",
    "address": "123 Main St",
    "city": "New York",
    "zip": "10001"
}

# Step 1: Add products to cart
print("Adding products to cart:")
total = 0
for product in products_to_add:
    print(f"  Adding {product['quantity']}x {product['name']} to cart")
    total += product['quantity'] * product['price']

# Step 2: Show cart total
print(f"\nCart total: ${total}")

# Step 3: Fill shipping form
print("\nFilling shipping information:")
for field, value in shipping_info.items():
    print(f"  Filling {field}: {value}")

# Step 4: Complete order
print("\n✓ Order completed successfully")
print(f"Order total: ${total}")
```

---

## Key Takeaways

### For Loops
- Use when you know what you're iterating over (list, string, range)
- Perfect for processing collections of items
- Cleaner and more Pythonic for most iteration needs

### While Loops
- Use when you don't know how many iterations needed
- Great for waiting, retrying, and condition-based iteration
- Always ensure the condition will eventually become false

### range() Function
- `range(stop)` - 0 to stop-1
- `range(start, stop)` - start to stop-1
- `range(start, stop, step)` - with custom increment

### Break and Continue
- `break` - exit loop immediately (useful for finding items)
- `continue` - skip to next iteration (useful for filtering)
- Both make code more efficient by avoiding unnecessary processing

### Automation Patterns
- Iterate through elements on web pages
- Fill multiple form fields
- Process tables and lists of data
- Data-driven testing with multiple test cases
- Retry logic for reliability
- Batch operations for efficiency

---

**Great job completing all exercises! You're now ready to use loops effectively in your automation code!**
