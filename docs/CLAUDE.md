# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python automation courses repository containing structured lectures with examples and exercises for learning Python programming.

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
├── Lecture_1_Python_Basics_Setup/
│   ├── README.md                    # Main lecture guide
│   ├── QUICK_START.md              # Quick start guide for students
│   ├── presentation.html           # Interactive HTML slide presentation
│   ├── PRESENTATION_GUIDE.md       # Guide for using the presentation
│   ├── examples/                   # Code examples demonstrating concepts
│   │   ├── 01_variables_and_datatypes.py
│   │   ├── 02_operators.py
│   │   ├── 03_print_statements.py
│   │   └── 04_comments_and_structure.py
│   └── exercises/                  # Practice exercises for students
│       ├── exercise_01_variables.py
│       ├── exercise_02_calculations.py
│       ├── exercise_03_personal_info.py
│       └── SOLUTIONS.md           # Solutions for all exercises
│
└── [Future lectures will follow the same structure]
```

Each lecture follows a consistent structure:
- **README.md**: Comprehensive lecture guide with concepts and instructions
- **QUICK_START.md**: Quick reference for getting started
- **presentation.html**: Interactive slide presentation (uses global assets)
- **PRESENTATION_GUIDE.md**: How to use the HTML presentation
- **examples/**: Numbered Python files demonstrating each concept
- **exercises/**: Hands-on practice problems with solutions

Global shared resources:
- **assets/presentation/css/styles.css**: Global presentation styling (used by all lectures)
- **assets/presentation/js/presentation.js**: Global navigation script (used by all lectures)
- All presentations reference these files using relative paths: `../assets/presentation/`

## Development Setup

### Python Environment

- **Python Version**: 3.11 or later required
- **Virtual Environment**: Create with `python -m venv venv` and activate with `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Unix)
- **No External Dependencies**: Lecture 1 uses only Python standard library

### Running Course Materials

**Examples:**
```bash
# Run individual example files
python Lecture_1_Python_Basics_Setup/examples/01_variables_and_datatypes.py

# Run all examples in sequence
cd Lecture_1_Python_Basics_Setup/examples
python 01_variables_and_datatypes.py
python 02_operators.py
python 03_print_statements.py
python 04_comments_and_structure.py
```

**Exercises:**
```bash
# Students work on exercises by editing the files and running them
python Lecture_1_Python_Basics_Setup/exercises/exercise_01_variables.py
python Lecture_1_Python_Basics_Setup/exercises/exercise_02_calculations.py
python Lecture_1_Python_Basics_Setup/exercises/exercise_03_personal_info.py
```

## Course Design Principles

When creating new lectures or updating existing ones:

1. **Consistent Structure**: Follow the established pattern (README, QUICK_START, examples/, exercises/)
2. **Progressive Learning**: Each example builds on previous concepts
3. **Hands-on Practice**: Exercises reinforce concepts from examples
4. **Comprehensive Documentation**: Each Python file includes detailed comments explaining concepts
5. **Solutions Provided**: Include SOLUTIONS.md for student reference after completion
6. **Visual Output**: Examples and exercises produce clear, formatted output for immediate feedback

## Creating New Lectures

To add a new lecture, follow this template:

1. Create `Lecture_X_Topic_Name/` directory
2. Add `README.md` with installation, concepts, and navigation
3. Add `QUICK_START.md` with condensed instructions
4. Create `presentation.html` - interactive slide presentation for visual learners
   - **Link to global assets** using: `../assets/presentation/css/styles.css`
   - **Link to global script** using: `../assets/presentation/js/presentation.js`
5. Add `PRESENTATION_GUIDE.md` - instructions for using the presentation
6. Create `examples/` with numbered Python files (01_, 02_, etc.)
7. Create `exercises/` with practice problems and `SOLUTIONS.md`
8. Update this CLAUDE.md file with the new lecture structure

### Presentation Guidelines

The HTML presentations should:
- **Use global assets** - Link to `../assets/presentation/` for CSS and JS
- Include 15-25 slides covering all lecture topics
- Use syntax-highlighted code examples (classes defined in global CSS)
- Provide keyboard navigation (handled by global JS)
- Include visual elements (colored boxes, tables, two-column layouts)
- Feature a slide counter and navigation buttons (handled by global JS)
- Work offline in all modern browsers (no external dependencies)

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
