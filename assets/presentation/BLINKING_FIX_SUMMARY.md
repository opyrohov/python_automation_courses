# Blinking Issue - Complete Fix

## The Problem
When clicking "Next" or using keyboard navigation, the first slide would briefly flash/blink before showing the correct slide.

## Root Cause
The issue was caused by using `display: none` and `display: block` to hide/show slides:

```css
/* OLD - BUGGY */
.slide { display: none; }
.slide.active { display: block; }
```

When switching slides:
1. Old slide gets `display: none` (immediately disappears)
2. New slide gets `display: block` (starts appearing)
3. During this switch, there's a brief moment where rendering causes a flash
4. The browser has to recalculate layout (reflow)
5. This can cause the first slide to briefly appear

## The Solution

### Changed from `display` to `opacity` + `visibility`

```css
/* NEW - FIXED */
.slide {
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease-in-out, visibility 0s 0.3s;
    z-index: 1;
}

.slide.active {
    opacity: 1;
    visibility: visible;
    transition: opacity 0.3s ease-in-out, visibility 0s 0s;
    z-index: 2;
}
```

### Why This Works

1. **All slides stay in the DOM** - No layout reflow from display changes
2. **Smooth opacity transition** - Slides fade in/out smoothly
3. **z-index layering** - Active slide (z-index: 2) appears on top of others (z-index: 1)
4. **visibility for accessibility** - Hidden slides are not interactive
5. **Proper transition timing** - visibility changes at the right moment

### Visual Explanation

**Before (Buggy):**
```
Slide 1 (display: block) → display: none → [FLASH/NOTHING] → Slide 2 (display: block)
                                            ↑ Brief moment causing flash
```

**After (Fixed):**
```
Slide 1 (opacity: 1, z-index: 2)
                ↓ Smooth crossfade (0.3s)
Slide 2 (opacity: 0→1, z-index: 2)

During transition, Slide 1 fades out while Slide 2 fades in
Both exist simultaneously, creating smooth transition
```

## JavaScript Improvements

Also fixed the order of operations:

```javascript
// BEFORE - Wrong order
slides[currentSlide].classList.remove('active'); // Uses old index!
currentSlide = n; // Updates AFTER

// AFTER - Correct order
const oldSlide = currentSlide; // Store old
currentSlide = n; // Update first
slides[oldSlide].classList.remove('active'); // Use correct index
slides[currentSlide].classList.add('active');
```

Added transition guard to prevent rapid clicks:

```javascript
let isTransitioning = false;

function showSlide(n) {
    if (isTransitioning) return; // Block rapid navigation
    isTransitioning = true;

    // ... do transition ...

    setTimeout(() => {
        isTransitioning = false;
    }, 350); // After 300ms transition
}
```

## Testing

Open `presentation.html` and test:

1. **Single click** - Should smoothly fade to next slide
2. **Rapid clicks** - Should not cause flickering (blocked by guard)
3. **Keyboard navigation** - Arrow keys should work smoothly
4. **Jump navigation** - Home/End should fade properly
5. **No blinking** - First slide should never flash

## Technical Details

### CSS Transitions vs Animations

**Animations (old approach):**
- Triggered on class add
- Can be interrupted awkwardly
- Harder to control timing

**Transitions (new approach):**
- Smooth property changes
- Better for state changes
- Easier to control with delays

### Visibility Timing

```css
/* When hiding */
visibility: hidden;
transition: visibility 0s 0.3s; /* Delay 0.3s - stays visible during fade */

/* When showing */
visibility: visible;
transition: visibility 0s 0s; /* No delay - immediately visible */
```

This ensures:
- When fading out, slide stays visible during opacity transition
- When fading in, slide becomes visible immediately

### Z-Index Layering

- **Inactive slides**: z-index: 1
- **Active slide**: z-index: 2

During transition:
- New slide (becoming active) has z-index: 2, appears on top
- Old slide (becoming inactive) has z-index: 1, below
- Smooth crossfade effect

## Files Modified

1. **assets/presentation/css/styles.css**
   - Completely redesigned slide visibility approach
   - Removed display-based hiding
   - Added opacity/visibility transitions
   - Added z-index layering

2. **assets/presentation/js/presentation.js**
   - Fixed showSlide() logic order
   - Added transition guard
   - Updated timeout to match CSS

## Result

✅ **No more blinking** - Smooth, professional transitions
✅ **Better performance** - No layout reflow
✅ **Cleaner code** - Proper state management
✅ **Prevents bugs** - Transition guard blocks issues
✅ **Works globally** - All lectures automatically fixed

## If Issue Persists

If you still see blinking, check:

1. **Browser cache** - Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
2. **File paths** - Ensure CSS/JS files are loading correctly
3. **Browser console** - Check for any errors
4. **CSS override** - Look for any custom styles that might interfere

Try opening DevTools (F12) → Network tab → Refresh page → Verify:
- `styles.css` loads (should be ~420 lines)
- `presentation.js` loads (should be ~160 lines)
- No 404 errors

## Version
- **Created:** 2024-10-20
- **Status:** Production
- **Applies to:** All presentations using global assets
