"""
Exercise 3: Personal Information Card

Instructions:
1. Create variables with your personal information
2. Use print statements and string formatting to display a professional information card
3. Practice using f-strings, formatting numbers, and creating visual output
4. Be creative with the layout!

Estimated time: 20-25 minutes
"""

# ============================================
# TASK 1: Create Your Information Variables
# ============================================
# Create variables for the following information:

# Personal Details
# - full_name: Your full name
# - age: Your age
# - occupation: Your current occupation or "Student"
# - email: Your email address (can be fake)
# - phone: Your phone number (can be fake)

# YOUR CODE HERE:






# Location
# - city: Your city
# - country: Your country

# YOUR CODE HERE:



# Skills (create at least 3 skill variables)
# - skill1, skill2, skill3: Programming languages or skills you know or want to learn

# YOUR CODE HERE:




# ============================================
# TASK 2: Create a Simple Information Card
# ============================================
# Use print statements to display your information in a nice format
# Example output:
"""
==================================================
              PERSONAL INFORMATION
==================================================
Name:         John Doe
Age:          25
Occupation:   Software Developer
Email:        john.doe@email.com
Phone:        (555) 123-4567
Location:     New York, USA
==================================================
"""

# YOUR CODE HERE (use print statements with f-strings):
print("=" * 50)
print("              PERSONAL INFORMATION")
print("=" * 50)
# Add your print statements here







print("=" * 50)
print()

# ============================================
# TASK 3: Create a Skills Section
# ============================================
# Display your skills in a formatted list
# Example output:
"""
==================================================
                   SKILLS
==================================================
- Python
- JavaScript
- HTML/CSS
==================================================
"""

# YOUR CODE HERE:
print("=" * 50)
print("                   SKILLS")
print("=" * 50)
# Add your skills here




print("=" * 50)
print()

# ============================================
# TASK 4: Create a Professional Summary
# ============================================
# Write a multi-line string with a brief professional summary or bio (3-5 lines)
# Store it in a variable called 'summary'

# YOUR CODE HERE:
summary = """
Write your professional summary here.
You can include your interests, goals, or background.
Make it 3-5 lines long.
"""

# Display the summary
print("=" * 50)
print("           PROFESSIONAL SUMMARY")
print("=" * 50)
print(summary)
print("=" * 50)
print()

# ============================================
# TASK 5: Create a Statistics Section
# ============================================
# Calculate and display some statistics about yourself

# Create these variables:
# - years_coding: How many years you've been coding (or want to code)
# - projects_completed: Number of projects you've completed (can be estimated)
# - hours_per_week: Hours per week you spend coding or learning

# YOUR CODE HERE:




# Calculate:
# - total_hours: years_coding * 52 weeks * hours_per_week
# - hours_per_project: total_hours / projects_completed (if projects_completed > 0)

# YOUR CODE HERE:


if projects_completed > 0:
    hours_per_project = total_hours / projects_completed
else:
    hours_per_project = 0

# Display the statistics
print("=" * 50)
print("              STATISTICS")
print("=" * 50)
print(f"Years Coding:           {years_coding}")
print(f"Projects Completed:     {projects_completed}")
print(f"Hours per Week:         {hours_per_week}")
print(f"Total Hours:            {total_hours:,}")
if projects_completed > 0:
    print(f"Avg Hours per Project:  {hours_per_project:.1f}")
print("=" * 50)
print()

# ============================================
# TASK 6: Create Contact Information
# ============================================
# Format your contact information nicely

print("=" * 50)
print("            CONTACT INFORMATION")
print("=" * 50)
# Display email and phone with nice formatting
# YOUR CODE HERE (use f-strings):



print("=" * 50)
print()

# ============================================
# BONUS TASK: Create a Complete Business Card
# ============================================
# Combine everything into one nice-looking business card
# Be creative! Use symbols, spacing, and formatting to make it look professional

print("\n")
print("*" * 60)
print("*" + " " * 58 + "*")
# Add your business card design here
# Include: name, occupation, email, phone, location, and top skill
# YOUR CODE HERE:








print("*" + " " * 58 + "*")
print("*" * 60)
print()

# ============================================
# EXTRA BONUS: Fun Facts Section
# ============================================
# Create variables and display fun facts about yourself

# Create these variables:
# - favorite_language: Your favorite programming language (or one you want to learn)
# - favorite_food: Your favorite food
# - hobby: Your hobby

# YOUR CODE HERE:




# Display fun facts
print("=" * 50)
print("                FUN FACTS")
print("=" * 50)
print(f"Favorite Language: {favorite_language}")
print(f"Favorite Food:     {favorite_food}")
print(f"Hobby:             {hobby}")
print("=" * 50)
print()

print("=" * 50)
print("   Congratulations! You completed Exercise 3!")
print("=" * 50)
print("\nGreat job creating your personal information card!")
print("This exercise helped you practice:")
print("- Creating and using variables")
print("- String formatting with f-strings")
print("- Formatting output for readability")
print("- Working with different data types")
print("- Basic calculations")
