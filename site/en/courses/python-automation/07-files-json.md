# Lecture 7: Working with Files and JSON

Working with files and JSON in Python.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_7_File_Handling_JSON/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_7_File_Handling_JSON/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_7_File_Handling_JSON/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- Reading and writing files
- Context manager (with)
- Working with JSON
- Working with CSV

## Reading Files

```python
# Reading the entire file
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Reading line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Reading all lines into a list
with open("file.txt", "r") as f:
    lines = f.readlines()
```

## Writing Files

```python
# Write (overwrites the file)
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")

# Append to a file
with open("output.txt", "a") as f:
    f.write("New line\n")

# Write a list of lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

## JSON

```python
import json

# Reading JSON
with open("data.json", "r") as f:
    data = json.load(f)

# Writing JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# JSON string
json_str = json.dumps({"name": "John"})
data = json.loads('{"name": "John"}')
```

## Path (pathlib)

```python
from pathlib import Path

# Creating a path
path = Path("data/users.json")

# Checks
path.exists()
path.is_file()
path.is_dir()

# Reading/writing
content = path.read_text()
path.write_text("content")

# Creating directories
Path("data/reports").mkdir(parents=True, exist_ok=True)
```
