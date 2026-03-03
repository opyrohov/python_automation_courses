"""
Lecture 1: Basic Operators
This file demonstrates various operators in Python including arithmetic, comparison, and logical operators.
"""

# ============================================
# ARITHMETIC OPERATORS
# ============================================

print("=" * 50)
print("ARITHMETIC OPERATORS")
print("=" * 50)

# Addition (+)
num1 = 10
num2 = 5
result = num1 + num2
print(f"{num1} + {num2} = {result}")

# Subtraction (-)
result = num1 - num2
print(f"{num1} - {num2} = {result}")

# Multiplication (*)
result = num1 * num2
print(f"{num1} * {num2} = {result}")

# Division (/) - always returns a float
result = num1 / num2
print(f"{num1} / {num2} = {result}")

# Floor Division (//) - returns integer part only
result = num1 // num2
print(f"{num1} // {num2} = {result}")

# Example with remainder
result = 17 // 5
print(f"17 // 5 = {result} (drops the decimal)")

# Modulus (%) - returns remainder
result = num1 % num2
print(f"{num1} % {num2} = {result}")

# More practical modulus example
result = 17 % 5
print(f"17 % 5 = {result} (remainder after division)")

# Exponentiation (**) - power
result = num1 ** num2
print(f"{num1} ** {num2} = {result} (10 to the power of 5)")

result = 2 ** 3
print(f"2 ** 3 = {result} (2 cubed)")
print()

# ============================================
# COMPARISON OPERATORS
# ============================================

print("=" * 50)
print("COMPARISON OPERATORS")
print("=" * 50)

a = 10
b = 20
c = 10

# Equal to (==)
print(f"{a} == {b} is {a == b}")
print(f"{a} == {c} is {a == c}")

# Not equal to (!=)
print(f"{a} != {b} is {a != b}")
print(f"{a} != {c} is {a != c}")

# Greater than (>)
print(f"{a} > {b} is {a > b}")
print(f"{b} > {a} is {b > a}")

# Less than (<)
print(f"{a} < {b} is {a < b}")
print(f"{b} < {a} is {b < a}")

# Greater than or equal to (>=)
print(f"{a} >= {c} is {a >= c}")
print(f"{a} >= {b} is {a >= b}")

# Less than or equal to (<=)
print(f"{a} <= {c} is {a <= c}")
print(f"{b} <= {a} is {b <= a}")
print()

# ============================================
# LOGICAL OPERATORS
# ============================================

print("=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50)

# AND operator - both conditions must be True
is_adult = True
has_ticket = True
can_enter_movie = is_adult and has_ticket
print(f"Is adult: {is_adult}, Has ticket: {has_ticket}")
print(f"Can enter movie: {can_enter_movie}")
print()

is_adult = True
has_ticket = False
can_enter_movie = is_adult and has_ticket
print(f"Is adult: {is_adult}, Has ticket: {has_ticket}")
print(f"Can enter movie: {can_enter_movie}")
print()

# OR operator - at least one condition must be True
has_cash = False
has_card = True
can_pay = has_cash or has_card
print(f"Has cash: {has_cash}, Has card: {has_card}")
print(f"Can pay: {can_pay}")
print()

# NOT operator - inverts the boolean value
is_raining = False
is_sunny = not is_raining
print(f"Is raining: {is_raining}")
print(f"Is sunny: {is_sunny}")
print()

# ============================================
# COMBINED EXAMPLES
# ============================================

print("=" * 50)
print("COMBINED EXAMPLES")
print("=" * 50)

# Age eligibility example
age = 25
has_license = True
can_rent_car = (age >= 21) and has_license
print(f"Age: {age}, Has license: {has_license}")
print(f"Can rent car: {can_rent_car}")
print()

# Discount eligibility
is_student = True
is_senior = False
age = 22
gets_discount = is_student or (age >= 65)
print(f"Is student: {is_student}, Age: {age}")
print(f"Gets discount: {gets_discount}")
print()

# Temperature check
temperature = 72
is_comfortable = (temperature >= 68) and (temperature <= 78)
print(f"Temperature: {temperature}°F")
print(f"Is comfortable: {is_comfortable}")
print()

# ============================================
# OPERATOR PRECEDENCE
# ============================================

print("=" * 50)
print("OPERATOR PRECEDENCE")
print("=" * 50)

# Operators are evaluated in order: ** > *, /, //, % > +, -
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result} (multiplication first)")

result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result} (parentheses first)")

result = 10 + 5 * 2 ** 3
print(f"10 + 5 * 2 ** 3 = {result}")
print("Order: 2**3=8, then 5*8=40, then 10+40=50")
print()

# ============================================
# COMPOUND ASSIGNMENT OPERATORS
# ============================================

print("=" * 50)
print("COMPOUND ASSIGNMENT OPERATORS")
print("=" * 50)

# These are shortcuts that combine an operation with assignment
score = 100

# Add and assign (+=)
score += 10  # Same as: score = score + 10
print(f"After += 10: {score}")

# Subtract and assign (-=)
score -= 5   # Same as: score = score - 5
print(f"After -= 5: {score}")

# Multiply and assign (*=)
score *= 2   # Same as: score = score * 2
print(f"After *= 2: {score}")

# Divide and assign (/=)
score /= 4   # Same as: score = score / 4
print(f"After /= 4: {score}")
print()

# ============================================
# PRACTICAL EXAMPLES
# ============================================

print("=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Calculate total price with tax
item_price = 29.99
tax_rate = 0.08
tax_amount = item_price * tax_rate
total_price = item_price + tax_amount
print(f"Item price: ${item_price}")
print(f"Tax (8%): ${tax_amount:.2f}")
print(f"Total: ${total_price:.2f}")
print()

# Calculate average
test1 = 85
test2 = 92
test3 = 78
average = (test1 + test2 + test3) / 3
print(f"Test scores: {test1}, {test2}, {test3}")
print(f"Average: {average:.2f}")
print()

# Check if number is even or odd using modulus
number = 17
is_even = (number % 2) == 0
print(f"Is {number} even? {is_even}")
print(f"Is {number} odd? {not is_even}")
