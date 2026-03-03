# Лекція 15: Стратегії локаторів (Частина 1)

**Курс автоматизації Python + Playwright**

---

## Слайд 1: Титульний

# Лекція 15
## Стратегії локаторів (Частина 1)

Курс автоматизації Python + Playwright

---

## Слайд 2: Що ви дізнаєтесь сьогодні

- Опануєте CSS селектори (id, class, атрибути)
- Зрозумієте основи XPath та коли їх використовувати
- Використовуватимете сучасні текстові локатори Playwright
- Застосовуватимете локатори на основі ролей та міток
- Застосуєте найкращі практики вибору локаторів
- Будуватимете стійкі та підтримувані тестові селектори
- Уникатимете поширених помилок з локаторами

---

## Слайд 3: Чому локатори важливі

**Локатори** — це спосіб знаходження елементів на веб-сторінці. Вони є основою всієї автоматизації браузера!

### Вплив хороших та поганих локаторів:

**Хороші локатори:**
- Тести виконуються надійно
- Легко підтримувати
- Зрозумілі та читабельні
- Стійкі до змін

**Погані локатори:**
- Нестабільні тестові збої
- Важко налагоджувати
- Ламаються при змінах UI
- Важко зрозуміти

---

## Слайд 4: Огляд стратегій локаторів

### CSS Селектори
- ID селектори
- Class селектори
- Атрибутні селектори
- Комбінатори

### XPath
- Абсолютні шляхи
- Відносні шляхи
- Текстовий XPath
- Навігація по осях

### Сучасні локатори Playwright
- get_by_role
- get_by_text
- get_by_label
- get_by_placeholder

### Найкращі практики
- Віддавайте перевагу атрибутам, орієнтованим на користувача
- Уникайте крихких селекторів
- Використовуйте test ID за потреби
- Тримайте селектори простими

---

## Слайд 5: Частина 1 — CSS Селектори

# Частина 1
## CSS Селектори

Найпоширеніший спосіб знаходження елементів

---

## Слайд 6: CSS Селектори: Основи

**CSS Селектори** — це ті самі селектори, які ви використовуєте в CSS таблицях стилів. Вони швидкі, читабельні та широко підтримуються.

### Поширені типи CSS селекторів:

- **#id** - Вибір за ID
- **.class** - Вибір за назвою класу
- **tag** - Вибір за HTML тегом
- **[attribute]** - Вибір за атрибутом
- **parent > child** - Комбінатор прямого нащадка
- **ancestor descendant** - Комбінатор нащадка

---

## Слайд 7: ID Селектори - #id

**Найкраща практика:** ID повинні бути унікальними на сторінці, що робить їх найнадійнішим селектором!

### HTML приклад:
```html
<button id="submit-btn">Submit</button>
<input id="username" type="text">
```

### Код Playwright:
```python
# Використання CSS селектора з ID
page.locator("#submit-btn").click()
page.locator("#username").fill("john_doe")

# Альтернативно, використовуйте get_by_test_id для тестових ID
page.get_by_test_id("submit-button").click()
```

---

## Слайд 8: Class Селектори - .class

**Увага:** Класи можуть з'являтися кілька разів на сторінці. Будьте конкретними!

### HTML приклад:
```html
<button class="btn btn-primary">Login</button>
<button class="btn btn-secondary">Cancel</button>
```

### Код Playwright:
```python
# Один клас
page.locator(".btn-primary").click()

# Кілька класів (елемент повинен мати обидва)
page.locator(".btn.btn-primary").click()

# Будьте конкретними щоб уникнути неоднозначності
page.locator("button.btn-primary").click()
```

---

## Слайд 9: Атрибутні Селектори - [attribute]

Вибір елементів на основі будь-якого атрибуту та його значення.

### Варіації синтаксису:
```python
# Має атрибут (будь-яке значення)
page.locator("[data-testid]")

# Точне співпадіння
page.locator("[type='submit']")

# Містить значення
page.locator("[class*='btn']")

# Починається зі значення
page.locator("[href^='https']")

# Закінчується значенням
page.locator("[src$='.png']")
```

---

## Слайд 10: Атрибутні Селектори: Реальний приклад

### HTML:
```html
<button type="submit" data-action="login">Login</button>
<input type="email" name="userEmail" placeholder="Email">
<a href="https://example.com/docs">Documentation</a>
```

### Код Playwright:
```python
# Вибір за типом
page.locator("[type='submit']").click()

# Вибір за data атрибутом
page.locator("[data-action='login']").click()

# Вибір за name
page.locator("[name='userEmail']").fill("user@example.com")

# Вибір посилань на конкретний домен
page.locator("[href^='https://example.com']").click()
```

