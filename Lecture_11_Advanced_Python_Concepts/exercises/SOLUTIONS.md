# Exercise Solutions - Lecture 11

This file contains sample solutions for the exercises. Try to complete the exercises on your own first before checking these solutions!

## Exercise 1: Comprehensions

### Task 1: Basic List Comprehension
```python
squares = [x ** 2 for x in range(1, 11)]
```

### Task 2: List Comprehension with Condition
```python
evens = [x for x in range(1, 21) if x % 2 == 0]
```

### Task 3: List Comprehension with If-Else
```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 11)]
```

### Task 4: Transform Strings
```python
uppercase_names = [name.upper() for name in names]
```

### Task 5: Filter and Transform
```python
long_word_lengths = [len(word) for word in words if len(word) > 3]
```

### Task 6: Nested List Comprehension
```python
flattened = [num for row in matrix for num in row]
```

### Task 7: Dictionary Comprehension
```python
cubes_dict = {x: x ** 3 for x in range(1, 6)}
```

### Task 8: Dictionary from Two Lists
```python
person = {k: v for k, v in zip(keys, values)}
```

### Task 9: Filter Dictionary
```python
high_scores = {name: score for name, score in scores.items() if score > 50}
```

### Task 10: Test Data Generation
```python
test_users = [{"id": i, "email": f"user{i}@test.com"} for i in range(1, 6)]
```

### Bonus: Extract File Extensions
```python
extensions = {filename.split('.')[-1] for filename in filenames}
```

---

## Exercise 2: *args, **kwargs, and Decorators

### Task 1: Function with *args
```python
def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)
```

### Task 2: Function with **kwargs
```python
def build_query(**kwargs):
    return "&".join(f"{key}={value}" for key, value in kwargs.items())
```

### Task 3: Combining Regular Params with *args
```python
def greet_all(greeting, *names):
    return [f"{greeting}, {name}!" for name in names]
```

### Task 4: Combining *args and **kwargs
```python
def format_message(template, *args, **kwargs):
    result = template
    # Apply positional arguments
    for i, arg in enumerate(args):
        result = result.replace(f"{{{i}}}", str(arg))
    # Apply keyword arguments
    for key, value in kwargs.items():
        result = result.replace(f"{{{key}}}", str(value))
    return result
```

### Task 5: Simple Decorator
```python
def print_wrapper(func):
    def wrapper(*args, **kwargs):
        print("START")
        result = func(*args, **kwargs)
        print("END")
        return result
    return wrapper
```

### Task 6: Decorator with Arguments
```python
def log_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper
```

### Task 7: Timing Decorator
```python
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"{func.__name__} took {duration:.4f} seconds")
        return result
    return wrapper
```

### Task 8: Decorator with Parameters
```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator
```

### Task 9: Validation Decorator
```python
def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check all positional arguments
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative value not allowed: {arg}")
        # Check all keyword arguments
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"Negative value not allowed for {key}: {value}")
        return func(*args, **kwargs)
    return wrapper
```

### Bonus: Cache Decorator
```python
def cache(func):
    cached_results = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"  Cache hit for {args}")
            return cached_results[args]
        print(f"  Cache miss for {args}")
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper
```

---

## Exercise 3: Datetime and String Methods

### Task 1: Format Current Date
```python
formatted_date = now.strftime("%B %d, %Y")
```

### Task 2: Parse Date String
```python
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
```

### Task 3: Date Arithmetic
```python
future_date = today + timedelta(days=30)
```

### Task 4: Calculate Age
```python
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
```

### Task 5: Compare Dates
```python
is_future = event_date > current
```

### Task 6: String Split
```python
fields = csv_line.split(',')
```

### Task 7: String Join
```python
joined = "-".join(words)
```

### Task 8: String Strip
```python
cleaned = user_input.strip()
```

### Task 9: String Replace
```python
replaced = text.replace(" ", "_")
```

### Task 10: Check Prefix/Suffix
```python
starts_with_test = filename.startswith("test_")
ends_with_py = filename.endswith(".py")
```

### Task 11: Extract Domain
```python
domain = email.split('@')[1]
```

### Task 12: Case Conversion
```python
uppercase = text.upper()
lowercase = text.lower()
```

### Task 13: Count Occurrences
```python
count = text.count("test")
```

### Task 14: Build URL
```python
url = f"{base}/{endpoint}/{user_id}"
# or
url = "/".join([base, endpoint, user_id])
```

### Bonus: Timestamp Filename
```python
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename_with_timestamp = f"screenshot_{timestamp}.png"
```

---

## Exercise 4: Automation Helpers

