# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python automation courses repository containing structured lectures with examples and exercises for learning Python programming and Playwright test automation.

### Course Phases

- **Python Fundamentals** (Lectures 1-12): Core Python concepts
- **Playwright Automation** (Lectures 13-21): Web automation with Playwright

## Language Guidelines

- **Code, README.md, presentation.html**: English
- **PRESENTATION_SCRIPT_UA.md**: Ukrainian (instructor script - what to say on each slide)

## Project Structure

```
python_automation_courses/
├── assets/                          # Global shared resources
│   ├── presentation/               # Shared presentation assets
│   │   ├── css/
│   │   │   └── styles.css         # Global presentation styling
│   │   ├── js/
│   │   │   └── presentation.js    # Global navigation script
│   │   └── README.md              # Presentation assets documentation
│   └── README.md                  # Assets folder documentation
│
├── Lecture_X_Topic_Name/
│   ├── README.md                    # Quick reference guide
│   ├── presentation.html           # Interactive HTML slide presentation
│   ├── PRESENTATION_SCRIPT_UA.md   # Ukrainian instructor script
│   ├── examples/                   # Code examples
│   │   ├── 01_first_topic.py
│   │   ├── 02_second_topic.py
│   │   └── ...
│   └── exercises/                  # Practice exercises
│       ├── exercise_01_topic.py
│       ├── exercise_02_topic.py
│       └── SOLUTIONS.md           # Solutions for all exercises
│
└── [Future lectures will follow the same structure]
```

