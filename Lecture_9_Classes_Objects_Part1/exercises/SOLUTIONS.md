# Lecture 9: Classes & Objects (Part 1) - Exercise Solutions

This file contains solutions for all exercises in Lecture 9.

## Exercise 1: Basic Classes

### Exercise 1.1: Create a Simple Class
```python
class Book:
    """Represents a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Test
book1 = Book("Python Basics", "John Doe")
print(f"{book1.title} by {book1.author}")
```

### Exercise 1.2: Add More Attributes
```python
class Movie:
    """Represents a movie."""
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

# Test
movie = Movie("Inception", "Christopher Nolan", 2010)
print(f"{movie.title} ({movie.year}) directed by {movie.director}")
```

### Exercise 1.3: Default Values
```python
class Product:
    """Represents a product."""
    def __init__(self, name, price, in_stock=True):
        self.name = name
        self.price = price
        self.in_stock = in_stock

# Test
product1 = Product("Laptop", 999.99)
product2 = Product("Mouse", 29.99, False)
print(f"{product1.name}: ${product1.price}, In Stock: {product1.in_stock}")
print(f"{product2.name}: ${product2.price}, In Stock: {product2.in_stock}")
```

### Exercise 1.4: Test User Class
```python
class TestUser:
    """Represents a test user."""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = True

# Test
user = TestUser("testuser1", "test@example.com", "Pass123!")
print(f"User: {user.username}, Active: {user.is_active}")
```

### Exercise 1.5: Browser Config Class
```python
class BrowserConfig:
    """Browser configuration class."""
    def __init__(self, browser_type="chromium", headless=False, timeout=30000):
        self.browser_type = browser_type
        self.headless = headless
        self.timeout = timeout

# Test
config1 = BrowserConfig()
config2 = BrowserConfig("firefox", True, 60000)
print(f"Config 1: {config1.browser_type}, headless={config1.headless}")
print(f"Config 2: {config2.browser_type}, headless={config2.headless}")
```

---

## Exercise 2: Instance Methods

### Exercise 2.1: Add a Method
```python
class Dog:
    """Represents a dog."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says Woof!")

# Test
dog = Dog("Buddy", 3)
dog.bark()  # Buddy says Woof!
```

### Exercise 2.2: Method with Return Value
```python
class Calculator:
    """Simple calculator class."""
    def __init__(self, name):
        self.name = name

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

# Test
calc = Calculator("MyCalc")
print(calc.add(5, 3))        # 8
print(calc.multiply(4, 7))   # 28
```

### Exercise 2.3: Bank Account
```python
class BankAccount:
    """Represents a bank account."""
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw money."""
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        """Get current balance."""
        return self.balance

# Test
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: ${account.get_balance()}")  # Balance: $1300
```

### Exercise 2.4: Shopping Cart
```python
class ShoppingCart:
    """Represents a shopping cart."""
    def __init__(self):
        self.items = []

    def add_item(self, item_name):
        """Add item to cart."""
        self.items.append(item_name)

    def remove_item(self, item_name):
        """Remove item from cart."""
        if item_name in self.items:
            self.items.remove(item_name)

    def get_item_count(self):
        """Get number of items."""
        return len(self.items)

    def clear(self):
        """Clear the cart."""
        self.items = []

# Test
cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Mouse")
print(f"Items: {cart.get_item_count()}")  # 2
cart.remove_item("Mouse")
print(f"Items: {cart.get_item_count()}")  # 1
```

---

## Exercise 3: Page Objects

### Exercise 3.1: Simple LoginPage
```python
class LoginPage:
    """Page object for login page."""
    def __init__(self, page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "#submit"

    def enter_username(self, username):
        """Enter username."""
        print(f"Entering username: {username}")
        # self.page.fill(self.username_input, username)

    def enter_password(self, password):
        """Enter password."""
        print(f"Entering password: {'*' * len(password)}")
        # self.page.fill(self.password_input, password)

    def click_submit(self):
        """Click submit button."""
        print("Clicking submit")
        # self.page.click(self.submit_button)
```

