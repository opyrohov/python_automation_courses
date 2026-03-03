"""
Lecture 3: Break, Continue, and range()
This file demonstrates loop control statements and the range() function in detail.
"""

# ============================================
# RANGE() FUNCTION - SINGLE PARAMETER
# ============================================
print("=== range() with One Parameter ===")

# range(stop) - generates 0 to stop-1
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print("\n")

# Converting range to list to see all values
print(f"list(range(5)): {list(range(5))}")
print(f"list(range(10)): {list(range(10))}")

print()

# ============================================
# RANGE() FUNCTION - TWO PARAMETERS
# ============================================
print("=== range() with Two Parameters ===")

# range(start, stop) - generates start to stop-1
print("range(2, 8):", end=" ")
for i in range(2, 8):
    print(i, end=" ")
print("\n")

print(f"list(range(1, 6)): {list(range(1, 6))}")
print(f"list(range(5, 11)): {list(range(5, 11))}")

print()

# ============================================
# RANGE() FUNCTION - THREE PARAMETERS
# ============================================
print("=== range() with Three Parameters (Step) ===")

# range(start, stop, step) - generates with custom increment
print("Even numbers (0 to 10):", end=" ")
for i in range(0, 11, 2):
    print(i, end=" ")
print("\n")

print("Odd numbers (1 to 10):", end=" ")
for i in range(1, 11, 2):
    print(i, end=" ")
print("\n")

print("Count by 5s:", end=" ")
for i in range(0, 51, 5):
    print(i, end=" ")
print("\n")

print()

# ============================================
# RANGE() - COUNTING BACKWARDS
# ============================================
print("=== Counting Backwards with range() ===")

