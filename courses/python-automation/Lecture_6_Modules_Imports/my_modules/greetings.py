"""
A simple module with greeting functions.
This demonstrates how to create your own modules.
"""

def say_hello(name):
    """Return a hello greeting."""
    return f"Hello, {name}!"

def say_goodbye(name):
    """Return a goodbye message."""
    return f"Goodbye, {name}!"

def greet_multiple(names):
    """Greet multiple people."""
    greetings = []
    for name in names:
        greetings.append(say_hello(name))
    return greetings

# Module-level variable
MODULE_VERSION = "1.0.0"
GREETING_LANGUAGE = "English"

# This code runs when module is imported
print(f"Greetings module loaded (version {MODULE_VERSION})")
