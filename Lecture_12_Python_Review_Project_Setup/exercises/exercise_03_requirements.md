# Exercise 3: Requirements.txt Practice

Master dependency management with requirements.txt files.

## Objective
Learn to create, maintain, and use requirements.txt files effectively for reproducible environments.

## Exercise 3.1: Creating requirements.txt

### Method 1: Manual Creation (Recommended)

Create `requirements.txt` manually with these packages:
```
playwright==1.40.0
pytest==8.0.0
pytest-playwright==0.4.4
requests==2.31.0
python-dotenv==1.0.0
```

**Questions:**
1. What do the `==` symbols mean?
2. Why specify versions?
3. What happens if you use `>=` instead of `==`?

### Method 2: Freeze Current Environment

```bash
# Install some packages
pip install playwright pytest requests

# Generate requirements.txt from installed packages
pip freeze > requirements_frozen.txt

# Compare with manual version
# Open both files and compare
```

**Questions:**
1. Which file is longer?
2. Why are there more packages in frozen version?
3. Which method is better for a project?

## Exercise 3.2: Installing from requirements.txt

### Setup
1. Create a new folder: `install_practice`
2. Create `requirements.txt`:
   ```
   pytest==8.0.0
   requests==2.31.0
   ```

### Tasks
1. Create and activate venv
2. Install from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify installation:
   ```bash
   pip list
   pytest --version
   ```
4. Try importing in Python:
   ```bash
   python -c "import pytest, requests; print('Success!')"
   ```

**Expected:** All packages installed correctly ✓

## Exercise 3.3: Version Pinning Strategies

Create three different requirements files:

### requirements_exact.txt (Exact versions)
```
playwright==1.40.0
pytest==8.0.0
```

### requirements_minimum.txt (Minimum versions)
```
playwright>=1.40.0
pytest>=8.0.0
```

### requirements_compatible.txt (Compatible versions)
```
playwright~=1.40.0
pytest~=8.0.0
```

### Test Each Strategy

For each file:
1. Create a new venv
2. Install from the requirements file
3. Check what versions were installed

**Questions:**
1. Which strategy installs the latest version?
2. Which is safest for production?
3. When would you use each strategy?

## Exercise 3.4: Dependency Conflicts

Experience and resolve dependency conflicts.

### Scenario: Conflicting Requirements

Create `requirements_conflict.txt`:
```
package-a==1.0.0
package-b==2.0.0
```

Where package-a requires package-c>=2.0.0
But package-b requires package-c<2.0.0

**Task:** Try to install these (simulated):
```bash
# This will fail
pip install -r requirements_conflict.txt
```

**Questions:**
1. What error message do you see?
2. How would you resolve this?
3. How can you prevent this?

## Exercise 3.5: Organizing Requirements

For larger projects, split requirements into multiple files.

### Create Requirements Files

**requirements/base.txt** (core dependencies):
```
playwright==1.40.0
pytest==8.0.0
python-dotenv==1.0.0
```

**requirements/dev.txt** (development tools):
```
-r base.txt
pytest-cov==4.1.0
black==23.12.1
flake8==7.0.0
```

**requirements/prod.txt** (production only):
```
-r base.txt
gunicorn==21.2.0
```

### Install Different Environments

```bash
# Development environment
pip install -r requirements/dev.txt

# Production environment
pip install -r requirements/prod.txt
```

**Question:** Why split requirements?

## Exercise 3.6: Updating Dependencies

Practice updating packages safely.

### Initial Setup
```bash
# Create venv
# Install old versions
pip install playwright==1.39.0 pytest==7.4.0

# Save current state
pip freeze > requirements_old.txt
```

### Update Strategy 1: Update All
```bash
# Update everything to latest
pip install --upgrade -r requirements_old.txt

# Check new versions
pip list

# Save new requirements
pip freeze > requirements_new.txt
```

### Update Strategy 2: Update One at a Time
```bash
# Update only playwright
pip install --upgrade playwright

# Test everything still works
pytest

# If good, update requirements.txt
```

**Questions:**
1. Which strategy is safer?
2. When would you update all at once?
3. How do you test if updates broke anything?

## Exercise 3.7: Comments and Organization

Create a well-documented requirements.txt:

