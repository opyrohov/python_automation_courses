# Solutions for Lecture 2 Exercises

## Exercise 1: String Practice

### Exercise 1: Email Validation
```python
email = "user@example.com"

if "@" in email and "." in email:
    print("Valid email format")
else:
    print("Invalid email format")

domain = email.split("@")[1]
print(f"Domain: {domain}")
```

### Exercise 2: Name Formatting
```python
first_name = "John"
last_name = "Doe"

full_name = f"{first_name} {last_name}"

print(full_name)  # "John Doe"
print(f"{last_name.upper()}, {first_name}")  # "DOE, John"
print(f"{first_name.lower()}.{last_name.lower()}")  # "john.doe"
```

### Exercise 3: URL Manipulation
```python
url = "https://www.example.com/products/item-12345"

domain = url.replace("https://", "").replace("http://", "").split("/")[0]
print(f"Domain: {domain}")

product_id = url.split("-")[-1]
print(f"Product ID: {product_id}")

new_url = url.replace("products", "items")
print(f"New URL: {new_url}")
```

### Exercise 4: Text Cleaning
```python
messy_text = "   Welcome to Python Programming!   "

clean_text = messy_text.strip()
print(f"Clean: '{clean_text}'")

lowercase_text = clean_text.lower()
print(f"Lowercase: {lowercase_text}")

o_count = lowercase_text.count('o')
print(f"Letter 'o' appears {o_count} times")

replaced_text = clean_text.replace("Python", "JavaScript")
print(f"Replaced: {replaced_text}")
```

### Exercise 5: Password Strength Checker
```python
password = "MyPassword123"

print(f"Password length: {len(password)}")

has_numbers = any(char.isdigit() for char in password)
print(f"Contains numbers: {has_numbers}")

has_uppercase = any(char.isupper() for char in password)
print(f"Contains uppercase: {has_uppercase}")

has_lowercase = any(char.islower() for char in password)
print(f"Contains lowercase: {has_lowercase}")

if len(password) >= 8 and has_numbers and has_uppercase and has_lowercase:
    print("✓ Strong password")
else:
    print("✗ Weak password")
```

### Exercise 6: Log Message Parser
```python
log_message = "[ERROR] 2024-01-15 10:30:45 - Database connection failed"

log_level = log_message.split("]")[0].replace("[", "")
print(f"Log level: {log_level}")

timestamp = log_message.split(" - ")[0].split("] ")[1]
print(f"Timestamp: {timestamp}")

message = log_message.split(" - ")[1]
print(f"Message: {message}")

if "[ERROR]" in log_message:
    print("This is an error message")
```

### Exercise 7: CSV Data Processing
```python
csv_line = "John,Doe,30,Engineer,New York"

fields = csv_line.split(",")
print(f"Fields: {fields}")

first_name = fields[0]
last_name = fields[1]
age = fields[2]
job = fields[3]
city = fields[4]

print(f"{first_name} {last_name}, {age}, works as an {job} in {city}")
```

### Exercise 8: Page Title Verification
```python
page_title = "Shopping Cart - MyStore"
expected_keywords = ["Shopping", "Cart"]

for keyword in expected_keywords:
    if keyword in page_title:
        print(f"✓ Found: {keyword}")
    else:
        print(f"✗ Missing: {keyword}")
```

### BONUS: Username Generator
```python
full_name = "John Michael Doe"
birth_year = 1995

names = full_name.split()
first_initial = names[0][0]
last_name = names[-1]
year_suffix = str(birth_year)[-2:]

username = f"{first_initial}{last_name}{year_suffix}".lower()
print(f"Username: {username}")  # jdoe95
```

---

## Exercise 2: Conditional Logic

### Exercise 1: Age Classifier
```python
age = 25

if age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
```

### Exercise 2: Grade Calculator
```python
score = 87

if score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Good job!")
elif score >= 70:
    print("Grade: C - Satisfactory")
elif score >= 60:
    print("Grade: D - Needs improvement")
else:
    print("Grade: F - Failed")
```