### Task 1: Test Data Generator
```python
def generate_test_users(count, domain="test.com"):
    base_date = datetime.now().date()
    return [
        {
            "id": i,
            "username": f"user{i}",
            "email": f"user{i}@{domain}",
            "created_date": (base_date - timedelta(days=i-1)).strftime("%Y-%m-%d")
        }
        for i in range(1, count + 1)
    ]
```

### Task 2: Flexible Element Checker
```python
def check_elements(*selectors, **options):
    timeout = options.get("timeout", 5)
    visible = options.get("visible", True)

    print(f"Checking {len(selectors)} elements (timeout={timeout}s, visible={visible}):")
    for selector in selectors:
        print(f"  ✓ '{selector}' check passed")
    return True
```

### Task 3: Retry Decorator
```python
def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"Attempt {attempt}/{max_attempts}")
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"  Failed: {e}, retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator
```

### Task 4: Screenshot Helper
```python
def generate_screenshot_name(test_name, *tags, **options):
    include_timestamp = options.get("include_timestamp", True)

    parts = [test_name]
    parts.extend(tags)

    if include_timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        parts.append(timestamp)

    return "_".join(parts) + ".png"
```

### Task 5: Filter Test Data
```python
def filter_test_data(data, **conditions):
    return [
        item for item in data
        if all(item.get(key) == value for key, value in conditions.items())
    ]
```

### Task 6: Build Selector
```python
def build_selector(element, **attributes):
    selector = element
    for key, value in attributes.items():
        # Convert underscores to hyphens for attribute names
        attr_name = key.replace("_", "-")
        selector += f"[{attr_name}='{value}']"
    return selector
```

### Task 7: Parse Test Results
```python
def parse_test_results(result_strings):
    total = len(result_strings)
    passed = 0
    failed = 0
    total_duration = 0.0

    for result in result_strings:
        if "PASSED" in result:
            passed += 1
        elif "FAILED" in result:
            failed += 1

        # Extract duration from "(2.5s)" pattern
        duration_str = result.split('(')[1].split('s')[0]
        total_duration += float(duration_str)

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "total_duration": total_duration
    }
```

### Task 8: Date Range Generator
```python
def generate_date_range(start_date, days, date_format="%Y-%m-%d"):
    return [
        (start_date + timedelta(days=i)).strftime(date_format)
        for i in range(days)
    ]
```

### Task 9: Clean and Validate URLs
```python
def clean_and_validate_urls(urls):
    valid = []
    invalid = []

    for url in urls:
        cleaned = url.strip().lower()
        if cleaned.startswith("http://") or cleaned.startswith("https://"):
            valid.append(cleaned)
        else:
            invalid.append(cleaned)

    return {"valid": valid, "invalid": invalid}
```

### Bonus: Test Report Generator
```python
def generate_test_report(test_results, **metadata):
    lines = []

    # Header
    lines.append("=" * 60)
    lines.append("TEST EXECUTION REPORT")
    lines.append("=" * 60)
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # Metadata
    if metadata:
        lines.append("Test Environment:")
        for key, value in metadata.items():
            lines.append(f"  {key.title()}: {value}")
        lines.append("")

    # Summary
    total = len(test_results)
    passed = sum(1 for t in test_results if t["status"] == "passed")
    failed = total - passed
    total_duration = sum(t["duration"] for t in test_results)

    lines.append("Summary:")
    lines.append(f"  Total Tests: {total}")
    lines.append(f"  Passed: {passed}")
    lines.append(f"  Failed: {failed}")
    lines.append(f"  Total Duration: {total_duration:.2f}s")
    lines.append("")

    # Individual results
    lines.append("Test Results:")
    for test in test_results:
        status_symbol = "✓" if test["status"] == "passed" else "✗"
        lines.append(f"  {status_symbol} {test['name']}: {test['status'].upper()} ({test['duration']}s)")

    lines.append("=" * 60)

    return "\n".join(lines)
```

---

## Tips for Success

1. **Practice, practice, practice** - These concepts become natural with repetition
2. **Understand the patterns** - Don't just memorize, understand when to use each technique
3. **Combine concepts** - Real-world code often uses multiple concepts together
4. **Read error messages** - They usually tell you exactly what's wrong
5. **Experiment** - Try variations to see how they work
6. **Use in real projects** - Apply these in your test automation code

## Common Mistakes to Avoid

1. **Comprehensions**: Don't make them too complex - readability matters
2. ***args/**kwargs**: Remember the order: regular, *args, default, **kwargs
3. **Decorators**: Always use @functools.wraps to preserve function metadata
4. **Datetime**: Pay attention to timezone issues in production code
5. **String methods**: Most return new strings, they don't modify the original

## Next Steps

After mastering these concepts:
- Apply them in your Playwright tests
- Build your own utility library
- Share patterns with your team
- Look into more advanced Python features (context managers, generators, etc.)