```
# ============================================================================
# TESTING FRAMEWORK
# ============================================================================

# Playwright - Browser automation
playwright==1.40.0

# Pytest - Testing framework
pytest==8.0.0

# Pytest-Playwright - Integration
pytest-playwright==0.4.4


# ============================================================================
# UTILITIES
# ============================================================================

# Environment variable management
python-dotenv==1.0.0

# HTTP library for API testing
requests==2.31.0


# ============================================================================
# DEVELOPMENT TOOLS (optional)
# ============================================================================

# Code formatting
# black==23.12.1

# Linting
# flake8==7.0.0
```

**Tasks:**
1. Install from this file
2. Add your own comments
3. Organize by category

## Exercise 3.8: Requirements Best Practices

Fix these poorly written requirements files:

### Bad Example 1: No versions
```
playwright
pytest
requests
```
**Problems:**
- Different team members get different versions
- Not reproducible
- May break in future

**Fix:** Add version pinning

### Bad Example 2: Too specific
```
playwright==1.40.0
anyio==4.2.0
certifi==2023.11.17
charset-normalizer==3.3.2
idna==3.6
... (50 more packages)
```
**Problems:**
- Hard to read
- Includes all dependencies
- Hard to maintain

**Fix:** Only list direct dependencies

### Bad Example 3: No organization
```
black==23.12.1
playwright==1.40.0
flake8==7.0.0
pytest==8.0.0
requests==2.31.0
```
**Problems:**
- Hard to find packages
- No context for what each is for

**Fix:** Add comments and organization

## Exercise 3.9: Real-World Scenario

You're taking over a project with this requirements.txt:

```
playwright
pytest
requests==2.25.0
beautifulsoup4
pandas
```

### Problems to Identify:
1. Which packages have no version specified?
2. Which package is very outdated?
3. How would you improve this file?

### Your Tasks:
1. Identify all issues
2. Create an improved version
3. Test the new requirements.txt
4. Document your changes

## Exercise 3.10: CI/CD Considerations

Create requirements files for different environments:

### requirements-test.txt (CI/CD)
```
playwright==1.40.0
pytest==8.0.0
pytest-playwright==0.4.4
pytest-xdist==3.5.0  # Parallel testing
```

### requirements-local.txt (Development)
```
-r requirements-test.txt
pytest-watch==4.2.0  # Auto-run tests
ipython==8.19.0  # Better REPL
```

**Questions:**
1. Why separate files?
2. What's `-r requirements-test.txt`?
3. When would you use each file?

## Challenge Exercises

### Challenge 1: Dependency Detective
Given only a requirements.txt, determine:
- What kind of project is this?
- What testing frameworks are used?
- Is this for web automation, API testing, or both?

### Challenge 2: Minimal Requirements
You have a huge requirements.txt from `pip freeze`.
Create a minimal version with only direct dependencies.

### Challenge 3: Version Compatibility
Research: What's the latest compatible version of:
- playwright with Python 3.8?
- pytest with Python 3.12?

Update requirements.txt accordingly.

## Verification Checklist

- [ ] Created requirements.txt manually
- [ ] Generated requirements with pip freeze
- [ ] Installed from requirements.txt
- [ ] Understood different version pinning strategies
- [ ] Organized requirements with comments
- [ ] Split requirements for different environments
- [ ] Updated dependencies safely
- [ ] Identified and fixed bad requirements files

## Common Mistakes to Avoid

1. **Using pip freeze blindly**
   - Includes all sub-dependencies
   - Hard to maintain
   - Better: manually list only what you use

2. **No version pinning**
   - Causes "works on my machine" problems
   - Hard to reproduce issues
   - Always pin versions

3. **Outdated dependencies**
   - Security vulnerabilities
   - Missing features
   - Review and update regularly

4. **Committing virtual environment**
   - requirements.txt is enough
   - venv should be in .gitignore
   - Others recreate from requirements.txt

## Quick Reference

```bash
# Create requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Upgrade packages
pip install --upgrade -r requirements.txt

# Check outdated packages
pip list --outdated

# Install with additional index
pip install -r requirements.txt -i https://pypi.org/simple
```

## Time Estimate
45-60 minutes

## Success Criteria

You should be able to:
- Create clear, maintainable requirements.txt
- Choose appropriate version pinning strategy
- Install and update dependencies confidently
- Organize requirements for different environments
- Troubleshoot dependency issues
- Explain why requirements.txt is important

## Next Steps
- Apply this to your real project
- Set up automated dependency updates (Dependabot/Renovate)
- Learn about poetry or pipenv (alternative tools)

See SOLUTIONS.md for detailed answers and explanations!
