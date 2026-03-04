# Lecture 12: Review and Project Setup

Python summary and project setup.

<div class="lecture-resources">
  <a href="/python_automation_courses/presentations/Lecture_12_Python_Review_Project_Setup/presentation.html" target="_blank">🎬 Presentation</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_12_Python_Review_Project_Setup/examples" target="_blank">💻 Examples</a>
  <a href="https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_12_Python_Review_Project_Setup/exercises" target="_blank">📝 Exercises</a>
</div>

## Lecture Topics

- Phase 1 Summary
- Project structure
- Virtual environments
- Preparing for Playwright

## Project Structure

```
my_project/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
├── .gitignore
├── README.md
└── venv/
```

## Virtual Environment

```bash
# Creation
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## requirements.txt

```
playwright>=1.40.0
pytest>=7.0.0
pytest-playwright>=0.4.0
python-dotenv>=1.0.0
```

## Next Steps

You have completed Phase 1: Python Basics!

Next — Phase 2: Playwright, where you will learn to:
- Automate the browser
- Find elements on the page
- Interact with web applications
- Write E2E tests