### Exercise 3: Login Validator
```python
username = "admin"
password = "secret123"
is_account_active = True

if username == "admin" and password == "secret123" and is_account_active:
    print("✓ Login successful!")
else:
    if username != "admin":
        print("✗ Invalid username")
    if password != "secret123":
        print("✗ Invalid password")
    if not is_account_active:
        print("✗ Account is not active")
```

### Exercise 4: Shopping Discount Calculator
```python
total_amount = 150
is_member = True
has_coupon = False

discount_rate = 0

if total_amount > 200:
    discount_rate = 0.25
elif is_member and total_amount > 100:
    discount_rate = 0.20
elif has_coupon:
    discount_rate = 0.15
elif is_member:
    discount_rate = 0.10

discount = total_amount * discount_rate
final_price = total_amount - discount

print(f"Original: ${total_amount}")
print(f"Discount: {discount_rate * 100}% (${discount})")
print(f"Final price: ${final_price}")
```

### Exercise 5: Temperature Adviser
```python
temperature = 22
is_raining = False

if temperature < 0:
    advice = "Wear a heavy coat"
elif temperature <= 15:
    advice = "Wear a jacket"
elif temperature <= 25:
    advice = "Wear a light sweater"
else:
    advice = "T-shirt weather"

if is_raining:
    advice += " and take an umbrella"

print(advice)
```

### Exercise 6: Password Strength Validator
```python
password = "MyPass123"

has_numbers = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)

if len(password) < 8:
    print("Weak password - too short")
    print("Suggestion: Use at least 8 characters")
elif len(password) >= 8 and has_numbers and has_uppercase and has_lowercase:
    print("Strong password")
elif len(password) >= 8 and (has_numbers or has_uppercase):
    print("Medium password")
    if not has_numbers:
        print("Suggestion: Add numbers")
    if not has_uppercase:
        print("Suggestion: Add uppercase letters")
    if not has_lowercase:
        print("Suggestion: Add lowercase letters")
else:
    print("Weak password")
```

### Exercise 7: Traffic Light System
```python
light_color = "green"
pedestrian_crossing = False

if light_color == "red":
    print("Stop")
elif light_color == "yellow":
    print("Slow down")
elif light_color == "green":
    if pedestrian_crossing:
        print("Slow down - pedestrians crossing")
    else:
        print("Go")
```

### Exercise 8: Number Analyzer
```python
number = 15

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if number % 5 == 0:
    print("Divisible by 5")
```

### Exercise 9: Movie Ticket Pricing
```python
age = 25
is_student = False
is_senior = False
show_time = "matinee"

base_price = 15
final_price = base_price

if show_time == "matinee":
    final_price -= 3

if age < 13:
    final_price -= 5

if is_student:
    final_price -= 4

if is_senior or age >= 65:
    final_price -= 6

print(f"Ticket price: ${final_price}")
```

### Exercise 10: File Upload Validator
```python
filename = "document.pdf"
file_size = 4.5
allowed_extensions = [".pdf", ".doc", ".docx"]
max_size = 5.0

is_valid = True

# Check extension
file_extension = ""
for ext in allowed_extensions:
    if filename.endswith(ext):
        file_extension = ext
        break

if file_extension:
    print(f"✓ File extension {file_extension} is allowed")
else:
    print("✗ File extension not allowed")
    is_valid = False

# Check size
if file_size <= max_size:
    print(f"✓ File size ({file_size}MB) is within limit")
else:
    print(f"✗ File size ({file_size}MB) exceeds limit ({max_size}MB)")
    is_valid = False

if is_valid:
    print("✓ File upload is valid")
else:
    print("✗ File upload is invalid")
```

