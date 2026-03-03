# Global Assets

This folder contains shared resources used across multiple lectures in the Python Automation Course.

## 📁 Structure

```
assets/
├── presentation/          # Shared presentation resources
│   ├── css/
│   │   └── styles.css    # Global presentation styling
│   ├── js/
│   │   └── presentation.js # Global navigation script
│   └── README.md         # Detailed presentation assets documentation
└── README.md             # This file
```

## 🎯 Purpose

The assets folder serves as a centralized location for shared resources, promoting:

- **Reusability** - Use the same files across multiple lectures
- **Consistency** - Ensure uniform look and behavior
- **Maintainability** - Update in one place, affect all lectures
- **Efficiency** - Reduce duplication and repository size

## 📦 Current Assets

### Presentation Assets

Located in `presentation/`, these files power the interactive HTML slide presentations:

- **CSS** - Styling, layout, animations, syntax highlighting
- **JavaScript** - Navigation, keyboard shortcuts, touch support

All lectures that include HTML presentations should link to these global files.

**Usage Example:**
```html
<link rel="stylesheet" href="../assets/presentation/css/styles.css">
<script src="../assets/presentation/js/presentation.js"></script>
```

See `presentation/README.md` for detailed documentation.

## 🔮 Future Assets

As the course grows, this folder may include:

- **Images** - Common diagrams, logos, icons
- **Fonts** - Custom typography
- **Templates** - Reusable HTML/markdown templates
- **Data** - Sample datasets for exercises
- **Scripts** - Utility scripts for course management

## 🛠️ Guidelines

### Adding New Assets

When adding new shared assets:

1. **Create appropriate subfolder** - Organize by asset type
2. **Document usage** - Add README explaining how to use
3. **Use relative paths** - Ensure portability across systems
4. **Test thoroughly** - Verify works from all lecture locations
5. **Update documentation** - Keep this README current

### Naming Conventions

- Use lowercase with hyphens: `presentation-theme.css`
- Be descriptive: `python-logo.svg` not `img1.svg`
- Version if needed: `styles-v2.css`
- Group related files in subfolders

### File Organization

```
assets/
├── [type]/               # Asset type (presentation, images, etc.)
│   ├── [subtype]/       # Optional subcategory
│   │   └── files...
│   └── README.md        # Documentation for this asset type
└── README.md            # This file
```

## 🔗 Integration

### From Lecture Folders

Lectures reference global assets using relative paths:

```
Lecture_X/presentation.html  →  ../assets/presentation/css/styles.css
```

The `..` goes up one level from the lecture folder to the repository root.

### Path Examples

```
From: Lecture_1_Python_Basics_Setup/presentation.html
To:   assets/presentation/css/styles.css
Path: ../assets/presentation/css/styles.css

From: Lecture_2_Control_Flow/presentation.html
To:   assets/presentation/js/presentation.js
Path: ../assets/presentation/js/presentation.js
```

## 📏 Standards

### Version Control

- **Commit carefully** - Changes affect multiple lectures
- **Test before commit** - Verify all lectures still work
- **Use clear messages** - Explain what changed and why
- **Tag releases** - Version significant updates

### Best Practices

1. **Keep it lean** - Only include truly shared resources
2. **Document everything** - Future maintainers will thank you
3. **No external dependencies** - Keep course self-contained
4. **Cross-platform** - Test on Windows, Mac, Linux
5. **Backward compatible** - Don't break existing lectures

## 🚀 Quick Reference

### For Content Creators

- **Creating presentations?** → Use `presentation/` assets
- **Need custom styling?** → Override in lecture-specific files
- **Found a bug?** → Fix once in assets, benefits all lectures

### For Developers

- **Adding new asset type?** → Create subfolder with README
- **Updating existing?** → Test all lectures afterward
- **Major changes?** → Discuss with team first

## 📚 Documentation

- **Presentation Assets:** See `presentation/README.md`
- **Course Structure:** See `/CLAUDE.md` in repository root
- **Individual Lectures:** See lecture-specific README files

## 🤝 Contributing

When contributing to global assets:

1. Ensure changes benefit multiple lectures
2. Document new assets thoroughly
3. Test across different environments
4. Update relevant README files
5. Consider backward compatibility

---

**Note:** This folder structure follows web development best practices for shared resources, making the course easier to maintain and extend.