print("Countdown from 10:", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print("Blast off!\n")

print("Count down by 2s:", end=" ")
for i in range(20, 0, -2):
    print(i, end=" ")
print("\n")

print(f"list(range(5, 0, -1)): {list(range(5, 0, -1))}")

print()

# ============================================
# BREAK STATEMENT - EXIT LOOP EARLY
# ============================================
print("=== Break Statement ===")

# Example 1: Stop when condition met
print("Finding first even number:")
numbers = [1, 3, 5, 8, 9, 11]

for num in numbers:
    print(f"  Checking {num}...")
    if num % 2 == 0:
        print(f"  Found first even number: {num}")
        break
else:
    # This executes only if loop completes without break
    print("  No even numbers found")

print()

# Example 2: Search and exit
print("Searching for target:")
items = ["apple", "banana", "cherry", "date"]
target = "cherry"

for index, item in enumerate(items):
    print(f"  Checking index {index}: {item}")
    if item == target:
        print(f"  Found '{target}' at index {index}!")
        break

print()

# ============================================
# CONTINUE STATEMENT - SKIP ITERATION
# ============================================
print("=== Continue Statement ===")

# Example 1: Skip even numbers
print("Print only odd numbers:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
print("\n")

# Example 2: Skip specific values
print("Skip multiples of 3:")
for num in range(1, 16):
    if num % 3 == 0:
        continue  # Skip multiples of 3
    print(num, end=" ")
print("\n")

print()

# ============================================
# BREAK IN WHILE LOOP
# ============================================
print("=== Break in While Loop ===")

count = 1

while True:  # Infinite loop
    print(f"Count: {count}")
    if count >= 5:
        print("Reached limit, breaking!")
        break
    count += 1

print()

# ============================================
# CONTINUE IN WHILE LOOP
# ============================================
print("=== Continue in While Loop ===")

num = 0

while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip printing even numbers
    print(f"Odd number: {num}")

print()

# ============================================
# BREAK AND CONTINUE TOGETHER
# ============================================
print("=== Break and Continue Together ===")

print("Process numbers, skip negatives, stop at zero:")
numbers = [5, 3, -2, 7, -4, 0, 9]

for num in numbers:
    if num == 0:
        print("  Encountered zero, stopping!")
        break
    if num < 0:
        print(f"  Skipping negative: {num}")
        continue
    print(f"  Processing: {num}")

print()

# ============================================
# NESTED LOOPS WITH BREAK
# ============================================
print("=== Break in Nested Loops ===")

# Break only exits the inner loop
found = False
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            print(f"  Found condition at i={i}, j={j}")
            found = True
            break  # Only breaks inner loop
        print(f"  i={i}, j={j}")
    if found:
        break  # Break outer loop too

print()

# ============================================
# PRACTICAL EXAMPLE: SEARCH WITH BREAK
# ============================================
print("=== Practical Example: Finding User ===")

users = [
    {"name": "Alice", "id": 101},
    {"name": "Bob", "id": 102},
    {"name": "Charlie", "id": 103},
    {"name": "Diana", "id": 104}
]

search_id = 103

for user in users:
    if user["id"] == search_id:
        print(f"Found user: {user['name']} (ID: {user['id']})")
        break
else:
    print(f"User with ID {search_id} not found")

print()

# ============================================
# PRACTICAL EXAMPLE: SKIP INVALID DATA
# ============================================
print("=== Practical Example: Validating Data ===")

scores = [85, 92, -5, 78, 150, 88, 95]

print("Valid scores (0-100):")
for score in scores:
    if score < 0 or score > 100:
        print(f"  Skipping invalid score: {score}")
        continue
    print(f"  Valid score: {score}")

print()

# ============================================
# PRACTICAL EXAMPLE: FIRST N PRIMES
# ============================================
print("=== Practical Example: Finding First 5 Primes ===")

count = 0
num = 2

while count < 5:
    is_prime = True

    # Check if num is prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # Not prime, no need to check further

    if is_prime:
        print(f"Prime {count + 1}: {num}")
        count += 1

    num += 1

print()

# ============================================
# PRACTICAL EXAMPLE: PASSWORD VALIDATION
# ============================================
print("=== Practical Example: Password Requirements ===")

passwords = ["abc", "Pass123", "password", "MyP@ss123", "12345"]

for password in passwords:
    print(f"\nChecking: '{password}'")

    # Skip if too short
    if len(password) < 8:
        print("  ✗ Too short (minimum 8 characters)")
        continue

    # Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if not has_digit:
        print("  ✗ Must contain at least one digit")
        continue

    # Check for uppercase
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if not has_upper:
        print("  ✗ Must contain at least one uppercase letter")
        continue

    print("  ✓ Password is valid!")

print()

# ============================================
# PRACTICAL EXAMPLE: PROCESSING UNTIL SUCCESS
# ============================================
print("=== Practical Example: Retry Until Success ===")

attempts = [False, False, True, False]  # Simulating success on 3rd attempt
max_attempts = 5

for attempt_num in range(1, max_attempts + 1):
    print(f"Attempt {attempt_num}...")

    # Simulate operation
    if attempt_num <= len(attempts):
        success = attempts[attempt_num - 1]
    else:
        success = False

    if success:
        print("  ✓ Operation succeeded!")
        break
    else:
        print("  ✗ Operation failed, retrying...")
else:
    # This runs if loop completes without break
    print("✗ Failed after all attempts")

print()

# ============================================
# PRACTICAL EXAMPLE: FILTERING WITH CONTINUE
# ============================================
print("=== Practical Example: Processing Orders ===")

orders = [
    {"id": 1, "status": "pending", "amount": 100},
    {"id": 2, "status": "cancelled", "amount": 50},
    {"id": 3, "status": "pending", "amount": 200},
    {"id": 4, "status": "completed", "amount": 150},
    {"id": 5, "status": "pending", "amount": 75}
]

print("Processing pending orders:")
total = 0

for order in orders:
    if order["status"] != "pending":
        continue  # Skip non-pending orders

    print(f"  Order #{order['id']}: ${order['amount']}")
    total += order["amount"]

print(f"Total pending: ${total}")

print()

# ============================================
# ELSE CLAUSE WITH LOOPS
# ============================================
print("=== Else Clause with Loops ===")

# Else executes if loop completes without break
print("Example 1: Loop completes (else runs):")
for i in range(3):
    print(f"  {i}")
else:
    print("  Loop completed normally")

print("\nExample 2: Loop breaks (else doesn't run):")
for i in range(3):
    print(f"  {i}")
    if i == 1:
        print("  Breaking!")
        break
else:
    print("  This won't print because loop was broken")

print()

# ============================================
# SUMMARY
# ============================================
print("=== Summary ===")
print("\nrange() function:")
print("  • range(5) → 0, 1, 2, 3, 4")
print("  • range(2, 7) → 2, 3, 4, 5, 6")
print("  • range(0, 10, 2) → 0, 2, 4, 6, 8")
print("  • range(10, 0, -1) → 10, 9, 8, ..., 1")

print("\nbreak statement:")
print("  • Exits the loop immediately")
print("  • Used to stop searching once found")
print("  • Prevents else clause from running")

print("\ncontinue statement:")
print("  • Skips rest of current iteration")
print("  • Moves to next iteration immediately")
print("  • Used to skip invalid/unwanted items")
