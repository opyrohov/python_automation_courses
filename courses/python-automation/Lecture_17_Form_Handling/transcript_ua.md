# Лекція 17: Робота з формами

**Курс автоматизації Python + Playwright**

---

## Слайд 1: Титульний

# Лекція 17
## Робота з формами

Курс автоматизації Python + Playwright

---

## Слайд 2: Що ви дізнаєтесь сьогодні

- Заповнювати поля вводу (fill vs type)
- Працювати з чекбоксами та радіо-кнопками
- Обробляти випадаючі списки
- Завантажувати файли програмно
- Відправляти форми та перевіряти результати
- Обробляти складні сценарії форм
- Застосовувати найкращі практики тестування форм

---

## Слайд 3: Чому робота з формами критично важлива

**Форми скрізь!** Логін, реєстрація, оформлення замовлення, пошук, налаштування — опанування автоматизації форм є необхідним.

### Поширені елементи форм:

**Текстові поля:**
- Текстові поля
- Email, пароль
- Числа, дати
- Textarea

**Вибір:**
- Чекбокси
- Радіо-кнопки
- Випадаючі списки
- Множинний вибір

**Дії:**
- Кнопки відправки
- Кнопки скидання
- Скасування/Закриття

**Спеціальні:**
- Завантаження файлів
- Вибір кольору
- Слайдери діапазону
- Вибір дати

---

## Слайд 4: Частина 1 — Текстові поля вводу

# Частина 1
## Текстові поля вводу

fill() vs type()

---

## Слайд 5: fill() - Швидкий ввід тексту

**fill()** встановлює значення поля миттєво — рекомендований спосіб для більшості сценаріїв.

```python
# Базове використання
page.locator("#email").fill("user@example.com")
page.locator("#password").fill("SecurePass123")

# Спочатку очищує існуюче значення
page.locator("#search").fill("новий пошуковий запит")

# Працює з get_by_* локаторами
page.get_by_label("Username").fill("john_doe")
```

**✅ Використовуйте fill() коли:** Вам потрібен швидкий, надійний ввід (99% випадків)

---

## Слайд 6: type() - Посимвольний ввід

**type()** симулює введення кожного символу один за одним — використовуйте для особливих випадків.

```python
# Вводить символ за символом
page.locator("#search").type("Python автоматизація")

# З затримкою між натисканнями (в мілісекундах)
page.locator("#search").type("повільний ввід", delay=100)

# Корисно для тестування автозаповнення
page.locator("#autocomplete").type("Pla")
# Чекаємо появи підказок
page.get_by_text("Playwright").click()
```

**⚠️ Використовуйте type() коли:** Тестуєте автозаповнення, події натискань клавіш або поля з обмеженою швидкістю вводу

---

## Слайд 7: fill() vs type() - Коли що використовувати?

### ✅ fill() - Рекомендовано

- **Швидкий** - Миттєве встановлення значення
- **Надійний** - Працює стабільно
- **Спочатку очищує** - Замінює існуюче значення
- **Використовуйте для:** Форм логіну, реєстрації, вводу даних

```python
page.locator("#email").fill("user@example.com")
```

### ⚠️ type() - Особливі випадки

- **Повільний** - Вводить кожен символ
- **Реальна симуляція** - Викликає події натискань
- **Налаштовуваний** - Можна додати затримки
- **Використовуйте для:** Автозаповнення, валідації символів

```python
page.locator("#search").type("запит", delay=50)
```

---

## Слайд 8: Найкращі практики для текстових полів

```python
# ✅ ДОБРЕ: Очистити та заповнити
page.locator("#email").fill("user@example.com")

# ✅ ДОБРЕ: Використовуйте мітки коли можливо
page.get_by_label("Email Address").fill("user@example.com")

# ✅ ДОБРЕ: Використовуйте плейсхолдери
page.get_by_placeholder("Введіть ваш email").fill("user@example.com")

# ❌ ПОГАНО: Не використовуйте складні селектори
page.locator("div > div > input:nth-child(3)").fill("text")

# ✅ ДОБРЕ: Перевірте що значення встановлено
page.locator("#email").fill("user@example.com")
assert page.locator("#email").input_value() == "user@example.com"
```

---

## Слайд 9: Частина 2 — Чекбокси та радіо-кнопки

# Частина 2
## Чекбокси та радіо-кнопки

check(), uncheck(), set_checked()

---

## Слайд 10: Робота з чекбоксами

Три методи для взаємодії з чекбоксами:

```python
# Метод 1: check() - Відмітити чекбокс
page.locator("#terms").check()
page.get_by_label("Я приймаю умови").check()

# Метод 2: uncheck() - Зняти відмітку з чекбокса
page.locator("#newsletter").uncheck()

# Метод 3: set_checked(boolean) - Встановити конкретний стан
page.locator("#remember-me").set_checked(True)
page.locator("#remember-me").set_checked(False)

# Перевірити поточний стан
is_checked = page.locator("#terms").is_checked()
print(f"Умови прийнято: {is_checked}")
```

**Порада:** check() та uncheck() є ідемпотентними — безпечно викликати навіть якщо вже в тому стані!

