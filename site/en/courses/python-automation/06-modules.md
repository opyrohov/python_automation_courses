# Lecture 6: Modules and Imports

Modules and imports in Python.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_6_Modules_Imports/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_6_Modules_Imports/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_6_Modules_Imports/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- Importing modules
- Creating your own modules
- Packages
- Virtual environments
- pip and requirements.txt

## Importing Modules

```python
# Import the entire module
import math
result = math.sqrt(16)  # 4.0

# Import with an alias
import numpy as np
arr = np.array([1, 2, 3])

# Import specific functions
from math import sqrt, pi
result = sqrt(16)

# Import everything (not recommended)
from math import *
```

## Standard Modules

```python
# os - working with the OS
import os
current_dir = os.getcwd()
os.makedirs("new_folder", exist_ok=True)
files = os.listdir(".")

# datetime - dates and time
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)

# json - working with JSON
import json
data = json.loads('{"name": "John"}')
text = json.dumps(data, indent=2)

# random - random numbers
import random
random.randint(1, 10)
random.choice(["a", "b", "c"])
random.shuffle(my_list)

# re - regular expressions
import re
pattern = r"\d+"
matches = re.findall(pattern, "abc123def456")
```

## Creating a Module

```python
# my_module.py
"""My own module."""

PI = 3.14159

def greet(name: str) -> str:
    """Greeting."""
    return f"Hello, {name}!"

class Calculator:
    def add(self, a, b):
        return a + b

# Usage
# main.py
from my_module import greet, Calculator

print(greet("World"))
calc = Calculator()
```

## Packages

```
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

```python
# __init__.py
from .module1 import function1
from .module2 import function2

# Usage
from my_package import function1
from my_package.subpackage import module3
```

## Virtual Environments

```bash
# Creation
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Deactivate
deactivate
```

## pip and requirements.txt

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.28.0

# List installed packages
pip list
pip freeze

# Save dependencies
pip freeze > requirements.txt

# Install from file
pip install -r requirements.txt
```

## requirements.txt

```txt
requests==2.28.0
playwright>=1.40.0
pytest>=7.0.0
python-dotenv~=1.0.0
```

## if __name__ == "__main__"

```python
# my_module.py
def main():
    print("Running as main script")

def helper():
    print("Helper function")

# Runs only when executed directly
if __name__ == "__main__":
    main()
```

## Exercises

::: tip Exercise 1
Create a module with string utility functions.
:::

::: tip Exercise 2
Organize code into a package with submodules.
:::

[Code examples on GitHub](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_6_Modules_Imports/examples)
