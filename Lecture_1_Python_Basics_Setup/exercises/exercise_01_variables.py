"""
Exercise 1: Variables and Data Types

Instructions:
1. Complete each task below by writing the appropriate code
2. Run the file to check your results
3. Make sure all print statements display the correct output

Estimated time: 15-20 minutes
"""

# ============================================
# TASK 1: Create Variables
# ============================================
# Create the following variables with appropriate values:
# - A variable called 'city' with your city name
# - A variable called 'population' with an estimated population (integer)
# - A variable called 'area_sq_miles' with the area in square miles (float)
# - A variable called 'is_capital' indicating if it's a capital city (boolean)

# YOUR CODE HERE:



# Test your variables (don't modify this)
print("=" * 50)
print("TASK 1: City Information")
print("=" * 50)
print(f"City: {city}")
print(f"Population: {population:,}")
print(f"Area: {area_sq_miles} square miles")
print(f"Is Capital: {is_capital}")
print()

# ============================================
# TASK 2: Personal Information
# ============================================
# Create variables for your personal information:
# - first_name (string)
# - last_name (string)
# - age (integer)
# - favorite_number (integer or float)

# YOUR CODE HERE:



# Create a variable called 'full_name' that combines first_name and last_name
# YOUR CODE HERE:


# Test your variables (don't modify this)
print("=" * 50)
print("TASK 2: Personal Information")
print("=" * 50)
print(f"Full Name: {full_name}")
print(f"Age: {age}")
print(f"Favorite Number: {favorite_number}")
print()

# ============================================
# TASK 3: Shopping Cart
# ============================================
# You're building a simple shopping cart. Create these variables:
# - item1_name (string): "Laptop"
# - item1_price (float): 899.99
# - item1_quantity (integer): 1
# - item2_name (string): "Mouse"
# - item2_price (float): 25.50
# - item2_quantity (integer): 2

# YOUR CODE HERE:



# Test your variables (don't modify this)
print("=" * 50)
print("TASK 3: Shopping Cart")
print("=" * 50)
print(f"{item1_name}: ${item1_price} x {item1_quantity}")
print(f"{item2_name}: ${item2_price} x {item2_quantity}")
print()

# ============================================
# TASK 4: Type Conversion
# ============================================
# You have these string variables:
age_string = "28"
price_string = "49.99"
quantity_string = "5"

# Convert them to appropriate numeric types and store in new variables:
# - age_number (should be an integer)
# - price_number (should be a float)
# - quantity_number (should be an integer)

# YOUR CODE HERE:



# Test your conversions (don't modify this)
print("=" * 50)
print("TASK 4: Type Conversion")
print("=" * 50)
print(f"Age: {age_number} (type: {type(age_number).__name__})")
print(f"Price: ${price_number} (type: {type(price_number).__name__})")
print(f"Quantity: {quantity_number} (type: {type(quantity_number).__name__})")
print()

# ============================================
# TASK 5: Boolean Variables
# ============================================
# Create boolean variables for the following scenarios:
# - is_student: Are you currently a student? (True/False)
# - has_experience: Do you have programming experience? (True/False)
# - is_weekend: Is today a weekend? (True/False)

# YOUR CODE HERE:



# Test your variables (don't modify this)
print("=" * 50)
print("TASK 5: Boolean Variables")
print("=" * 50)
print(f"Is Student: {is_student}")
print(f"Has Experience: {has_experience}")
print(f"Is Weekend: {is_weekend}")
print()

# ============================================
# BONUS TASK: Multi-line String
# ============================================
# Create a multi-line string variable called 'bio' with a short
# biography about yourself (3-4 lines)

# YOUR CODE HERE:



# Test your bio (don't modify this)
print("=" * 50)
print("BONUS: Biography")
print("=" * 50)
print(bio)
print()

print("=" * 50)
print("Congratulations! You completed Exercise 1!")
print("=" * 50)