Each lecture follows a consistent structure:
- **README.md**: Quick reference guide with code snippets
- **presentation.html**: Interactive slide presentation (uses global assets)
- **PRESENTATION_SCRIPT_UA.md**: Ukrainian script for instructor (what to say per slide)
- **examples/**: Numbered Python files demonstrating each concept (01_*.py, 02_*.py)
- **exercises/**: Practice problems with SOLUTIONS.md

Global shared resources:
- **assets/presentation/css/styles.css**: Global presentation styling (used by all lectures)
- **assets/presentation/js/presentation.js**: Global navigation script (used by all lectures)
- All presentations reference these files using relative paths: `../assets/presentation/`

## Development Setup

### Python Environment

- **Python Version**: 3.11 or later required
- **Virtual Environment**: Create with `python -m venv venv` and activate with `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Unix)

### Running Course Materials

```bash
# Run example files
python Lecture_X_Topic/examples/01_example.py

# Run exercises
python Lecture_X_Topic/exercises/exercise_01_topic.py

# Run Playwright examples (Lectures 13+)
python Lecture_15_Locator_Strategies_Part1/examples/01_css_selectors.py
```

## Course Design Principles

When creating new lectures or updating existing ones:

1. **Consistent Structure**: Follow the established pattern (README, presentation.html, PRESENTATION_SCRIPT_UA.md, examples/, exercises/)
2. **Progressive Learning**: Each example builds on previous concepts
3. **Hands-on Practice**: Exercises reinforce concepts from examples
4. **Comprehensive Documentation**: Each Python file includes detailed comments explaining concepts
5. **Solutions Provided**: Include SOLUTIONS.md for student reference after completion
6. **Visual Output**: Examples and exercises produce clear, formatted output for immediate feedback

## Creating New Lectures

To add a new lecture, follow this template:

1. Create `Lecture_X_Topic_Name/` directory
2. Add `README.md` with quick reference and code snippets
3. Create `presentation.html` - interactive slide presentation
   - Link to global CSS: `../assets/presentation/css/styles.css`
   - Link to global JS: `../assets/presentation/js/presentation.js`
4. Create `PRESENTATION_SCRIPT_UA.md` - Ukrainian instructor script
5. Create `examples/` with numbered Python files (01_*, 02_*, etc.)
6. Create `exercises/` with practice problems and `SOLUTIONS.md`

### Presentation Guidelines

The HTML presentations should:
- **Use global assets** - Link to `../assets/presentation/` for CSS and JS
- Include 15-25 slides covering all lecture topics
- Use syntax-highlighted code examples (classes defined in global CSS)
- Provide keyboard navigation (handled by global JS)
- Include visual elements (colored boxes, tables, two-column layouts)
- Feature a slide counter and navigation buttons (handled by global JS)
- Work offline in all modern browsers (no external dependencies)

#### Required Slide Structure

1. **Title slide** - with emoji logo (🎭 for Playwright, 🐍 for Python)
2. **"What You'll Learn Today"** - checklist of learning objectives
3. **Section dividers** - "Part 1", "Part 2" etc. for organizing content
4. **Content slides** - with code examples and explanations
5. **Summary/Recap** - at the end

#### Complete HTML Template

**IMPORTANT:** Always use this exact structure for presentations. Do NOT use Reveal.js or other frameworks.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture X: Topic Name</title>
    <link rel="stylesheet" href="../assets/presentation/css/styles.css">
</head>
<body>
    <div class="presentation">
        <div class="slide-counter">
            <span id="currentSlide">1</span> / <span id="totalSlides">20</span>
        </div>

        <!-- Title Slide -->
        <div class="slide active title-slide">
            <div class="python-logo">🎭</div>  <!-- Use 🐍 for Python, 🎭 for Playwright -->
            <h1>Lecture X</h1>
            <div class="subtitle">Topic Name</div>
            <p style="font-size: 1.3em; color: #888;">Python + Playwright Automation Course</p>
            <p style="margin-top: 50px; font-size: 1.1em; color: #999;">Press → to continue</p>
        </div>

        <!-- Learning Objectives -->
        <div class="slide">
            <h2>What You'll Learn Today</h2>
            <ul class="checklist">
                <li>✓ First learning objective</li>
                <li>✓ Second learning objective</li>
            </ul>
        </div>

        <!-- Section Divider -->
        <div class="slide section-slide">
            <h1>Part 1</h1>
            <h2>Section Title</h2>
            <p>Brief description</p>
        </div>

        <!-- Content Slide with Code -->
        <div class="slide">
            <h2>Slide Title</h2>
            <div class="code-block">
<span class="keyword">from</span> playwright.sync_api <span class="keyword">import</span> sync_playwright

<span class="keyword">with</span> <span class="function">sync_playwright</span>() <span class="keyword">as</span> p:
    browser = p.chromium.<span class="function">launch</span>()
    page = browser.<span class="function">new_page</span>()
    page.<span class="function">goto</span>(<span class="string">"https://example.com"</span>)
    <span class="comment"># This is a comment</span>
    count = <span class="number">42</span></div>
        </div>

        <!-- Final Slide -->
        <div class="slide title-slide">
            <div class="python-logo">🎭</div>
            <h1>Excellent!</h1>
            <div class="subtitle">You've completed Topic Name!</div>
        </div>

        <!-- Navigation (REQUIRED) -->
        <div class="navigation">
            <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)">← Previous</button>
            <button class="nav-btn" id="homeBtn" onclick="window.location.href='../index.html'" style="background: white; color: #667eea; border: 2px solid #667eea;">🏠 Home</button>
            <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)">Next →</button>
        </div>
    </div>
    <script src="../assets/presentation/js/presentation.js"></script>
</body>
</html>
```

#### CSS Classes for Slides

```html
<!-- Box types -->
<div class="highlight-box">Important concept</div>
<div class="success-box">Success message</div>
<div class="info-box">Information</div>
<div class="warning-box">Warning</div>

<!-- Code syntax highlighting (inside <div class="code-block">) -->
<span class="keyword">from</span>
<span class="string">"text"</span>
<span class="function">method_name</span>
<span class="comment"># comment</span>
<span class="number">123</span>

<!-- Two-column layout -->
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
    <div class="success-box">Left column</div>
    <div class="warning-box">Right column</div>
</div>

<!-- Table inside info-box -->
<div class="info-box">
    <table style="width: 100%;">
        <tr><th>Header 1</th><th>Header 2</th></tr>
        <tr><td>Cell 1</td><td>Cell 2</td></tr>
    </table>
</div>
```

#### Key Rules for Presentations

1. **Container structure**: Always use `<div class="presentation">` as the main container
2. **Slide counter**: Include `<div class="slide-counter">` with proper span IDs
3. **First slide**: Must have `class="slide active title-slide"` (note: `active` class!)
4. **Section dividers**: Use `class="slide section-slide"` for part headers
5. **Code blocks**: Use `<div class="code-block">` with syntax highlighting spans
6. **Navigation**: Always include the navigation div with three buttons
7. **Scripts**: Link to global JS at the end: `../assets/presentation/js/presentation.js`
8. **No whitespace in code-block**: Code inside `<div class="code-block">` must start immediately after `>` with no leading spaces

### PRESENTATION_SCRIPT_UA.md Format

This file contains the Ukrainian script for the instructor - what to say on each slide:

```markdown
# Скрипт презентації - Лекція X: Topic Name

## Слайд 1: Титульний слайд

**Що говорити:**

Доброго дня. Сьогодні лекція X - Topic Name...

---

## Слайд 2: What You'll Learn Today

**Що говорити:**

Ось наш план на сьогодні...

---
```

Key points:
- Each slide has "## Слайд N: Title" header
- "**Що говорити:**" section with Ukrainian text
- Use "---" as separator between slides
- Match slide numbers to presentation.html

### Global Assets Reference

All presentations share:
- **CSS** (`assets/presentation/css/styles.css`): Styling, layout, animations, syntax highlighting
- **JavaScript** (`assets/presentation/js/presentation.js`): Navigation, keyboard shortcuts, touch support

Benefits:
- ✅ Consistent look and feel across all lectures
- ✅ Update once, affect all presentations
- ✅ Smaller repository size (no duplication)
- ✅ Easier maintenance

See `assets/presentation/README.md` for detailed documentation on using and customizing global assets.

## Example File Formats

### Playwright Examples (Lectures 13+)

```python
"""Example 1: Topic Name"""
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print("=== Topic Demo ===\n")

    # Example 1: Description
    print("1. Testing feature...")
    page.goto("https://example.com")

    expect(page.locator("#element")).to_be_visible()
    print("   ✓ Element is visible")

    # Example 2: Another feature
    print("\n2. Testing another feature...")
    # ... more code
    print("   ✓ Feature works correctly")

    print("\n=== Demo Complete ===")
    browser.close()
```

Key points:
- Use `headless=False, slow_mo=500` for visual demos
- Print statements with `✓` emoji for visual feedback
- Clear section headers with `print("=== ... ===")`
- Numbered examples: `print("1. ...")`, `print("2. ...")`

### Python Fundamentals Examples (Lectures 1-12)

```python
"""Example 1: Topic Name
Demonstrates: concept being taught
"""

# Section header
print("=== Topic Name ===")
print()

# Example with explanation comments
variable = "value"  # Explanation of what this does
print(f"Result: {variable}")
```

## Dependencies

### Python Fundamentals (Lectures 1-12)
- Python 3.11+ (standard library only)

### Playwright Automation (Lectures 13+)
```bash
pip install playwright pytest
playwright install
```