### BONUS: ATM Withdrawal System
```python
account_balance = 1000
withdrawal_amount = 250
daily_limit = 500
withdrawals_today = 300
pin_correct = True

if not pin_correct:
    print("✗ Incorrect PIN")
elif withdrawal_amount > account_balance:
    print("✗ Insufficient balance")
elif (withdrawals_today + withdrawal_amount) > daily_limit:
    remaining_limit = daily_limit - withdrawals_today
    print(f"✗ Daily limit exceeded. You can withdraw up to ${remaining_limit} more today")
else:
    new_balance = account_balance - withdrawal_amount
    new_daily_total = withdrawals_today + withdrawal_amount
    print(f"✓ Withdrawal successful")
    print(f"Amount withdrawn: ${withdrawal_amount}")
    print(f"New balance: ${new_balance}")
    print(f"Daily withdrawals: ${new_daily_total}/{daily_limit}")
```

---

## Exercise 3: Playwright Scenarios

### Exercise 1: Login Flow Validation
```python
current_url = "https://example.com/dashboard"
page_title = "Dashboard - Welcome"
username_displayed = "John Doe"

print("Validating login...")

if "dashboard" in current_url:
    print("✓ URL is correct")
else:
    print("✗ URL is incorrect")

if "Dashboard" in page_title:
    print("✓ Page title is correct")
else:
    print("✗ Page title is incorrect")

if username_displayed:
    print(f"✓ Username '{username_displayed}' is displayed")
else:
    print("✗ Username not displayed")
```

### Exercise 2: Error Message Handler
```python
error_message = "Error: Invalid email format"

if "email" in error_message.lower():
    print("Fix email format and retry")
elif "password" in error_message.lower():
    print("Enter a valid password")
elif "account" in error_message.lower():
    print("Check username or register")
elif "network" in error_message.lower():
    print("Check internet connection")
else:
    print("Unknown error - contact support")
```

### Exercise 3: Search Results Validation
```python
search_term = "Python Automation"
result_count = 25
first_result_title = "Learn Python Automation Testing"
first_result_url = "https://example.com/python-automation"

if result_count > 0:
    print(f"✓ Found {result_count} results")
else:
    print("✗ No results found")

search_words = search_term.lower().split()
title_match = all(word in first_result_title.lower() for word in search_words)

if title_match:
    print("✓ Search terms found in first result title")
else:
    print("✗ Search terms not found in first result title")

url_search_term = search_term.lower().replace(" ", "-")
if url_search_term in first_result_url:
    print("✓ Search terms found in URL")
else:
    print("✗ Search terms not found in URL")
```

### Exercise 4: Form Field Validator
```python
email = "user@example.com"
phone = "123-456-7890"
age = "25"
website = "https://example.com"

# Email validation
if "@" in email and "." in email:
    print("✓ Email is valid")
else:
    print("✗ Email is invalid")

# Phone validation
if len(phone) == 12:
    print("✓ Phone is valid")
else:
    print("✗ Phone is invalid")

# Age validation
if age.isdigit() and int(age) >= 18:
    print("✓ Age is valid")
else:
    print("✗ Age is invalid")

# Website validation
if website.startswith("http://") or website.startswith("https://"):
    print("✓ Website is valid")
else:
    print("✗ Website is invalid")
```

### Exercise 5: Navigation Validator
```python
current_page = "home"
expected_pages = ["home", "products", "cart", "checkout", "confirmation"]

if current_page in expected_pages:
    print(f"✓ Current page '{current_page}' is valid")
    current_index = expected_pages.index(current_page)
    if current_index < len(expected_pages) - 1:
        next_page = expected_pages[current_index + 1]
        print(f"Next page should be: {next_page}")
    else:
        print("You are on the final page")
else:
    print(f"✗ Current page '{current_page}' is not valid")
```

### Exercise 6: Element State Checker
```python
button_visible = True
button_enabled = False
button_text = "Submit Order"
form_valid = False

if button_visible and button_enabled and form_valid:
    print(f"✓ Ready to click '{button_text}'")
else:
    print("✗ Cannot proceed because:")
    if not button_visible:
        print("  - Button is not visible")
    if not button_enabled:
        print("  - Button is not enabled")
    if not form_valid:
        print("  - Form is not valid")
```