### Exercise 3.2: LoginPage with login() Method
```python
class LoginPage:
    """Page object for login page."""
    def __init__(self, page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "#submit"

    def enter_username(self, username):
        """Enter username."""
        print(f"Entering username: {username}")
        # self.page.fill(self.username_input, username)

    def enter_password(self, password):
        """Enter password."""
        print(f"Entering password: {'*' * len(password)}")
        # self.page.fill(self.password_input, password)

    def click_submit(self):
        """Click submit button."""
        print("Clicking submit")
        # self.page.click(self.submit_button)

    def login(self, username, password):
        """Perform complete login."""
        print(f"🔐 Logging in as: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()

# Test (simulated)
class FakePage:
    pass

login_page = LoginPage(FakePage())
login_page.login("testuser", "password123")
```

### Exercise 3.3: HomePage
```python
class HomePage:
    """Page object for home page."""
    def __init__(self, page):
        self.page = page
        self.welcome_message = ".welcome-message"
        self.logout_button = "#logout"
        self.profile_link = "#profile"

    def get_welcome_text(self):
        """Get welcome message text."""
        # return self.page.locator(self.welcome_message).text_content()
        return "Welcome, User!"

    def logout(self):
        """Click logout button."""
        print("Logging out")
        # self.page.click(self.logout_button)

    def go_to_profile(self):
        """Navigate to profile page."""
        print("Going to profile")
        # self.page.click(self.profile_link)
```

### Exercise 3.4: ProductPage
```python
class ProductPage:
    """Page object for product page."""
    def __init__(self, page):
        self.page = page
        self.product_title = "h1.product-title"
        self.price = ".product-price"
        self.add_to_cart_button = "#add-to-cart"
        self.quantity_input = "#quantity"

    def get_product_name(self):
        """Get product name."""
        # return self.page.locator(self.product_title).text_content()
        return "Sample Product"

    def get_price(self):
        """Get product price."""
        # price_text = self.page.locator(self.price).text_content()
        # return float(price_text.replace("$", ""))
        return 29.99

    def set_quantity(self, qty):
        """Set product quantity."""
        print(f"Setting quantity to: {qty}")
        # self.page.fill(self.quantity_input, str(qty))

    def add_to_cart(self):
        """Add product to cart."""
        print("Adding to cart")
        # self.page.click(self.add_to_cart_button)
```

### BONUS: BasePage
```python
class BasePage:
    """Base class for all page objects."""
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url):
        """Navigate to URL."""
        print(f"Navigating to: {url}")
        # self.page.goto(url)

    def get_title(self):
        """Get page title."""
        # return self.page.title()
        return "Page Title"

    def take_screenshot(self, name):
        """Take screenshot."""
        print(f"📸 Taking screenshot: {name}.png")
        # self.page.screenshot(path=f"{name}.png")

class LoginPage(BasePage):
    """Login page inheriting from BasePage."""
    def __init__(self, page):
        super().__init__(page)  # Call parent __init__
        self.username_input = "#username"
        self.password_input = "#password"
        self.submit_button = "#submit"

    def login(self, username, password):
        """Perform login."""
        print(f"Logging in as: {username}")
        # self.page.fill(self.username_input, username)
        # self.page.fill(self.password_input, password)
        # self.page.click(self.submit_button)

# Now LoginPage has all BasePage methods!
# login_page.navigate_to("https://example.com/login")
# login_page.take_screenshot("before_login")
```

---

## Key Takeaways

1. **Classes** are blueprints for creating objects
2. **`__init__`** method initializes new objects
3. **`self`** refers to the current instance
4. **Instance variables** store data unique to each object
5. **Instance methods** define behaviors and actions
6. **Page Object Model** organizes automation code effectively
7. **Inheritance** (BasePage) allows code reuse

## Next Steps

- Practice creating more complex classes
- Build page objects for your test websites
- Combine multiple page objects in test flows
- Learn about class methods and inheritance in Lecture 10

Good luck with your automation journey!
