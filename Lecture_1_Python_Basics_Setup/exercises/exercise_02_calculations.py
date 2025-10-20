"""
Exercise 2: Calculations and Operators

Instructions:
1. Complete each task by writing the appropriate calculations
2. Use the provided variables to perform calculations
3. Store results in the specified variable names
4. Run the file to check your results

Estimated time: 20-25 minutes
"""

# ============================================
# TASK 1: Restaurant Bill Calculator
# ============================================
# Calculate the total cost of a restaurant bill

meal_cost = 45.50
drink_cost = 8.75
tax_rate = 0.08  # 8% tax
tip_rate = 0.18  # 18% tip

# Calculate the following:
# - subtotal: meal_cost + drink_cost
# - tax_amount: subtotal * tax_rate
# - total_before_tip: subtotal + tax_amount
# - tip_amount: total_before_tip * tip_rate
# - final_total: total_before_tip + tip_amount

# YOUR CODE HERE:






# Test your calculations (don't modify this)
print("=" * 50)
print("TASK 1: Restaurant Bill")
print("=" * 50)
print(f"Meal: ${meal_cost:.2f}")
print(f"Drinks: ${drink_cost:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax_amount:.2f}")
print(f"Tip (18%): ${tip_amount:.2f}")
print(f"Final Total: ${final_total:.2f}")
print()

# ============================================
# TASK 2: Temperature Converter
# ============================================
# Convert temperature from Fahrenheit to Celsius
# Formula: Celsius = (Fahrenheit - 32) * 5/9

fahrenheit = 72

# Calculate celsius using the formula above
# YOUR CODE HERE:


# Test your calculation (don't modify this)
print("=" * 50)
print("TASK 2: Temperature Conversion")
print("=" * 50)
print(f"{fahrenheit}°F = {celsius:.1f}°C")
print()

# ============================================
# TASK 3: Circle Calculations
# ============================================
# Calculate area and circumference of a circle
# Area = π * r²
# Circumference = 2 * π * r

radius = 7.5
pi = 3.14159

# Calculate:
# - area: pi * radius squared
# - circumference: 2 * pi * radius

# YOUR CODE HERE:



# Test your calculations (don't modify this)
print("=" * 50)
print("TASK 3: Circle Calculations")
print("=" * 50)
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

# ============================================
# TASK 4: Age Calculator
# ============================================
# Calculate various time units from age

age_in_years = 25

# Calculate:
# - age_in_months: age_in_years * 12
# - age_in_days: age_in_years * 365 (approximate, ignoring leap years)
# - age_in_hours: age_in_days * 24

# YOUR CODE HERE:




# Test your calculations (don't modify this)
print("=" * 50)
print("TASK 4: Age Calculator")
print("=" * 50)
print(f"Age: {age_in_years} years")
print(f"Age: {age_in_months} months")
print(f"Age: {age_in_days:,} days")
print(f"Age: {age_in_hours:,} hours")
print()

# ============================================
# TASK 5: Even or Odd Checker
# ============================================
# Use the modulus operator to check if numbers are even

number1 = 42
number2 = 17

# For each number, create a boolean variable that is True if even, False if odd
# Hint: A number is even if number % 2 == 0

# YOUR CODE HERE:



# Test your calculations (don't modify this)
print("=" * 50)
print("TASK 5: Even or Odd")
print("=" * 50)
print(f"{number1} is even: {is_number1_even}")
print(f"{number2} is even: {is_number2_even}")
print()

# ============================================
# TASK 6: Comparison Operations
# ============================================
# Compare values and store results in boolean variables

score1 = 85
score2 = 92
passing_score = 60

# Create these boolean variables:
# - score1_passed: Is score1 greater than or equal to passing_score?
# - score2_passed: Is score2 greater than or equal to passing_score?
# - scores_equal: Are score1 and score2 equal?
# - score2_higher: Is score2 greater than score1?

# YOUR CODE HERE:





# Test your comparisons (don't modify this)
print("=" * 50)
print("TASK 6: Score Comparisons")
print("=" * 50)
print(f"Score 1 ({score1}) passed: {score1_passed}")
print(f"Score 2 ({score2}) passed: {score2_passed}")
print(f"Scores are equal: {scores_equal}")
print(f"Score 2 is higher: {score2_higher}")
print()

# ============================================
# TASK 7: Logical Operators
# ============================================
# Use logical operators to combine conditions

age = 22
has_ticket = True
has_id = True

# Create these boolean variables:
# - can_enter_movie: age is 18 or older AND has_ticket is True
# - can_buy_alcohol: age is 21 or older AND has_id is True
# - missing_requirement: does NOT have ticket OR does NOT have ID

# YOUR CODE HERE:




# Test your logic (don't modify this)
print("=" * 50)
print("TASK 7: Logical Operations")
print("=" * 50)
print(f"Age: {age}, Has Ticket: {has_ticket}, Has ID: {has_id}")
print(f"Can enter movie (18+ with ticket): {can_enter_movie}")
print(f"Can buy alcohol (21+ with ID): {can_buy_alcohol}")
print(f"Missing requirement: {missing_requirement}")
print()

# ============================================
# TASK 8: Compound Assignment
# ============================================
# Use compound assignment operators

balance = 1000.00

# Perform these operations in order using compound assignment:
# 1. Add 500 to balance (use +=)
# 2. Subtract 150 from balance (use -=)
# 3. Multiply balance by 1.05 (5% interest) (use *=)

# YOUR CODE HERE:




# Test your operations (don't modify this)
print("=" * 50)
print("TASK 8: Bank Account Balance")
print("=" * 50)
print(f"Final Balance: ${balance:.2f}")
print()

# ============================================
# BONUS TASK: Price Discount Calculator
# ============================================
# Calculate final price after multiple discounts

original_price = 299.99
discount_percent = 20  # 20% off
additional_discount = 10  # Additional $10 off

# Calculate:
# - discount_amount: original_price * (discount_percent / 100)
# - price_after_percent: original_price - discount_amount
# - final_price: price_after_percent - additional_discount
# - total_savings: original_price - final_price

# YOUR CODE HERE:





# Test your calculations (don't modify this)
print("=" * 50)
print("BONUS: Discount Calculator")
print("=" * 50)
print(f"Original Price: ${original_price:.2f}")
print(f"{discount_percent}% Discount: -${discount_amount:.2f}")
print(f"Additional Discount: -${additional_discount:.2f}")
print(f"Final Price: ${final_price:.2f}")
print(f"Total Savings: ${total_savings:.2f}")
print()

print("=" * 50)
print("Congratulations! You completed Exercise 2!")
print("=" * 50)
