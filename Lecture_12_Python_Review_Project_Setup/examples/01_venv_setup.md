# Virtual Environment Setup Guide

This guide walks you through creating and using virtual environments for your Python automation projects.

## What is a Virtual Environment?

A virtual environment is an isolated Python environment that:
- Contains its own Python interpreter
- Has its own set of installed packages
- Doesn't interfere with other projects or system Python
- Can be easily recreated on other machines

## Why Use Virtual Environments?

### Problem: Without Virtual Environments
```
System Python
├── Project A needs pytest 7.0
├── Project B needs pytest 8.0
└── CONFLICT! Can only have one version installed
```

### Solution: With Virtual Environments
```
System Python
├── Project A
│   └── venv (pytest 7.0)
└── Project B
    └── venv (pytest 8.0)
NO CONFLICTS! Each project isolated.
```

## Creating a Virtual Environment

### Step 1: Navigate to Your Project Folder
```bash
# Create a new project folder
mkdir my_automation_project
cd my_automation_project
```

### Step 2: Create Virtual Environment
```bash
# Create venv (named 'venv' by convention)
python -m venv venv

# You can name it anything, but 'venv' is standard
# python -m venv my_env_name
```

This creates a `venv/` folder containing:
- Python interpreter copy
- pip package manager
- Space for installed packages

### Step 3: Activate Virtual Environment

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Verify Activation
You should see `(venv)` at the beginning of your command prompt:
```bash
(venv) C:\my_automation_project>
```

Verify Python is from venv:
```bash
# Windows
where python
# Should show: C:\my_automation_project\venv\Scripts\python.exe

# Mac/Linux
which python
# Should show: /path/to/my_automation_project/venv/bin/python
```

## Using Virtual Environment

### Installing Packages
Once activated, all `pip install` commands install to venv, not system Python:

```bash
# Activate venv first!
(venv) $ pip install playwright

# Package is installed only in this venv
```

### Check Installed Packages
```bash
(venv) $ pip list

# Shows only packages in this venv
```

### Deactivating Virtual Environment
When you're done working on the project:
```bash
(venv) $ deactivate

# Prompt returns to normal (no 'venv' prefix)
$
```

## Daily Workflow

Every time you work on your project:

1. **Open terminal**
2. **Navigate to project folder**
   ```bash
   cd my_automation_project
   ```
3. **Activate venv**
   ```bash
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```
4. **Work on project** (run tests, install packages, etc.)
5. **Deactivate when done**
   ```bash
   deactivate
   ```

## Git and Virtual Environments

### NEVER Commit venv to Git!

The `venv/` folder should NEVER be committed to version control because:
- It's large (hundreds of MB)
- It's machine-specific (won't work on other computers)
- Other developers should create their own venv

### Add to .gitignore
Create `.gitignore` file:
```
# Virtual environments
venv/
env/
ENV/
.venv/

# Python cache
__pycache__/
*.pyc
*.pyo

# Pytest cache
.pytest_cache/

# Test results
test-results/
screenshots/
videos/

# Environment variables
.env

# IDE
.vscode/
.idea/
*.swp
```

## Common Issues and Solutions

### Issue 1: "python: command not found"
**Solution**: Install Python first
```bash
# Check if Python is installed
python --version

# If not installed, download from python.org
```

### Issue 2: PowerShell execution policy error
**Error**:
```
cannot be loaded because running scripts is disabled on this system
```

**Solution**: Change execution policy (one-time)
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue 3: Venv not activating (no prefix showing)
**Solutions**:
- Make sure you're in the project folder containing `venv/`
- Check the activation command is correct for your OS
- Try closing and reopening terminal
- On Windows, try Command Prompt instead of PowerShell

### Issue 4: "pip: command not found" after activation
**Solution**: Recreate venv with --pip option
```bash
# Delete old venv
rm -rf venv  # Mac/Linux
rmdir /s venv  # Windows

# Create new venv ensuring pip is included
python -m venv venv --pip
```

### Issue 5: Using wrong Python version
**Solution**: Specify Python version when creating venv
```bash
# Use specific Python version (if multiple installed)
python3.11 -m venv venv
# or
py -3.11 -m venv venv
```

## Sharing Your Project

When someone else clones your project:

1. They clone the repository (without venv)
2. They create their own venv:
   ```bash
   python -m venv venv
   ```
3. They activate venv
4. They install dependencies from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
5. They're ready to work!

## Best Practices

✅ **DO:**
- Always use venv for projects
- Name it `venv` (convention)
- Activate before working on project
- Add to .gitignore
- Use requirements.txt to track dependencies

❌ **DON'T:**
- Commit venv to Git
- Install packages without activating venv
- Share venv folder between projects
- Modify venv folder manually

## Quick Command Reference

```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install package
pip install package_name

# Install from requirements.txt
pip install -r requirements.txt

# List installed packages
pip list

# Save current packages to requirements.txt
pip freeze > requirements.txt

# Deactivate
deactivate

# Delete venv (if needed)
rm -rf venv  # Mac/Linux
rmdir /s venv  # Windows
```

## Next Steps

Now that you understand virtual environments:
1. Create a venv for your automation project
2. Install Playwright and pytest
3. Create requirements.txt
4. Start writing tests!

See `02_project_structure/` for the complete project setup.
