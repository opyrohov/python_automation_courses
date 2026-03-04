# Lecture 3: Loops

Loops in Python — for and while.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_3_Loops/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_3_Loops/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_3_Loops/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- `for` loop
- `while` loop
- `break` and `continue`
- `range()` function
- Nested loops

## for Loop

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Hello":
    print(char)

# With enumerate (index + value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

## range() Function

```python
# range(stop)
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# range(start, stop)
for i in range(2, 5):  # 2, 3, 4
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Reverse order
for i in range(5, 0, -1):  # 5, 4, 3, 2, 1
    print(i)
```

## while Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1

# while with exit condition
while True:
    answer = input("Continue? (y/n): ")
    if answer == "n":
        break
```

## break and continue

```python
# break - exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
```

## else in Loops

```python
# else executes if the loop completed without break
for i in range(5):
    if i == 10:  # never True
        break
else:
    print("Loop completed normally")
```

## Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")
```

## List Comprehension

```python
# Regular loop
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(5)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i * j for j in range(3)] for i in range(3)]
```

## Exercises

::: tip Exercise 1
Write a program to print the multiplication table from 1 to 10.
:::

::: tip Exercise 2
Find the sum of all numbers from 1 to 100 that are divisible by 3 or 5.
:::

[Code examples on GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_3_Loops/examples)