---

## Слайд 11: Комбінування CSS Селекторів

Комбінуйте селектори для більш точного націлювання

### Поширені комбінації:
```python
# Тег + клас
page.locator("button.btn-primary")

# Тег + ID
page.locator("input#username")

# Тег + атрибут
page.locator("button[type='submit']")

# Кілька атрибутів
page.locator("input[type='text'][name='search']")

# Клас + атрибут
page.locator(".form-control[placeholder='Email']")
```

---

## Слайд 12: CSS Комбінатори

Навігація зв'язків між елементами

### Типи комбінаторів:
```python
# Нащадок (пробіл) - будь-який рівень нижче
page.locator("div.container button")

# Прямий нащадок (>) - тільки безпосередні діти
page.locator("form > button")

# Сусідній сиблінг (+) - безпосередньо після
page.locator("label + input")

# Загальний сиблінг (~) - будь-який сиблінг після
page.locator("h2 ~ p")
```

---

## Слайд 13: Приклад Комбінатора

### HTML Структура:
```html
<div class="login-form">
  <form>
    <label>Email</label>
    <input type="email" name="email">
    <button type="submit">Login</button>
  </form>
</div>
```

### Код Playwright:
```python
# Кнопка всередині форми логіну
page.locator(".login-form button").click()

# Пряма дочірня кнопка форми
page.locator("form > button").click()

# Input що йде після label
page.locator("label + input").fill("test@example.com")
```

---

## Слайд 14: Частина 2 — Основи XPath

# Частина 2
## Основи XPath

Потужний, але використовуйте обережно

---

## Слайд 15: Що таке XPath?

**XPath** (XML Path Language) — це мова запитів для вибору вузлів у XML/HTML документі.

### Коли використовувати XPath:
- Коли CSS селектори не можуть виразити зв'язок
- Навігація вгору по DOM дереву (до батька)
- Складне співпадіння тексту
- Вибір за позицією

**Примітка:** XPath може бути повільнішим за CSS та важчим для читання. Використовуйте його коли необхідно, але віддавайте перевагу CSS та сучасним локаторам Playwright коли можливо.

---

## Слайд 16: Синтаксис XPath

### Абсолютні vs Відносні шляхи:
```python
# Абсолютний шлях (починається з кореня) - УНИКАЙТЕ!
page.locator("xpath=/html/body/div/form/button")

# Відносний шлях (починається з //) - ПЕРЕВАГА
page.locator("xpath=//button[@type='submit']")
```

**Ніколи не використовуйте абсолютні шляхи!** Вони ламаються при будь-якій зміні DOM.

---

## Слайд 17: Поширені Паттерни XPath

```python
# Вибір за тегом
page.locator("xpath=//button")

# Вибір за атрибутом
page.locator("xpath=//button[@type='submit']")

# Вибір за ID
page.locator("xpath=//*[@id='submit-btn']")

# Вибір за класом
page.locator("xpath=//button[@class='btn-primary']")

# Містить клас (для кількох класів)
page.locator("xpath=//button[contains(@class, 'btn-primary')]")

# Вибір за текстовим вмістом
page.locator("xpath=//button[text()='Login']")
```

---

## Слайд 18: XPath: Співпадіння Тексту

XPath чудово підходить для пошуку елементів за їхнім текстовим вмістом

```python
# Точне співпадіння тексту
page.locator("xpath=//button[text()='Login']")

# Містить текст
page.locator("xpath=//div[contains(text(), 'Welcome')]")

# Починається з тексту
page.locator("xpath=//h1[starts-with(text(), 'Chapter')]")

# Без урахування регістру (використовуючи translate)
page.locator("xpath=//button[contains(translate(text(), 'LOGIN', 'login'), 'login')]")
```

**Порада:** `get_by_text()` Playwright зазвичай краще за XPath для співпадіння тексту!

---

## Слайд 19: Осі XPath: Навігація

Навігація зв'язків у DOM дереві

```python
# Батько
page.locator("xpath=//button[@id='submit']/parent::form")

# Предок
page.locator("xpath=//button[@id='submit']/ancestor::div")

# Наступний сиблінг
page.locator("xpath=//label[text()='Email']/following-sibling::input")

# Попередній сиблінг
page.locator("xpath=//input[@name='email']/preceding-sibling::label")

# Дитина
page.locator("xpath=//form/child::button")
```

---

## Слайд 20: XPath: Реальний Приклад

