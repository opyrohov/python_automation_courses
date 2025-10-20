# Global Presentation Assets

This folder contains **shared CSS and JavaScript files** used by all lecture presentations throughout the Python Automation Course.

## 📁 Folder Structure

```
assets/presentation/
├── css/
│   └── styles.css         # Global presentation styling
├── js/
│   └── presentation.js    # Global navigation and interactivity
└── README.md             # This file
```

## 🎯 Purpose

Instead of duplicating CSS and JavaScript files in each lecture folder, we maintain a single source of truth here. This approach provides:

- **Consistency**: All presentations look and behave the same way
- **Maintainability**: Update styles or features in one place
- **Efficiency**: Smaller repository size (no duplication)
- **Standards**: Single source for presentation best practices

## 📄 Files

### css/styles.css

The master stylesheet for all presentations containing:

**Layout & Structure**
- Slide positioning and sizing
- Navigation button placement
- Slide counter styling

**Visual Design**
- Color scheme (purple gradient theme)
- Typography (fonts, sizes, line heights)
- Spacing and padding
- Animations and transitions

**Components**
- Code blocks with syntax highlighting
- Info/warning/success boxes
- Tables and lists
- Two-column layouts
- Checklists

**Syntax Highlighting**
- `.comment` - Green (#75715e)
- `.string` - Yellow (#e6db74)
- `.number` - Purple (#ae81ff)
- `.keyword` - Pink (#f92672)
- `.function` - Cyan (#66d9ef)

### js/presentation.js

The master JavaScript file providing:

**Navigation**
- `showSlide(n)` - Display slide at index n
- `changeSlide(direction)` - Move forward/backward
- `goToFirstSlide()` - Jump to first slide
- `goToLastSlide()` - Jump to last slide

**Keyboard Shortcuts**
- `→` or `PageDown` - Next slide
- `←` or `PageUp` - Previous slide
- `Home` - First slide
- `End` - Last slide
- `Escape` - Reserved for future use

**Touch Support**
- Swipe left - Next slide
- Swipe right - Previous slide
- Configurable swipe threshold (50px)

**UI Updates**
- Slide counter display
- Button state management (disable at ends)
- Scroll to top on slide change

## 🔗 Usage in Lectures

Each lecture's `presentation.html` should include:

```html
<!-- In the <head> section -->
<link rel="stylesheet" href="../assets/presentation/css/styles.css">

<!-- At the end of <body> section -->
<script src="../assets/presentation/js/presentation.js"></script>
```

**Note:** The `..` in the path goes up one directory level from the lecture folder to the repository root.

### Example Directory Structure

```
python_automation_courses/
├── assets/
│   └── presentation/
│       ├── css/styles.css
│       └── js/presentation.js
├── Lecture_1_Python_Basics_Setup/
│   └── presentation.html  (uses ../assets/presentation/...)
├── Lecture_2_Control_Flow/
│   └── presentation.html  (uses ../assets/presentation/...)
└── Lecture_3_Functions/
    └── presentation.html  (uses ../assets/presentation/...)
```

## 🛠️ Customization

### Global Changes (Affect All Lectures)

To change the look or behavior of **ALL** presentations:

1. **Modify styles:** Edit `css/styles.css`
2. **Add features:** Edit `js/presentation.js`
3. **Test changes:** Open any `presentation.html` in a browser
4. **Verify:** Check multiple lectures to ensure consistency

### Lecture-Specific Customization

If a specific lecture needs unique styling:

1. Add a `<style>` block in that lecture's HTML
2. Use more specific CSS selectors to override global styles
3. Document the reason for the custom styling

**Example:**
```html
<!-- In a specific lecture's presentation.html -->
<style>
    /* Lecture-specific override */
    .slide {
        background: #f0f0f0; /* Different background for this lecture */
    }
</style>
```

## 🎨 Color Scheme

The presentations use a consistent color palette:

- **Primary Purple:** `#667eea`
- **Secondary Purple:** `#764ba2`
- **Success Green:** `#28a745`
- **Info Blue:** `#17a2b8`
- **Warning Yellow:** `#ffc107`
- **Light Gradient:** `#84fab0` to `#8fd3f4`

### Code Block Colors (Monokai-inspired)
- **Background:** `#2d2d2d`
- **Text:** `#f8f8f2`
- **Comments:** `#75715e`
- **Strings:** `#e6db74`
- **Numbers:** `#ae81ff`
- **Keywords:** `#f92672`
- **Functions:** `#66d9ef`

## 📏 Standards

### Slide Structure

Each presentation should follow this HTML structure:

```html
<div class="presentation">
    <div class="slide-counter">
        <span id="currentSlide">1</span> / <span id="totalSlides">20</span>
    </div>

    <div class="slide active">
        <!-- First slide content -->
    </div>

    <div class="slide">
        <!-- Second slide content -->
    </div>

    <!-- More slides... -->
</div>

<div class="navigation">
    <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)">← Previous</button>
    <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)">Next →</button>
</div>
```

### CSS Classes Reference

- `.slide` - Individual slide container
- `.slide.active` - Currently visible slide
- `.title-slide` - Special layout for title slides
- `.code-block` - Code examples with syntax highlighting
- `.info-box` - Blue information boxes
- `.warning-box` - Yellow warning boxes
- `.success-box` - Green success boxes
- `.two-column` - Two-column grid layout
- `.checklist` - List with checkmarks
- `.highlight` - Highlighted text with gradient

## 🔄 Version Control

When updating global assets:

1. **Test thoroughly** - Changes affect all lectures
2. **Document changes** - Update this README if needed
3. **Commit with clear message** - Explain what changed and why
4. **Check all lectures** - Verify nothing broke

## 🚀 Best Practices

### For Instructors/Content Creators

1. **Use existing classes** - Don't create custom styles unless necessary
2. **Follow the color scheme** - Maintains visual consistency
3. **Test in multiple browsers** - Chrome, Firefox, Edge, Safari
4. **Keep slides simple** - 1-2 concepts per slide
5. **Use code blocks** - Syntax highlighting makes code readable

### For Developers

1. **Comment your changes** - Explain why, not just what
2. **Keep it lightweight** - No external dependencies
3. **Mobile-first** - Test on various screen sizes
4. **Accessibility** - Consider color contrast and font sizes
5. **Performance** - Optimize animations and transitions

## 📦 Dependencies

**None!** These files are completely self-contained:
- No external libraries required
- No internet connection needed
- Works offline
- Compatible with all modern browsers

## 🤝 Contributing

When improving the global assets:

1. Discuss major changes with the team
2. Test across different lectures
3. Update this README if adding new features
4. Consider backward compatibility
5. Document any breaking changes

---

**Last Updated:** Created for Python Automation Course v1.0
**Maintained By:** Course Development Team
**Questions?** Check lecture-specific `PRESENTATION_GUIDE.md` files
