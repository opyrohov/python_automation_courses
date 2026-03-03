"""
Lecture 3: While Loops
This file demonstrates how to use while loops for condition-based iteration in Python.
"""

# ============================================
# BASIC WHILE LOOP
# ============================================
print("=== Basic While Loop ===")

count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1

print()

# ============================================
# COUNTDOWN WITH WHILE LOOP
# ============================================
print("=== Countdown ===")

countdown = 10

while countdown > 0:
    print(countdown, end=" ")
    countdown -= 1

print("Blast off!")
print()

# ============================================
# WHILE LOOP WITH USER INPUT (SIMULATED)
# ============================================
print("=== While Loop with Validation ===")

# Simulating user input validation
password = "wrong"
attempts = 0
max_attempts = 3

while password != "secret" and attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts}: Password is '{password}'")

    if password == "secret":
        print("Access granted!")
    else:
        print("Access denied!")
        # In real scenario, we'd ask for input here
        # For demo, we'll change it on last attempt
        if attempts == max_attempts - 1:
            password = "secret"
        else:
            password = "wrong"

if password == "secret":
    print("Successfully logged in!")
else:
    print("Maximum attempts reached. Account locked.")

print()

# ============================================
# INFINITE LOOP PREVENTION
# ============================================
print("=== Avoiding Infinite Loops ===")

# WRONG: This would loop forever (don't run this!)
# x = 1
# while x <= 5:
#     print(x)
#     # Missing: x += 1  (This would cause infinite loop!)

# CORRECT: Always ensure condition will eventually be false
x = 1
while x <= 5:
    print(f"x = {x}")
    x += 1  # This ensures the loop will end

print()

# ============================================
# WHILE LOOP WITH ACCUMULATOR
# ============================================
print("=== While Loop with Accumulator ===")

# Sum numbers from 1 to 10
num = 1
total = 0

while num <= 10:
    total += num
    num += 1

print(f"Sum of 1 to 10: {total}")

print()

# ============================================
# WHILE TRUE WITH BREAK
# ============================================
print("=== While True with Break ===")

# Useful pattern for menus or repeated actions
counter = 0

while True:
    counter += 1
    print(f"Iteration {counter}")

    if counter >= 5:
        print("Reached limit, breaking out!")
        break

print()

# ============================================
# WHILE LOOP VS FOR LOOP
# ============================================
print("=== When to Use While vs For ===")

# FOR LOOP: When you know how many iterations
print("For loop (known iterations):")
for i in range(5):
    print(f"  Step {i + 1}")

print()

# WHILE LOOP: When you don't know how many iterations
print("While loop (unknown iterations):")
import random
random.seed(42)  # For consistent demo

attempts = 0
target = 7
guess = 0

while guess != target:
    attempts += 1
    guess = random.randint(1, 10)
    print(f"  Attempt {attempts}: Guessed {guess}")

print(f"Found target {target} after {attempts} attempts!")

print()

# ============================================
# PROCESSING UNTIL CONDITION MET
# ============================================
print("=== Processing Until Condition Met ===")

balance = 100
interest_rate = 0.05  # 5% per year
target = 150
years = 0

print(f"Starting balance: ${balance}")
print(f"Target: ${target}")

while balance < target:
    years += 1
    balance += balance * interest_rate
    print(f"Year {years}: ${balance:.2f}")

print(f"Reached target in {years} years!")

print()

# ============================================
# NESTED WHILE LOOPS
# ============================================
print("=== Nested While Loops ===")

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

print()

# ============================================
# PRACTICAL EXAMPLE: RETRY LOGIC
# ============================================
print("=== Practical Example: Retry Logic ===")

max_retries = 3
retry_count = 0
success = False

while retry_count < max_retries and not success:
    retry_count += 1
    print(f"Attempt {retry_count}...")

    # Simulate an operation that might fail
    # For demo, succeed on third attempt
    if retry_count == 3:
        success = True
        print("  ✓ Operation succeeded!")
    else:
        print("  ✗ Operation failed, retrying...")

if not success:
    print("Failed after maximum retries")

print()

# ============================================
# PRACTICAL EXAMPLE: WAITING FOR CONDITION
# ============================================
print("=== Practical Example: Waiting for Element ===")

# Simulating waiting for a web element to appear
element_found = False
wait_time = 0
max_wait = 5

print("Waiting for element to appear...")

while not element_found and wait_time < max_wait:
    wait_time += 1
    print(f"  Checking... ({wait_time}s)")

    # Simulate element appearing after 3 seconds
    if wait_time >= 3:
        element_found = True
        print("  ✓ Element found!")

if not element_found:
    print("  ✗ Timeout: Element not found")

print()

# ============================================
# PRACTICAL EXAMPLE: PROCESSING QUEUE
# ============================================
print("=== Practical Example: Processing Queue ===")

tasks = ["Task A", "Task B", "Task C", "Task D"]
print(f"Tasks to process: {tasks}")

while len(tasks) > 0:
    current_task = tasks.pop(0)  # Remove first task
    print(f"Processing: {current_task}")
    print(f"Remaining tasks: {len(tasks)}")

print("All tasks completed!")

print()

# ============================================
# PRACTICAL EXAMPLE: FINDING FIRST MATCH
# ============================================
print("=== Practical Example: Finding First Match ===")

numbers = [2, 4, 6, 7, 8, 10]
target = 7
index = 0
found = False

print(f"Looking for {target} in {numbers}")

while index < len(numbers) and not found:
    if numbers[index] == target:
        found = True
        print(f"Found {target} at index {index}")
    else:
        index += 1

if not found:
    print(f"{target} not found in list")

print()

# ============================================
# PRACTICAL EXAMPLE: POLL UNTIL READY
# ============================================
print("=== Practical Example: Polling Status ===")

status = "pending"
checks = 0
max_checks = 5

print("Checking job status...")

while status == "pending" and checks < max_checks:
    checks += 1
    print(f"  Check {checks}: Status is '{status}'")

    # Simulate status change
    if checks >= 3:
        status = "complete"

print(f"Final status: {status}")

print()

# ============================================
# PRACTICAL EXAMPLE: VALIDATION LOOP
# ============================================
print("=== Practical Example: Input Validation ===")

# Simulating input validation
valid_inputs = ["yes", "no", "maybe"]
user_input = "invalid"
attempts = 0

print(f"Valid inputs: {valid_inputs}")

while user_input not in valid_inputs and attempts < 3:
    attempts += 1
    print(f"Attempt {attempts}: Input '{user_input}' is invalid")

    # Simulate getting new input
    if attempts == 2:
        user_input = "yes"

if user_input in valid_inputs:
    print(f"Valid input received: {user_input}")
else:
    print("Maximum attempts exceeded")

print()

# ============================================
# COMPARISON: FOR VS WHILE
# ============================================
print("=== Summary: For vs While ===")

print("\nUse FOR when:")
print("  • You know how many iterations you need")
print("  • You're iterating over a sequence (list, string, range)")
print("  • You want cleaner, more readable code for simple iteration")

print("\nUse WHILE when:")
print("  • You don't know how many iterations needed")
print("  • You're waiting for a condition to change")
print("  • You're implementing retry logic")
print("  • You're processing until a state is reached")
