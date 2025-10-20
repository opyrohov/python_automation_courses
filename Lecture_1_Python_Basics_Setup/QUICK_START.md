# Quick Start Guide - Lecture 1

Get up and running with Lecture 1 in just a few minutes!

## Prerequisites

Before starting this lecture, make sure you have:
- [ ] Python 3.11 or later installed
- [ ] A code editor (VS Code or PyCharm) installed
- [ ] Basic computer skills

## 🎯 Two Ways to Learn

### Option 1: Interactive Presentation (Recommended for Overview)
Open `presentation.html` in your browser for a slide-based overview of all concepts.
- 20 interactive slides with syntax highlighting
- Navigate with arrow keys or buttons
- Great for first-time learners

### Option 2: Hands-On with Code Files (Recommended for Practice)
Follow the steps below to work directly with Python files and exercises.

## Getting Started

### Step 1: Verify Python Installation

Open your terminal or command prompt and run:

```bash
python --version
```

You should see something like `Python 3.11.x` or later.

If not, follow the installation instructions in [README.md](README.md#installation--setup).

### Step 2: Set Up Your Workspace

1. Navigate to the lecture folder:
   ```bash
   cd Lecture_1_Python_Basics_Setup
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. (Optional) Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

### Step 3: Run Your First Example

Try running the first example file:

```bash
python examples/01_variables_and_datatypes.py
```

You should see output showing various variable examples!

## Learning Path

Follow this order for the best learning experience:

### 1. Read the Main README
Start with [README.md](README.md) to understand the lecture structure.

### 2. Study the Examples (in order)

Run and study each example file:

```bash
# Example 1: Variables and Data Types
python examples/01_variables_and_datatypes.py

# Example 2: Operators
python examples/02_operators.py

# Example 3: Print Statements
python examples/03_print_statements.py

# Example 4: Comments and Code Structure
python examples/04_comments_and_structure.py
```

**Pro Tip:** Open each file in your code editor while running it to see the code and output side-by-side.

### 3. Complete the Exercises

After studying the examples, complete the exercises:

```bash
# Exercise 1: Variables and Data Types
python exercises/exercise_01_variables.py

# Exercise 2: Calculations and Operators
python exercises/exercise_02_calculations.py

# Exercise 3: Personal Information Card
python exercises/exercise_03_personal_info.py
```

### 4. Check Your Solutions

After completing each exercise, check your work against [exercises/SOLUTIONS.md](exercises/SOLUTIONS.md).

## Tips for Success

### While Studying Examples

1. **Read the code first** - Try to understand what it does before running it
2. **Run the code** - See the actual output
3. **Modify the code** - Change values and see what happens
4. **Take notes** - Write down important concepts

### While Doing Exercises

1. **Don't peek at solutions** - Try to solve problems independently first
2. **Use the examples** - Refer back to example files when stuck
3. **Test frequently** - Run your code often to catch errors early
4. **Experiment** - Try different approaches

### Debugging Tips

If you get an error:

1. **Read the error message** - It usually tells you what's wrong
2. **Check the line number** - Errors indicate which line failed
3. **Common beginner mistakes:**
   - Misspelled variable names
   - Missing quotes around strings
   - Wrong indentation
   - Missing colons or parentheses

## Running Python Code

### Method 1: From Terminal

```bash
python filename.py
```

### Method 2: In VS Code

1. Open the file
2. Click the "Run" button (▶️) in the top right
3. Or press `Ctrl+Alt+N` (Windows/Linux) or `Cmd+Alt+N` (Mac)

### Method 3: In PyCharm

1. Open the file
2. Right-click in the editor
3. Select "Run 'filename'"
4. Or press `Ctrl+Shift+F10` (Windows/Linux) or `Ctrl+Shift+R` (Mac)

## Practice Schedule

Here's a suggested schedule to complete this lecture:

### Day 1 (1-2 hours)
- Install Python and your code editor
- Read README.md
- Study examples 1 and 2
- Complete exercise 1

### Day 2 (1-2 hours)
- Study examples 3 and 4
- Complete exercises 2 and 3
- Review solutions

### Day 3 (30 minutes)
- Review all concepts
- Experiment with your own code
- Move on to Lecture 2

## Getting Help

If you're stuck:

1. **Re-read the examples** - The answer is usually there
2. **Check the solutions** - See how it should be done
3. **Google the error** - Copy the error message into Google
4. **Take a break** - Sometimes stepping away helps

## What You'll Learn

By the end of this lecture, you'll be able to:

- ✓ Install and set up Python
- ✓ Create variables and use different data types
- ✓ Perform calculations with operators
- ✓ Use print statements to display output
- ✓ Write clean, well-commented code
- ✓ Follow Python coding conventions

## Next Steps

Once you complete all exercises:

1. Review your solutions
2. Create your own mini-project combining all concepts
3. Move on to Lecture 2

## Troubleshooting

### Python Not Found

If you get "python is not recognized":
- Make sure Python is installed
- Check "Add Python to PATH" was selected during installation
- Try `python3` instead of `python`

### Import Errors

This lecture doesn't use any external libraries, so you shouldn't see import errors. If you do, make sure you're running the correct file.

### Syntax Errors

Common causes:
- Missing quotes: `name = John` → `name = "John"`
- Missing colons (in if statements - covered later)
- Wrong indentation

---

**Ready to start? Open [README.md](README.md) and begin your Python journey!**