### HTML:
```html
<div class="product-card">
  <h3>Laptop</h3>
  <p class="price">$999</p>
  <button class="add-to-cart">Add to Cart</button>
</div>
```

### Код Playwright:
```python
# Знайти кнопку в картці продукту з конкретною назвою
page.locator("xpath=//div[.//h3[text()='Laptop']]//button[@class='add-to-cart']").click()

# Отримати ціну продукту з назвою Laptop
price = page.locator("xpath=//div[.//h3[text()='Laptop']]//p[@class='price']").text_content()
print(price)  # $999
```

---

## Слайд 21: Частина 3 — Сучасні Локатори Playwright

# Частина 3
## Сучасні Локатори Playwright

Рекомендований спосіб знаходження елементів

---

## Слайд 22: Чому використовувати сучасні локатори Playwright?

**Сучасні локатори** орієнтовані на користувача та доступні — вони працюють так, як користувачі взаємодіють з вашим додатком!

### Переваги:
- Більш стійкі до змін DOM
- Краще тестування доступності
- Самодокументований код
- Автоочікування та автоповтор
- Кращі повідомлення про помилки

**Рекомендація Playwright:** Завжди віддавайте перевагу сучасним локаторам перед CSS/XPath коли можливо!

---

## Слайд 23: get_by_role() - Найкращий Локатор

**Рекомендовано:** Це стратегія локаторів #1 від Playwright!

### Поширені ролі:
```python
# Кнопки
page.get_by_role("button", name="Login").click()

# Посилання
page.get_by_role("link", name="Contact Us").click()

# Текстові поля
page.get_by_role("textbox", name="Email").fill("test@example.com")

# Чекбокси
page.get_by_role("checkbox", name="Accept terms").check()

# Заголовки
expect(page.get_by_role("heading", name="Welcome")).to_be_visible()
```

---

## Слайд 24: get_by_role() - Поширені ARIA Ролі

```python
# Навігація
page.get_by_role("navigation")

# Основний вміст
page.get_by_role("main")

# Радіо кнопки
page.get_by_role("radio", name="Option A").click()

# Комбобокс (випадаючий список)
page.get_by_role("combobox").select_option("value")

# Елементи списку
page.get_by_role("listitem").filter(has_text="Item 1")

# Таблиці
page.get_by_role("table")
page.get_by_role("row")
page.get_by_role("cell")
```

---

## Слайд 25: get_by_text() - Пошук за Видимим Текстом

Знаходження елементів за їхнім текстовим вмістом

```python
# Точне співпадіння (за замовчуванням)
page.get_by_text("Login").click()

# Часткове співпадіння
page.get_by_text("Welcome", exact=False).is_visible()

# Чутливий до регістру за замовчуванням
page.get_by_text("LOGIN")  # Не співпаде з "Login"

# Пошук у конкретному контейнері
page.locator(".sidebar").get_by_text("Settings").click()
```

**Випадок використання:** Чудово підходить для кліків по посиланнях, пошуку заголовків або перевірки текстового вмісту!

---

## Слайд 26: get_by_label() - Пошук Полів Форми за Міткою

Знаходження полів форми за пов'язаним текстом мітки

### HTML приклад:
```html
<label for="email">Email Address</label>
<input id="email" type="email">

<label>
  Password
  <input type="password">
</label>
```

### Код Playwright:
```python
# Працює з явними та неявними мітками
page.get_by_label("Email Address").fill("user@example.com")
page.get_by_label("Password").fill("secret123")

# Часткове співпадіння
page.get_by_label("Email", exact=False).fill("user@example.com")
```

---

## Слайд 27: get_by_placeholder() - Пошук за Плейсхолдером

Знаходження полів вводу за текстом плейсхолдера

### HTML приклад:
```html
<input type="text" placeholder="Search products...">
<input type="email" placeholder="Enter your email">
```

### Код Playwright:
```python
# Точне співпадіння
page.get_by_placeholder("Search products...").fill("laptop")

# Часткове співпадіння
page.get_by_placeholder("email", exact=False).fill("user@example.com")
```

**Примітка:** Віддавайте перевагу `get_by_label()` перед placeholder коли можливо — це більш доступно!

---

## Слайд 28: get_by_alt_text() - Пошук Зображень

Знаходження зображень за їхнім alt текстом

### HTML приклад:
```html
<img src="logo.png" alt="Company Logo">
<img src="profile.jpg" alt="User profile picture">
```

### Код Playwright:
```python
# Клік по зображенню (якщо воно клікабельне)
page.get_by_alt_text("Company Logo").click()

# Перевірка що зображення видиме
expect(page.get_by_alt_text("User profile picture")).to_be_visible()

# Часткове співпадіння
page.get_by_alt_text("profile", exact=False)
```