### Exercise 7: Price Comparison
```python
original_price_text = "$99.99"
sale_price_text = "$79.99"

original_price = float(original_price_text.replace("$", ""))
sale_price = float(sale_price_text.replace("$", ""))

discount_amount = original_price - sale_price
discount_percentage = (discount_amount / original_price) * 100

print(f"Original: ${original_price}")
print(f"Sale: ${sale_price}")
print(f"Discount: ${discount_amount:.2f} ({discount_percentage:.1f}%)")

if discount_percentage > 15:
    print("✓ Good deal!")
else:
    print("⚠ Not a significant discount")
```

### Exercise 8: Shopping Cart Validator
```python
cart_items = 3
expected_items = 3
cart_total_text = "Total: $145.97"
expected_total = 145.97

if cart_items == expected_items:
    print(f"✓ Cart item count is correct: {cart_items}")
else:
    print(f"✗ Item count mismatch: expected {expected_items}, got {cart_items}")

cart_total = float(cart_total_text.replace("Total: $", ""))

if cart_total == expected_total:
    print(f"✓ Cart total is correct: ${cart_total}")
else:
    print(f"✗ Total mismatch: expected ${expected_total}, got ${cart_total}")
```

### Exercise 9: Page Load Status
```python
page_loaded = True
required_element_visible = False
page_title = "Loading..."
wait_time = 3
max_wait = 5

if not page_loaded:
    print("Still loading...")
elif page_loaded and not required_element_visible:
    if wait_time < max_wait:
        print("Waiting for element...")
    else:
        print("Timeout error")
elif page_loaded and required_element_visible:
    print("Page ready")
```

### Exercise 10: Test Result Reporter
```python
test_name = "User Login Test"
expected_result = "Login successful"
actual_result = "Login successful"
execution_time = 2.5

print("=" * 50)
print(f"Test: {test_name}")
print("-" * 50)

if expected_result == actual_result:
    print("Status: PASS ✓")
else:
    print("Status: FAIL ✗")
    print(f"Expected: {expected_result}")
    print(f"Actual: {actual_result}")

print(f"Execution time: {execution_time}s")

if execution_time > 3:
    print("⚠ Performance warning: Test took longer than expected")

print("=" * 50)
```

### BONUS: Multi-Step Form Wizard
```python
current_step = 2
total_steps = 4
step_titles = ["Personal Info", "Address", "Payment", "Confirmation"]
completed_steps = [1]
current_step_valid = True

print(f"Step {current_step} of {total_steps}: {step_titles[current_step - 1]}")

previous_step = current_step - 1
if previous_step in completed_steps:
    print("✓ Previous steps completed")
else:
    print("✗ Previous steps not completed")

if current_step_valid:
    if current_step < total_steps:
        next_step = step_titles[current_step]
        print(f"→ Proceed to {next_step}")
    else:
        print("→ Ready to submit")
else:
    print("→ Complete current step")

progress = (current_step / total_steps) * 100
print(f"Progress: {progress}%")
```

---

## Tips for Success

1. **String Manipulation**:
   - Use `.split()` and `.join()` for breaking apart and combining strings
   - Remember that strings are case-sensitive - use `.lower()` or `.upper()` for comparisons
   - Use `in` operator to check if substring exists

2. **Control Flow**:
   - Always check the most specific conditions first
   - Use `and`, `or`, `not` to combine conditions
   - Consider using `elif` instead of multiple `if` statements when conditions are mutually exclusive

3. **Automation Context**:
   - In real Playwright code, you'll use these patterns constantly
   - String manipulation helps with text verification and data extraction
   - Conditional logic makes your tests dynamic and robust

Keep practicing these concepts - they're fundamental to automation testing!
