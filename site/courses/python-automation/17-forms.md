# Lecture 17: Form Handling

Робота з формами.

<div class="lecture-resources">

[🎬 Презентація](/presentations/Lecture_17_Form_Handling/presentation.html) |
[💻 Приклади](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_17_Form_Handling/examples) |
[📝 Вправи](https://github.com/opyrohov/python_automation_courses/tree/main/Lecture_17_Form_Handling/exercises)

</div>

## Input поля

```python
# Заповнення (очищує перед введенням)
page.get_by_label("Email").fill("user@test.com")

# Посимвольне введення
page.get_by_label("Search").type("query", delay=100)

# Очищення
page.get_by_label("Email").clear()
```

## Checkbox та Radio

```python
# Checkbox
page.get_by_label("Remember me").check()
page.get_by_label("Remember me").uncheck()

# Перевірка стану
is_checked = page.get_by_label("Remember me").is_checked()

# Radio
page.get_by_label("Option A").check()
```

## Select (Dropdown)

```python
# По значенню
page.get_by_label("Country").select_option("ua")

# По тексту
page.get_by_label("Country").select_option(label="Ukraine")

# По індексу
page.get_by_label("Country").select_option(index=2)

# Множинний вибір
page.locator("select").select_option(["opt1", "opt2"])
```

## File Upload

```python
# Один файл
page.get_by_label("Upload").set_input_files("file.pdf")

# Кілька файлів
page.get_by_label("Upload").set_input_files(["file1.pdf", "file2.pdf"])

# Очищення
page.get_by_label("Upload").set_input_files([])
```

## Форма повністю

```python
def fill_registration_form(page):
    page.get_by_label("Name").fill("John Doe")
    page.get_by_label("Email").fill("john@example.com")
    page.get_by_label("Password").fill("SecurePass123")
    page.get_by_label("Country").select_option("ua")
    page.get_by_label("I agree").check()
    page.get_by_role("button", name="Register").click()
```