---

## Слайд 29: get_by_title() - Пошук за Атрибутом Title

Знаходження елементів за їхнім атрибутом title (текст підказки)

### HTML приклад:
```html
<button title="Close dialog">X</button>
<a href="/help" title="Get help">?</a>
```

### Код Playwright:
```python
# Клік за title
page.get_by_title("Close dialog").click()
page.get_by_title("Get help").click()

# Часткове співпадіння
page.get_by_title("help", exact=False).click()
```

---

## Слайд 30: get_by_test_id() - Тестові ID

**Тестові ID** — це атрибути, додані спеціально для тестування. Використовуйте їх коли атрибути, орієнтовані на користувача, не стабільні.

### HTML приклад:
```html
<button data-testid="submit-button">Submit</button>
<div data-testid="error-message">Invalid input</div>
```

### Код Playwright:
```python
# Використання data-testid (атрибут за замовчуванням)
page.get_by_test_id("submit-button").click()

# Перевірка повідомлення про помилку
expect(page.get_by_test_id("error-message")).to_contain_text("Invalid")
```

---

## Слайд 31: Ланцюжки та Фільтрація Локаторів

Комбінуйте локатори для точного націлювання

```python
# Ланцюжок сучасних локаторів
page.get_by_role("navigation").get_by_role("link", name="Home").click()

# Фільтрація за текстом
page.get_by_role("listitem").filter(has_text="Product A").click()

# Фільтрація за вкладеним елементом
page.get_by_role("listitem").filter(
    has=page.get_by_role("button", name="Buy")
).click()

# Комбінація з CSS
page.locator(".product-card").get_by_role("button", name="Add to Cart").click()
```

---

## Слайд 32: Частина 4 — Найкращі Практики

# Частина 4
## Найкращі Практики

Як обрати правильний локатор

---

## Слайд 33: Пріоритет Локаторів: Що Використовувати Спочатку

**Рекомендований пріоритет Playwright (від найкращого до найгіршого):**

### Порядок пріоритету:
1. **get_by_role()** - ARIA ролі та доступні імена
2. **get_by_label()** - Поля форми з мітками
3. **get_by_placeholder()** - Поля форми з плейсхолдерами
4. **get_by_text()** - Текстовий вміст
5. **get_by_test_id()** - Тестові data атрибути
6. **CSS селектори** - Коли вищезазначені не працюють
7. **XPath** - Останній засіб для складних випадків

---

## Слайд 34: Хороші vs Погані Локатори

### Погані локатори:
```python
# Абсолютний XPath
page.locator("xpath=/html/body/div[2]/form/button")

# Загальні класи
page.locator(".btn.btn-1")

# На основі позиції
page.locator("button:nth-child(3)")

# Деталі реалізації
page.locator("[ng-click='submit()']")
```

### Хороші локатори:
```python
# На основі ролі
page.get_by_role("button", name="Submit")

# На основі мітки
page.get_by_label("Email")

# Test ID
page.get_by_test_id("submit-form")

# Семантичний CSS
page.locator("#login-form button[type='submit']")
```

---

## Слайд 35: Уникайте Крихких Селекторів

**Крихкі селектори** легко ламаються коли UI змінюється!

### Що робить селектор крихким?
- Залежність від позиції (nth-child, nth-of-type)
- Абсолютні шляхи
- Автогенеровані імена класів (напр., css-abc123)
- Занадто специфічні (довгі ланцюжки класів)
- Деталі реалізації (атрибути специфічні для фреймворку)

**Натомість:** Використовуйте семантичні, орієнтовані на користувача атрибути, які переживають рефакторинг!

---

## Слайд 36: Тримайте Селектори Простими

```python
# ЗАНАДТО СКЛАДНО
page.locator("div.container > div.row > div.col-md-6 > form > div:nth-child(2) > input")

# КРАЩЕ - Використовуйте унікальний атрибут
page.locator("[name='email']")

# НАЙКРАЩЕ - Використовуйте мітку
page.get_by_label("Email")
```

**Правило:** Якщо ви не можете пояснити свій селектор одним реченням, він занадто складний!

---

## Слайд 37: Коли Додавати Test ID

Іноді додавання тестового атрибуту — найкращий варіант

### Додавайте Test ID коли:
- Не існує стабільних атрибутів, орієнтованих на користувача
- Текстовий вміст часто змінюється (переклади, A/B тести)
- Кілька схожих елементів потребують розрізнення
- Складні динамічні компоненти

