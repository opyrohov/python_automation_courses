"""
Exercise 2: Conditional Logic Practice
Complete the exercises below to practice if/elif/else statements.
"""

# ============================================
# EXERCISE 1: Age Classifier
# ============================================
print("Exercise 1: Age Classifier")
print("-" * 40)

age = 25  # Try different values

# TODO: Write conditions to classify the age:
# 0-12: "Child"
# 13-17: "Teenager"
# 18-64: "Adult"
# 65+: "Senior"


print()

# ============================================
# EXERCISE 2: Grade Calculator
# ============================================
print("Exercise 2: Grade Calculator")
print("-" * 40)

score = 87  # Try different values

# TODO: Assign a letter grade based on the score:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# Also print a message (e.g., "Excellent!", "Good job!", etc.)


print()

# ============================================
# EXERCISE 3: Login Validator
# ============================================
print("Exercise 3: Login Validator")
print("-" * 40)

username = "admin"
password = "secret123"
is_account_active = True

# TODO: Check if login is successful:
# - Username must be "admin"
# - Password must be "secret123"
# - Account must be active
# Print appropriate success or error messages


print()

# ============================================
# EXERCISE 4: Shopping Discount Calculator
# ============================================
print("Exercise 4: Shopping Discount Calculator")
print("-" * 40)

total_amount = 150
is_member = True
has_coupon = False

# TODO: Calculate discount based on conditions:
# - If member AND total > 100: 20% discount
# - If member: 10% discount
# - If has_coupon: 15% discount
# - If total > 200: 25% discount
# Apply the best discount and print final price


print()

# ============================================
# EXERCISE 5: Temperature Adviser
# ============================================
print("Exercise 5: Temperature Adviser")
print("-" * 40)

temperature = 22  # in Celsius
is_raining = False

# TODO: Give clothing advice based on conditions:
# temp < 0: "Wear a heavy coat"
# temp 0-15: "Wear a jacket"
# temp 16-25: "Wear a light sweater"
# temp > 25: "T-shirt weather"
# If it's raining, add "and take an umbrella"


print()

# ============================================
# EXERCISE 6: Password Strength Validator
# ============================================
print("Exercise 6: Password Strength Validator")
print("-" * 40)

password = "MyPass123"

# TODO: Validate password strength:
# Weak: length < 8
# Medium: length >= 8 AND (has numbers OR has uppercase)
# Strong: length >= 8 AND has numbers AND has uppercase AND has lowercase
# Print the strength level and suggestions for improvement


print()

# ============================================
# EXERCISE 7: Traffic Light System
# ============================================
print("Exercise 7: Traffic Light System")
print("-" * 40)

light_color = "green"  # Try: "red", "yellow", "green"
pedestrian_crossing = False

# TODO: Implement traffic light logic:
# red: "Stop"
# yellow: "Slow down"
# green: "Go"
# If pedestrian_crossing is True and light is green: "Slow down - pedestrians crossing"


print()

# ============================================
# EXERCISE 8: Number Analyzer
# ============================================
print("Exercise 8: Number Analyzer")
print("-" * 40)

number = 15  # Try different values

# TODO: Analyze the number:
# Check if it's:
# - Positive, negative, or zero
# - Even or odd
# - Divisible by 5
# Print all applicable descriptions


print()

# ============================================
# EXERCISE 9: Movie Ticket Pricing
# ============================================
print("Exercise 9: Movie Ticket Pricing")
print("-" * 40)

age = 25
is_student = False
is_senior = False
show_time = "matinee"  # or "evening"

# TODO: Calculate ticket price:
# Base price: $15
# Matinee (before 5pm): -$3
# Children (under 13): -$5
# Students: -$4
# Seniors (65+): -$6
# Print the final price


print()

# ============================================
# EXERCISE 10: File Upload Validator
# ============================================
print("Exercise 10: File Upload Validator")
print("-" * 40)

filename = "document.pdf"
file_size = 4.5  # in MB
allowed_extensions = [".pdf", ".doc", ".docx"]
max_size = 5.0  # in MB

# TODO: Validate file upload:
# Check if:
# - File has an allowed extension
# - File size is within limit
# Print validation result and specific error messages if invalid


print()

# ============================================
# BONUS CHALLENGE: ATM Withdrawal System
# ============================================
print("BONUS: ATM Withdrawal System")
print("-" * 40)

account_balance = 1000
withdrawal_amount = 250
daily_limit = 500
withdrawals_today = 300
pin_correct = True

# TODO: Implement ATM withdrawal logic:
# Check:
# - PIN is correct
# - Sufficient balance
# - Not exceeding daily limit (including previous withdrawals)
# Print appropriate messages for each scenario


print()

print("=" * 40)
print("Excellent work! Check SOLUTIONS.md for answers.")
print("=" * 40)
