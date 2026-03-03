# Lecture 12: Python Review & Project Setup

Підсумок Python та налаштування проекту.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_12_Python_Review_Project_Setup/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_12_Python_Review_Project_Setup/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/courses/python-automation/Lecture_12_Python_Review_Project_Setup/exercises)

</div>

## Теми лекції

- Підсумок Phase 1
- Структура проекту
- Віртуальні середовища
- Підготовка до Playwright

## Структура проекту

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

## Віртуальне середовище

```bash
# Створення
python -m venv venv

# Активація (Windows)
venv\Scripts\activate

# Активація (Mac/Linux)
source venv/bin/activate

# Встановлення залежностей
pip install -r requirements.txt
```

## requirements.txt

```
playwright>=1.40.0
pytest>=7.0.0
pytest-playwright>=0.4.0
python-dotenv>=1.0.0
```

## Наступні кроки

Ви завершили Phase 1: Python Basics!

Далі — Phase 2: Playwright, де ви навчитесь:
- Автоматизувати браузер
- Знаходити елементи на сторінці
- Взаємодіяти з веб-застосунками
- Писати E2E тести
