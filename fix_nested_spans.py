import re
import sys
from pathlib import Path

def fix_nested_spans(html_content):
    """Fix nested span tags caused by previous buggy conversion"""

    # Pattern 1: <span <span class="keyword">class</span>="keyword">for</span>
    # Should be: <span class="keyword">for</span>
    html_content = re.sub(
        r'<span <span class="keyword">class</span>="([^"]+)">([^<]+)</span>',
        r'<span class="\1">\2</span>',
        html_content
    )

    # Pattern 2: <span <span class="keyword">class</span>="number">0</span>
    # Should be: <span class="number">0</span>
    html_content = re.sub(
        r'<span <span class="[^"]+">class</span>="([^"]+)">([^<]+)</span>',
        r'<span class="\1">\2</span>',
        html_content
    )

    return html_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python fix_nested_spans.py <file_path>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: {file_path} not found")
        sys.exit(1)

    print(f"Fixing {file_path}...")

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix nested spans
    new_content = fix_nested_spans(content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Done! Fixed {file_path}")


if __name__ == "__main__":
    main()
