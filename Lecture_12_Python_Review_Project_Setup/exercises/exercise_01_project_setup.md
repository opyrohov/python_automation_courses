# Exercise 1: Project Setup

Practice creating a professional automation project from scratch.

## Objective
Create a complete automation project with proper structure, virtual environment, and configuration.

## Instructions

### Part 1: Create Project Structure

1. Create a new folder called `my_test_project`
2. Navigate into the folder
3. Create the following subfolders:
   - `tests`
   - `pages`
   - `utils`
   - `test_data`
4. Create `__init__.py` files in `tests`, `pages`, and `utils` folders

**Expected result:**
```
my_test_project/
├── tests/
│   └── __init__.py
├── pages/
│   └── __init__.py
├── utils/
│   └── __init__.py
└── test_data/
```

### Part 2: Set Up Virtual Environment

1. Create a virtual environment named `venv`
2. Activate the virtual environment
3. Verify activation (you should see `(venv)` in your prompt)
4. Check that Python is running from the venv folder

**Commands to use:**
- Create: `python -m venv venv`
- Activate Windows: `venv\Scripts\activate`
- Activate Mac/Linux: `source venv/bin/activate`
- Verify: `where python` (Windows) or `which python` (Mac/Linux)

### Part 3: Create requirements.txt

Create a `requirements.txt` file with the following dependencies:
- playwright version 1.40.0
- pytest version 8.0.0
- pytest-playwright version 0.4.4
- python-dotenv version 1.0.0

**Hint:** Each line should be: `package==version`

### Part 4: Install Dependencies

1. Install all packages from requirements.txt
2. Install Playwright browsers
3. Verify everything is installed correctly

**Commands:**
```bash
pip install -r requirements.txt
playwright install
pip list
pytest --version
playwright --version
```

### Part 5: Create .gitignore

Create a `.gitignore` file that excludes:
- Virtual environment (`venv/`)
- Python cache (`__pycache__/`, `*.pyc`)
- Pytest cache (`.pytest_cache/`)
- Test results (`test-results/`, `screenshots/`, `videos/`)
- Environment variables (`.env`)
- IDE files (`.vscode/`, `.idea/`)

### Part 6: Create pytest.ini

Create a `pytest.ini` file with:
- testpaths pointing to `tests`
- Three custom markers: `smoke`, `regression`, `critical`
- Default options: `-v --tb=short`

### Part 7: Create Configuration

Create `utils/config.py` with:
- Import for os and dotenv
- Load environment variables
- BASE_URL variable
- HEADLESS variable (boolean)
- DEFAULT_TIMEOUT variable (30000)

### Part 8: Create .env File

Create `.env` file with:
- BASE_URL=https://example.com
- HEADLESS=False
- BROWSER=chromium

Also create `.env.example` as a template (without sensitive values).

### Part 9: Write Your First Test

Create `tests/test_example.py` with a simple test that:
1. Navigates to https://www.google.com
2. Verifies the page title contains "Google"
3. Verifies the search box is visible

Use the AAA pattern (Arrange, Act, Assert).

### Part 10: Run and Verify

1. Run your test: `pytest`
2. Run in headed mode: `pytest --headed`
3. Run with verbose output: `pytest -v`

**Expected:** Test should pass ✓

## Success Criteria

- [ ] Project structure created correctly
- [ ] Virtual environment created and activated
- [ ] All dependencies installed
- [ ] Configuration files created (.gitignore, pytest.ini, .env)
- [ ] Config module created
- [ ] First test written and passing
- [ ] Can run tests in both headless and headed modes

## Bonus Challenges

1. **Add More Tests**: Create `test_search.py` with a test that performs a search on Google
2. **Create BasePage**: Create `pages/base_page.py` with a BasePage class
3. **Add Helper Function**: Create a helper function in `utils/helpers.py` for taking screenshots
4. **Documentation**: Create a `README.md` documenting your project setup

## Troubleshooting

If you get stuck:
- Check that venv is activated (you should see `(venv)` in prompt)
- Verify Python version: `python --version` (should be 3.8+)
- Check installed packages: `pip list`
- Make sure you're in the project directory
- Review the examples in `examples/05_setup_guide.md`

## Time Estimate
30-45 minutes

## Next Steps
After completing this exercise:
1. Make sure you understand each file's purpose
2. Try breaking something and fixing it
3. Move to Exercise 2 to practice with virtual environments
4. Start thinking about what you'll test in your real projects

Good luck! 🚀