---

## Слайд 11: Робота з радіо-кнопками

Вибір опцій з групи радіо-кнопок:

```python
# Вибір за значенням
page.locator("input[name='payment'][value='credit-card']").check()

# Вибір за міткою
page.get_by_label("Кредитна картка").check()

# Вибір за роллю
page.get_by_role("radio", name="PayPal").check()

# Перевірка вибору
selected = page.locator("input[name='payment']:checked").input_value()
print(f"Обраний метод оплати: {selected}")
```

**Найкраща практика:** Використовуйте get_by_label() або get_by_role() для кращої доступності!

---

## Слайд 12: Реальний приклад чекбоксів та радіо

### HTML:
```html
<input type="checkbox" id="newsletter" />
<label for="newsletter">Підписатися на розсилку</label>

<input type="radio" name="gender" value="male" id="male" />
<label for="male">Чоловік</label>
<input type="radio" name="gender" value="female" id="female" />
<label for="female">Жінка</label>
```

### Код Playwright:
```python
# Чекбокс
page.get_by_label("Підписатися на розсилку").check()

# Радіо-кнопка
page.get_by_label("Жінка").check()

# Перевірка
assert page.locator("#newsletter").is_checked()
assert page.locator("#female").is_checked()
```

---

## Слайд 13: Частина 3 — Випадаючі списки

# Частина 3
## Випадаючі списки

select_option() для елементів <select>

---

## Слайд 14: select_option() - Вибір з випадаючого списку

Кілька способів вибору опцій випадаючого списку:

```python
# Вибір за значенням
page.locator("#country").select_option("us")

# Вибір за міткою (видимий текст)
page.locator("#country").select_option(label="United States")

# Вибір за індексом (з 0)
page.locator("#country").select_option(index=2)

# Вибір кількох опцій (для multi-select)
page.locator("#interests").select_option(["sports", "music", "travel"])
```

**Рекомендація:** Використовуйте label (видимий текст) для кращої читабельності та підтримуваності!

---

## Слайд 15: Приклади вибору з випадаючого списку

```python
# Приклад 1: Одиничний вибір
page.locator("#country").select_option(label="Canada")

# Приклад 2: Множинний вибір
page.locator("#skills").select_option([
    "Python",
    "JavaScript",
    "Playwright"
])

# Приклад 3: Динамічна опція
# Спочатку отримуємо всі опції
options = page.locator("#country option").all_text_contents()
# Вибираємо другу
page.locator("#country").select_option(index=1)

# Приклад 4: Перевірка вибору
selected = page.locator("#country").input_value()
assert selected == "ca", f"Очікувалось 'ca', отримано '{selected}'"
```

---

## Слайд 16: Кастомні випадаючі списки (не Select)

Багато сучасних сайтів використовують div-based випадаючі списки замість `<select>`

```python
# Для кастомних випадаючих списків на div/button
# Крок 1: Клік для відкриття випадаючого списку
page.locator(".dropdown-trigger").click()

# Крок 2: Клік по потрібній опції
page.get_by_text("Опція 2").click()

# Або з ролями
page.get_by_role("button", name="Оберіть країну").click()
page.get_by_role("option", name="United States").click()
```

**Примітка:** select_option() працює тільки з нативними `<select>` елементами!

---

## Слайд 17: Частина 4 — Завантаження файлів

# Частина 4
## Завантаження файлів

set_input_files() для вибору файлів

---

## Слайд 18: set_input_files() - Завантаження файлів

Програмний вибір файлів для завантаження:

```python
# Завантаження одного файлу
page.locator("input[type='file']").set_input_files("document.pdf")

# Завантаження кількох файлів
page.locator("input[type='file']").set_input_files([
    "file1.jpg",
    "file2.png",
    "file3.pdf"
])

# Завантаження з абсолютним шляхом
import os
file_path = os.path.abspath("files/upload.pdf")
page.locator("#file-upload").set_input_files(file_path)

# Очистити вибір файлів
page.locator("input[type='file']").set_input_files([])
```

---

## Слайд 19: Найкращі практики завантаження файлів

```python
from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/upload")

    # Завантажити файл
    file_path = os.path.abspath("document.pdf")
    page.locator("input[type='file']").set_input_files(file_path)

    # Натиснути кнопку завантаження
    page.get_by_role("button", name="Upload").click()

    # Чекати повідомлення про успіх
    page.wait_for_selector(".upload-success")

    # Перевірити
    success_msg = page.locator(".upload-success").text_content()
    assert "uploaded successfully" in success_msg.lower()

    browser.close()
```

---

## Слайд 20: Частина 5 — Відправка форм та валідація

# Частина 5
## Відправка форм та валідація

Відправка форм та перевірка результатів

---

## Слайд 21: Методи відправки форм

```python
# Метод 1: Клік по кнопці відправки (рекомендовано)
page.get_by_role("button", name="Submit").click()

# Метод 2: Натискання Enter в полі вводу
page.locator("#email").fill("user@example.com")
page.locator("#email").press("Enter")

# Метод 3: Виклик form.submit() (JavaScript)
page.locator("form#login").evaluate("form => form.submit()")

# Метод 4: Використання клавіатурного скорочення
page.keyboard.press("Enter")
```

