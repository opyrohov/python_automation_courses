# Lecture 8: Error Handling & Debugging

Обробка помилок та налагодження.

<div class="lecture-resources">

<a href="/presentations/Lecture_8_Error_Handling_Debugging/presentation.html" target="_blank">🎬 Презентація</a> |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_8_Error_Handling_Debugging/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_8_Error_Handling_Debugging/exercises)

</div>

## Теми лекції

- try/except/finally
- Типи винятків
- Власні винятки
- Налагодження (debugging)

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

## Типи винятків

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

## Власні винятки

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
