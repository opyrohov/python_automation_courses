"""
My Modules Package
==================
This __init__.py file makes this directory a Python package.
"""

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Automation Course"

# You can import items here to make them available at package level
from .greetings import say_hello, say_goodbye
from .calculator import add, subtract, multiply, divide

# This makes these available as: from my_modules import say_hello
__all__ = ['say_hello', 'say_goodbye', 'add', 'subtract', 'multiply', 'divide']

print(f"my_modules package loaded (version {__version__})")