**Найкраща практика:** Клікайте по кнопці відправки — це найбільш реалістично та тестує функціональність кнопки!

---

## Слайд 22: Валідація відправки форми

```python
# Заповнити форму
page.get_by_label("Email").fill("user@example.com")
page.get_by_label("Password").fill("SecurePass123")

# Відправити
page.get_by_role("button", name="Login").click()

# Перевірити успіх (кілька способів)

# 1. Перевірити зміну URL
page.wait_for_url("**/dashboard")
assert "/dashboard" in page.url

# 2. Перевірити наявність елемента успіху
success_banner = page.locator(".success-message")
assert success_banner.is_visible()

# 3. Перевірити текстовий вміст
welcome_msg = page.locator("h1").text_content()
assert "Welcome" in welcome_msg

# 4. Перевірити що помилки НЕ відображаються
assert not page.locator(".error-message").is_visible()
```

---

## Слайд 23: Повний приклад форми реєстрації

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com/register")

    # Текстові поля
    page.get_by_label("Full Name").fill("John Doe")
    page.get_by_label("Email").fill("john@example.com")
    page.get_by_label("Password").fill("SecurePass123")

    # Чекбокс
    page.get_by_label("I accept the terms").check()

    # Радіо-кнопка
    page.get_by_label("Male").check()

    # Випадаючий список
    page.locator("#country").select_option(label="United States")

    # Завантаження файлу
    page.locator("input[type='file']").set_input_files("avatar.jpg")

    # Відправити
    page.get_by_role("button", name="Register").click()

    # Валідація
    page.wait_for_selector(".registration-success")
    assert page.locator(".registration-success").is_visible()

    browser.close()
```

---

## Слайд 24: Тестування помилок валідації форми

```python
# Тест 1: Відправка пустої форми
page.get_by_role("button", name="Submit").click()

# Перевірити появу помилок валідації
email_error = page.locator(".error-email")
assert email_error.is_visible()
assert "required" in email_error.text_content().lower()

# Тест 2: Невалідний формат email
page.get_by_label("Email").fill("not-an-email")
page.get_by_role("button", name="Submit").click()

# Перевірити помилку валідації email
assert "invalid email" in page.locator(".error-email").text_content().lower()

# Тест 3: Занадто короткий пароль
page.get_by_label("Password").fill("123")
page.get_by_role("button", name="Submit").click()

# Перевірити помилку пароля
assert "at least 8 characters" in page.locator(".error-password").text_content().lower()
```

---

## Слайд 25: Найкращі практики роботи з формами

### ✅ РОБІТЬ

- Використовуйте fill() для швидкості
- Використовуйте get_by_label() коли можливо
- Перевіряйте відправку форми
- Тестуйте і успішні, і помилкові сценарії
- Чекайте готовності елементів
- Очищуйте форми між тестами

### ❌ НЕ РОБІТЬ

- Використовувати type() без потреби
- Покладатися на крихкі селектори
- Пропускати перевірки валідації
- Забувати чекати відповіді
- Тестувати тільки "happy path"
- Хардкодити шляхи до файлів

---

## Слайд 26: Спеціальні типи полів

### Date Picker (Вибір дати):
```python
# Формат: YYYY-MM-DD
page.locator("#birthday").fill("1990-06-15")
```

### DateTime Local:
```python
# Формат: YYYY-MM-DDTHH:MM
page.locator("#meeting-time").fill("2024-12-25T14:30")
```

### Range Slider (Слайдер):
```python
# Встановити значення напряму
page.locator("#volume").fill("75")
```

### Color Picker (Вибір кольору):
```python
# Формат: hex color
page.locator("#color").fill("#ff5733")
```

---

## Слайд 27: Підсумок

### Ключові висновки:

- ✅ Використовуйте **fill()** для швидкого вводу тексту (більшість випадків)
- ✅ Використовуйте **type()** тільки для автозаповнення або особливих випадків
- ✅ Використовуйте **check()/uncheck()** для чекбоксів
- ✅ Використовуйте **select_option()** для випадаючих списків
- ✅ Використовуйте **set_input_files()** для завантаження файлів
- ✅ Завжди **валідуйте** результати відправки форми
- ✅ Тестуйте і **успішні, і помилкові** сценарії
- ✅ Використовуйте сучасні локатори (**get_by_label**, **get_by_role**)

---

## Слайд 28: Що далі?

### Наступні теми:
- Розширені взаємодії (Hover, Drag & Drop)
- Стратегії очікування та таймаути
- Assertions та Expectations
- Скріншоти та відео

### Практика:
- Виконайте вправи в папці `exercises/`
- Перегляньте приклади в папці `examples/`
- Прочитайте детальний README.md
- Практикуйтесь на реальних формах реєстрації/логіну

---

## Слайд 29: Фінальний слайд

# Чудова робота!

## Ви опанували роботу з формами!

Практикуйтесь з різними формами для закріплення навичок
