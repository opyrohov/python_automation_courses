# Lecture 8: Error Handling and Debugging

Error handling and debugging.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_8_Error_Handling_Debugging/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_8_Error_Handling_Debugging/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_8_Error_Handling_Debugging/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- try/except/finally
- Exception types
- Custom exceptions
- Debugging

## try/except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Success!")
finally:
    print("Always runs")
```

## Exception Types

```python
# ValueError
int("not a number")

# KeyError
d = {"a": 1}
d["b"]

# IndexError
lst = [1, 2, 3]
lst[10]

# FileNotFoundError
open("nonexistent.txt")

# TypeError
"2" + 2
```

## Custom Exceptions

```python
class ValidationError(Exception):
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(self.message)

def validate_email(email):
    if "@" not in email:
        raise ValidationError("Invalid email", field="email")

try:
    validate_email("invalid")
except ValidationError as e:
    print(f"Error in {e.field}: {e.message}")
```

## Debugging

```python
# Print debugging
print(f"DEBUG: value = {value}")

# Breakpoint (Python 3.7+)
breakpoint()

# Assert
assert value > 0, "Value must be positive"

# Logging
import logging
logging.debug("Debug message")
logging.info("Info message")
logging.error("Error message")
```
