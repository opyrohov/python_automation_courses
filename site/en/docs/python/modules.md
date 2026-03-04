# Modules

Modules and packages in Python — code organization, imports, and virtual environments.

## Importing Modules

```python
# Importing entire module
import os
import json

# Importing specific objects
from pathlib import Path
from typing import Optional, List

# Importing with alias
import datetime as dt
from collections import defaultdict as dd

# Importing everything (not recommended)
from os.path import *
```

::: warning Avoid import *
`from module import *` imports everything from the module, which can lead to name conflicts. Always import specific objects.
:::

## Creating Modules

```python
# utils/helpers.py
"""Helper functions for tests."""

def generate_email(name: str) -> str:
    """Generates a test email."""
    return f"{name.lower()}@test.com"

def generate_password(length: int = 12) -> str:
    """Generates a random password."""
    import string
    import random
    chars = string.ascii_letters + string.digits + "!@#$%"
    return "".join(random.choices(chars, k=length))

# Constants
DEFAULT_TIMEOUT = 30000
BASE_URL = "https://example.com"
```

```python
# Usage in another file
from utils.helpers import generate_email, generate_password, DEFAULT_TIMEOUT

email = generate_email("john")  # john@test.com
password = generate_password()  # random password
```

## Packages

A package is a directory with an `__init__.py` file.

```
project/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   └── test_signup.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   ├── data_generator.py
│   └── constants.py
└── conftest.py
```

```python
# pages/__init__.py — exporting main classes
from .base_page import BasePage
from .login_page import LoginPage
from .dashboard_page import DashboardPage

__all__ = ["BasePage", "LoginPage", "DashboardPage"]
```

```python
# Now you can import directly from the package
from pages import LoginPage, DashboardPage
```

## Standard Library

### os and pathlib

```python
import os
from pathlib import Path

# Working with paths (pathlib recommended)
project_root = Path(__file__).parent.parent
config_path = project_root / "config" / "settings.json"
screenshots_dir = project_root / "screenshots"

# Creating a directory
screenshots_dir.mkdir(parents=True, exist_ok=True)

# Checking existence
if config_path.exists():
    print("Config found")

# Environment variables
base_url = os.getenv("BASE_URL", "https://localhost:3000")
api_key = os.environ.get("API_KEY")
```

### json

```python
import json

# Reading JSON
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Writing JSON
data = {"users": [{"name": "John", "role": "QA"}]}
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Working with strings
json_str = json.dumps(data, indent=2)
parsed = json.loads(json_str)
```

### datetime

```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()
utc_now = datetime.utcnow()

# Formatting
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
# "2024-01-15_14-30-45"

# Parsing
date = datetime.strptime("2024-01-15", "%Y-%m-%d")

# Arithmetic
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
```

### logging

```python
import logging

# Logger configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("test_run.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("tests")

# Usage
logger.info("Test started")
logger.warning("Element not found, retrying")
logger.error("Test failed: %s", error_message)
```

## Virtual Environments

```bash
# Creating a virtual environment
python -m venv venv

# Activation
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Installing dependencies
pip install playwright pytest

# Saving dependencies
pip freeze > requirements.txt

# Installing from file
pip install -r requirements.txt

# Deactivation
deactivate
```

::: tip requirements.txt for a QA Project
```txt
playwright==1.40.0
pytest==7.4.3
pytest-playwright==0.4.3
pytest-html==4.1.1
pytest-xdist==3.5.0
allure-pytest==2.13.2
python-dotenv==1.0.0
```
:::

## Useful Links

- [Documentation: Modules](https://docs.python.org/3/tutorial/modules.html)
- [Documentation: venv](https://docs.python.org/3/library/venv.html)
- [pip documentation](https://pip.pypa.io/en/stable/)
