# Exercise Solutions - Lecture 1

This file contains sample solutions for the exercises. Try to complete the exercises on your own first before checking these solutions!

## Exercise 1: Variables and Data Types

### Task 1: Create Variables
```python
city = "New York"
population = 8000000
area_sq_miles = 302.6
is_capital = False
```

### Task 2: Personal Information
```python
first_name = "John"
last_name = "Doe"
age = 25
favorite_number = 7

full_name = first_name + " " + last_name
# or
full_name = f"{first_name} {last_name}"
```

### Task 3: Shopping Cart
```python
item1_name = "Laptop"
item1_price = 899.99
item1_quantity = 1
item2_name = "Mouse"
item2_price = 25.50
item2_quantity = 2
```

### Task 4: Type Conversion
```python
age_number = int(age_string)
price_number = float(price_string)
quantity_number = int(quantity_string)
```

### Task 5: Boolean Variables
```python
is_student = True
has_experience = False
is_weekend = True
```

### Bonus Task: Multi-line String
```python
bio = """
I am a Python developer learning automation.
I enjoy solving problems and building useful tools.
This course is helping me improve my programming skills.
"""
```

---

## Exercise 2: Calculations and Operators

### Task 1: Restaurant Bill Calculator
```python
subtotal = meal_cost + drink_cost
tax_amount = subtotal * tax_rate
total_before_tip = subtotal + tax_amount
tip_amount = total_before_tip * tip_rate
final_total = total_before_tip + tip_amount
```

### Task 2: Temperature Converter
```python
celsius = (fahrenheit - 32) * 5/9
```

### Task 3: Circle Calculations
```python
area = pi * radius ** 2
circumference = 2 * pi * radius
```

### Task 4: Age Calculator
```python
age_in_months = age_in_years * 12
age_in_days = age_in_years * 365
age_in_hours = age_in_days * 24
```

### Task 5: Even or Odd Checker
```python
is_number1_even = number1 % 2 == 0
is_number2_even = number2 % 2 == 0
```

### Task 6: Comparison Operations
```python
score1_passed = score1 >= passing_score
score2_passed = score2 >= passing_score
scores_equal = score1 == score2
score2_higher = score2 > score1
```

### Task 7: Logical Operators
```python
can_enter_movie = age >= 18 and has_ticket
can_buy_alcohol = age >= 21 and has_id
missing_requirement = not has_ticket or not has_id
```

### Task 8: Compound Assignment
```python
balance += 500
balance -= 150
balance *= 1.05
```

### Bonus Task: Price Discount Calculator
```python
discount_amount = original_price * (discount_percent / 100)
price_after_percent = original_price - discount_amount
final_price = price_after_percent - additional_discount
total_savings = original_price - final_price
```

---

## Exercise 3: Personal Information Card

### Sample Solution

```python
# Task 1: Variables
full_name = "Jane Smith"
age = 28
occupation = "Software Developer"
email = "jane.smith@email.com"
phone = "(555) 123-4567"
city = "San Francisco"
country = "USA"
skill1 = "Python"
skill2 = "JavaScript"
skill3 = "SQL"

# Task 2: Information Card
print("=" * 50)
print("              PERSONAL INFORMATION")
print("=" * 50)
print(f"Name:         {full_name}")
print(f"Age:          {age}")
print(f"Occupation:   {occupation}")
print(f"Email:        {email}")
print(f"Phone:        {phone}")
print(f"Location:     {city}, {country}")
print("=" * 50)

# Task 3: Skills Section
print("=" * 50)
print("                   SKILLS")
print("=" * 50)
print(f"- {skill1}")
print(f"- {skill2}")
print(f"- {skill3}")
print("=" * 50)

# Task 4: Professional Summary
summary = """
Passionate software developer with 3 years of experience
in web development and automation. Eager to learn new
technologies and solve complex problems. Currently
expanding skills in Python automation and data analysis.
"""

# Task 5: Statistics
years_coding = 3
projects_completed = 15
hours_per_week = 20
total_hours = years_coding * 52 * hours_per_week

# Task 6: Contact Information
print("=" * 50)
print("            CONTACT INFORMATION")
print("=" * 50)
print(f"Email: {email}")
print(f"Phone: {phone}")
print("=" * 50)

# Bonus: Business Card
print("\n")
print("*" * 60)
print("*" + " " * 58 + "*")
print("*" + " " * 20 + "JANE SMITH" + " " * 28 + "*")
print("*" + " " * 16 + "Software Developer" + " " * 24 + "*")
print("*" + " " * 58 + "*")
print("*" + " " * 10 + f"Email: {email}" + " " * 14 + "*")
print("*" + " " * 10 + f"Phone: {phone}" + " " * 20 + "*")
print("*" + " " * 10 + f"Location: {city}, {country}" + " " * 12 + "*")
print("*" + " " * 58 + "*")
print("*" * 60)

# Extra Bonus: Fun Facts
favorite_language = "Python"
favorite_food = "Pizza"
hobby = "Photography"
```

---

## Tips for Success

1. **Don't just copy solutions** - Try to understand WHY each solution works
2. **Experiment** - Modify the solutions and see what happens
3. **Make mistakes** - Errors are learning opportunities
4. **Practice** - Create your own variations of these exercises
5. **Ask questions** - If something doesn't make sense, research it or ask for help

## Next Steps

After completing these exercises, you should feel comfortable with:
- Creating and naming variables
- Working with strings, numbers, and booleans
- Performing calculations and comparisons
- Using logical operators
- Formatting output with print and f-strings