### Приклад:
```html
<!-- HTML -->
<button data-testid="checkout-submit" class="btn-xyz123">
  {{ translatedText }}
</button>
```

```python
# Playwright - стабільний між перекладами та редизайнами
page.get_by_test_id("checkout-submit").click()
```

---

## Слайд 38: Налагодження Локаторів

Інструменти для пошуку та тестування локаторів

### Техніки налагодження:
```python
# Підрахунок співпадаючих елементів
count = page.locator(".btn").count()
print(f"Знайдено {count} кнопок")

# Отримати весь текстовий вміст
buttons = page.locator("button").all_text_contents()
print(buttons)

# Підсвітити елемент
page.locator("#submit").highlight()

# Зробити скріншот з обмежувальною рамкою
page.locator("#submit").screenshot(path="button.png")
```

**Порада:** Використовуйте Playwright Inspector (`PWDEBUG=1`) для інтерактивного тестування локаторів!

---

## Слайд 39: Використання Browser DevTools

Тестування селекторів у консолі браузера

### У консолі браузера:
```javascript
// Тест CSS селектора
document.querySelector("#submit-btn")
document.querySelectorAll(".btn")

// Тест XPath (більш багатослівний)
$x("//button[@type='submit']")
$x("//button[text()='Login']")

// Підрахунок співпадінь
document.querySelectorAll(".btn").length
$x("//button").length
```

**Ярлик:** Правий клік на елементі → Inspect → Copy Selector/XPath (але не використовуйте сліпо!)

---

## Слайд 40: Поширені Помилки з Локаторами

### Помилка #1: Покладання на Порядок
`page.locator("button").nth(2)` ламається якщо кнопки переупорядковані

### Помилка #2: Згенеровані Імена Класів
`page.locator(".css-1dbjc4n-x9f619")` змінюється при кожному білді

### Помилка #3: Занадто Специфічний
`page.locator("div > div > div > button.btn")` занадто крихкий

### Помилка #4: Ігнорування Доступності
Втрачена можливість покращити і тести, І користувацький досвід

---

## Слайд 41: Реальний Приклад: Форма Логіну

### HTML:
```html
<form id="login-form">
  <label for="email">Email Address</label>
  <input id="email" type="email" placeholder="you@example.com">

  <label for="password">Password</label>
  <input id="password" type="password">

  <button type="submit">Sign In</button>
  <a href="/forgot">Forgot Password?</a>
</form>
```

### Найкращий підхід:
```python
page.get_by_label("Email Address").fill("user@example.com")
page.get_by_label("Password").fill("secret123")
page.get_by_role("button", name="Sign In").click()
page.get_by_role("link", name="Forgot Password?").click()
```

---

## Слайд 42: Шпаргалка

```python
# Сучасні Локатори (Перевага)
page.get_by_role("button", name="Submit")
page.get_by_label("Email")
page.get_by_placeholder("Search...")
page.get_by_text("Welcome")
page.get_by_test_id("submit-btn")

# CSS Селектори
page.locator("#id")           # ID
page.locator(".class")        # Class
page.locator("[attr='value']") # Атрибут
page.locator("tag.class")    # Комбінація

# XPath (використовуйте обережно)
page.locator("xpath=//button[@type='submit']")
page.locator("xpath=//button[text()='Login']")

# Ланцюжки
page.locator(".container").get_by_role("button").click()
```

---

## Слайд 43: Підсумок

### Ключові висновки:
- Віддавайте перевагу сучасним локаторам Playwright (`get_by_role`, `get_by_label`)
- Використовуйте CSS селектори для стабільних атрибутів (ID, name)
- Використовуйте XPath тільки коли необхідно (навігація до батька, складний текст)
- Уникайте крихких селекторів (позиція, згенеровані класи)
- Тримайте селектори простими та читабельними
- Додавайте test ID коли атрибути, орієнтовані на користувача, не стабільні
- Тестуйте свої селектори в browser DevTools

---

## Слайд 44: Що Далі?

### На наступних лекціях:
- Стратегії Локаторів Частина 2 (Розширена фільтрація та ланцюжки)
- Розширені взаємодії (Hover, Drag & Drop)
- Стратегії очікування та таймаути
- Assertions та Expectations

### Практика:
- Виконайте вправи в папці `exercises/`
- Перегляньте приклади в папці `examples/`
- Прочитайте детальний README.md

---

## Слайд 45: Фінальний Слайд

# Чудова Робота!

## Тепер ви розумієте стратегії локаторів!

Практикуйтесь з вправами щоб опанувати ці концепції
