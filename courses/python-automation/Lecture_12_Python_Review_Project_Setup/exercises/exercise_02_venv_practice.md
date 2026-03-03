# Exercise 2: Virtual Environment Practice

Master creating, activating, and managing virtual environments.

## Objective
Get comfortable with virtual environments by creating multiple environments and understanding how they isolate dependencies.

## Exercise 2.1: Basic venv Operations

### Task 1: Create and Activate
1. Create a new folder called `venv_practice`
2. Create a virtual environment named `venv`
3. Activate it
4. Verify it's activated (check prompt and Python location)

### Task 2: Install Packages
With venv activated:
1. Install `requests` package
2. List all installed packages
3. Save installed packages to `requirements.txt`
4. Deactivate the virtual environment

### Task 3: Verify Isolation
1. Try importing requests WITHOUT activating venv
   ```bash
   python -c "import requests"
   ```
   **Expected:** Should fail (ModuleNotFoundError)

2. Activate venv and try again
   ```bash
   venv\Scripts\activate  # Windows
   python -c "import requests"
   ```
   **Expected:** Should succeed

**Question:** Why does it work in venv but not outside?

## Exercise 2.2: Multiple Projects

Simulate having two projects with different dependencies.

### Project A Setup
```bash
mkdir project_a
cd project_a
python -m venv venv
# Activate venv
pip install playwright==1.39.0
pip freeze > requirements.txt
```

### Project B Setup
```bash
cd ..
mkdir project_b
cd project_b
python -m venv venv
# Activate venv
pip install playwright==1.40.0
pip freeze > requirements.txt
```

### Verification
1. Activate Project A's venv
2. Check Playwright version: `pip show playwright`
   **Expected:** 1.39.0

3. Deactivate and activate Project B's venv
4. Check Playwright version: `pip show playwright`
   **Expected:** 1.40.0

**Question:** How can both versions exist on the same computer?

## Exercise 2.3: Recreating Environments

Practice recreating a venv from requirements.txt (common when cloning projects).

### Step 1: Create Original Environment
```bash
mkdir original_project
cd original_project
python -m venv venv
# Activate venv
pip install playwright pytest python-dotenv
pip freeze > requirements.txt
```

### Step 2: Delete and Recreate
```bash
deactivate
# Delete venv folder
rm -rf venv  # Mac/Linux
# OR
rmdir /s venv  # Windows

# Create new venv
python -m venv venv
# Activate new venv
pip install -r requirements.txt
```

### Step 3: Verify
```bash
pip list
# Should have same packages as before
```

**Question:** Why is this useful when sharing projects with teammates?

## Exercise 2.4: Common Mistakes

Identify and fix these common mistakes:

### Mistake 1: Installing Without Activation
```bash
# Create venv but DON'T activate
python -m venv venv
pip install playwright  # MISTAKE!
```

**Problem:** Package installs globally instead of in venv

**Fix:** Activate venv first!
```bash
python -m venv venv
venv\Scripts\activate  # Activate FIRST
pip install playwright  # Now installs in venv
```

### Mistake 2: Wrong Python
```bash
python -m venv venv
# Activate venv
python  # Uses venv Python ✓
python3  # Might use system Python! ✗
```

**Fix:** Always use `python` after activating (not `python3` or full path)

### Mistake 3: Forgetting to Activate
```bash
# Day 1
python -m venv venv
venv\Scripts\activate
pip install playwright
pytest  # Works! ✓

# Day 2 - New terminal
cd my_project
pytest  # Fails! ✗ (venv not activated)
```

**Fix:** Remember to activate every time you open a new terminal!

## Exercise 2.5: Real-World Scenario

You're joining a new team. The project has:
- requirements.txt
- .gitignore (includes venv/)
- No venv folder (it's gitignored)

### Your Tasks:
1. Create a venv
2. Install dependencies from requirements.txt
3. Install Playwright browsers
4. Run tests to verify setup

**Steps:**
```bash
# Clone project (simulated)
mkdir team_project
cd team_project

# Create requirements.txt (simulating existing file)
echo playwright==1.40.0 > requirements.txt
echo pytest==8.0.0 >> requirements.txt

# Your setup steps:
# 1. ???
# 2. ???
# 3. ???
# 4. ???
```

## Exercise 2.6: Cleanup Practice

Learn to properly clean up virtual environments.

### Task: Create, Use, Delete
1. Create a venv in `temp_project/`
2. Install 3 packages
3. List installed packages
4. Deactivate
5. Delete the entire venv folder
6. Verify it's gone

**Commands:**
```bash
mkdir temp_project
cd temp_project
# Create venv
# Activate
# Install packages
# Deactivate
# Delete venv folder
```

## Challenge Questions

Answer these questions based on your understanding:

1. **What is a virtual environment?**
   _Your answer:_

2. **Why use virtual environments?**
   _Your answer:_

3. **Should you commit venv/ to Git? Why or why not?**
   _Your answer:_

4. **How do teammates get the right dependencies if venv/ is not in Git?**
   _Your answer:_

5. **What's the difference between these commands?**
   ```bash
   pip freeze
   pip freeze > requirements.txt
   pip install -r requirements.txt
   ```
   _Your answer:_

6. **True or False:**
   - [ ] You can use the same venv for multiple projects
   - [ ] Each project should have its own venv
   - [ ] venv folders are small (a few KB)
   - [ ] Deleting venv loses your code
   - [ ] You must activate venv every time you open a terminal

## Verification Checklist

- [ ] Created and activated multiple venvs
- [ ] Installed packages in isolated environments
- [ ] Recreated venv from requirements.txt
- [ ] Understood why venv isolation is important
- [ ] Practiced deactivating and deleting venvs
- [ ] Can explain when and why to use venvs

## Common Issues to Solve

Fix these scenarios:

### Scenario 1:
```bash
$ pip install playwright
ERROR: Could not install packages
```
**Diagnosis:** What's wrong?
**Solution:** ?

### Scenario 2:
```bash
$ python test.py
ModuleNotFoundError: No module named 'playwright'
```
But `pip list` shows playwright is installed.
**Diagnosis:** What's wrong?
**Solution:** ?

### Scenario 3:
```bash
(venv) $ deactivate
$ pytest
pytest: command not found
```
**Diagnosis:** What's wrong?
**Solution:** ?

## Time Estimate
45-60 minutes

## Success Criteria
You should be able to:
- Create venvs confidently
- Understand why they're important
- Troubleshoot activation issues
- Recreate environments from requirements.txt
- Explain venv isolation to others

## Next Steps
- Complete Exercise 3 (requirements.txt practice)
- Try using venv in a real project
- Help a teammate set up their venv!

See SOLUTIONS.md for answers and detailed explanations.
