"""
Lecture 7 - Exercise 1: File Basics
==================================
Practice reading and writing files.

Instructions:
1. Complete each TODO section
2. Test your code by running: python exercise_01_file_basics.py
3. Check your solutions against SOLUTIONS.md
"""

from pathlib import Path

# Create output directory
output_dir = Path(__file__).parent / "my_output"
output_dir.mkdir(exist_ok=True)

print("=" * 50)
print("EXERCISE: File Basics")
print("=" * 50)
print()

# Exercise 1.1: Write a Simple Text File
# ======================================
# TODO: Create a file called "greeting.txt" in my_output folder
# Write 3 lines: "Hello, Python!", "File handling is easy.", "Let's practice!"

# Your code here:


print("-" * 50)


# Exercise 1.2: Read the File You Created
# =======================================
# TODO: Read the greeting.txt file and print its contents

# Your code here:


print("-" * 50)


# Exercise 1.3: Append to a File
# ==============================
# TODO: Append a new line "This line was added later!" to greeting.txt

# Your code here:


print("-" * 50)


# Exercise 1.4: Count Lines in a File
# ===================================
# TODO: Read greeting.txt and print the total number of lines

# Your code here:


print("-" * 50)


# Exercise 1.5: Write Multiple Lines
# ==================================
# TODO: Create a file "languages.txt" with these programming languages (one per line):
# Python, JavaScript, Java, C++, Go

# Your code here:


print("-" * 50)


# Exercise 1.6: Read Specific Lines
# =================================
# TODO: Read languages.txt and print only the first and last language

# Your code here:


print("-" * 50)


# Exercise 1.7: Create a Log File
# ===============================
# TODO: Create a function write_log(message) that appends messages with timestamp
# to "test.log" file. Test it with 3 different messages.

# Your code here:


print("-" * 50)


# BONUS: File Existence Check
# ===========================
# TODO: Write a function that checks if a file exists before reading it
# Test it with an existing file and a non-existing file

# Your code here:


print("=" * 50)
print("Exercise 1 Complete!")
print("=" * 50)
