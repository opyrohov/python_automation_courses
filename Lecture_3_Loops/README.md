# Lecture 3: Loops

Welcome to the third lecture of the Python Automation Course! In this lecture, you'll learn how to use loops to repeat actions and iterate through data - essential skills for web automation.

## Table of Contents
1. [For Loops](#for-loops)
2. [While Loops](#while-loops)
3. [The range() Function](#the-range-function)
4. [Break and Continue](#break-and-continue)
5. [Why This Matters for Playwright](#why-this-matters-for-playwright)
6. [Practice Exercises](#practice-exercises)

## For Loops

For loops allow you to iterate over sequences (lists, strings, ranges) and execute code for each item.

### Key Concepts:
- **Iterating over lists**: Loop through multiple items
- **Iterating over strings**: Access each character
- **Iterating over ranges**: Repeat actions a specific number of times
- **Loop variable**: Access current item in each iteration
- **Nested loops**: Loops inside other loops

See `examples/01_for_loops.py` for code examples.

## While Loops

While loops repeat code as long as a condition remains true - useful when you don't know how many iterations you need.

### Key Concepts:
- **Condition-based looping**: Continue until a condition is false
- **Loop counters**: Track iterations
- **Infinite loops**: Understanding and avoiding them
- **User input loops**: Repeat until valid input received
- **State-based loops**: Continue based on program state

See `examples/02_while_loops.py` for code examples.

## The range() Function

The `range()` function generates sequences of numbers, perfect for controlling loop iterations.

### Key Concepts:
- **range(stop)**: Generate numbers from 0 to stop-1
- **range(start, stop)**: Generate numbers from start to stop-1
- **range(start, stop, step)**: Generate numbers with custom increments
- **Using range with for loops**: Control iteration count
- **Counting backwards**: Negative step values

See `examples/03_break_continue_range.py` for code examples.

## Break and Continue

Control statements that let you modify loop behavior during execution.

### Key Concepts:
- **break**: Exit the loop immediately
- **continue**: Skip to the next iteration
- **Early termination**: Stop when you find what you need
- **Skipping items**: Process only specific items
- **Search patterns**: Find items and exit

See `examples/03_break_continue_range.py` for code examples.

## Why This Matters for Playwright

Loops are fundamental to web automation - you'll use them constantly in real-world testing scenarios.

### Loop Skills in Automation:
- **Iterating through elements**: Process multiple buttons, links, or form fields
- **Filling multiple forms**: Submit data for multiple users or test cases
- **Data-driven testing**: Run the same test with different data sets
- **Waiting strategies**: Retry actions until they succeed
- **Batch operations**: Perform actions on multiple pages

### Common Automation Patterns:
- **Finding elements**: Loop through search results to find specific items
- **Validating lists**: Check that all items in a list meet criteria
- **Form automation**: Fill multiple fields or submit multiple forms
- **Table processing**: Extract or validate data from tables
- **Navigation**: Visit multiple pages in sequence

See `examples/04_playwright_examples.py` for practical automation examples.

## Practice Exercises

Complete the exercises in the `exercises/` folder to reinforce what you've learned:
- `exercise_01_loop_practice.py` - For and while loop challenges
- `exercise_02_loops_and_logic.py` - Combining loops with conditionals
- `exercise_03_playwright_scenarios.py` - Automation-focused exercises

Solutions are available in `exercises/SOLUTIONS.md`.

## Running Your Code

```bash
# Run any Python file
python filename.py

# Or
python3 filename.py
```

## Next Steps

After completing this lecture, you should be comfortable with:
- Using for loops to iterate over sequences
- Using while loops for condition-based repetition
- Generating number sequences with range()
- Controlling loop flow with break and continue
- Understanding how loops enable powerful automation patterns

Move on to Lecture 4 when you're ready!
