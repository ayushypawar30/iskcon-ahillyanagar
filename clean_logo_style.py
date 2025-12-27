
import glob
import re

files = glob.glob('*.html')

# Regex to match the inline style on the logo image
# <img src="images/logo.png" alt="ISKCON Logo" style="...">
# We want to remove the style="..." part or replace the whole tag efficiently

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Flexible regex to find the logo img tag and strip its inline style
    # Looking for: <img src="images/logo.png" alt="ISKCON Logo" style="...">
    # Replacement: <img src="images/logo.png" alt="ISKCON Logo">
    
    # Note: We used single quotes in the update_logo.py script, but let's be safe with regex
    # Pattern: match <img src="images/logo.png" ... style="..." ... >
    
    def replacer(match):
        full_tag = match.group(0)
        # Remove style="..."
        cleaned = re.sub(r'\s*style="[^"]*"', '', full_tag)
        return cleaned

    # Search for the specific logo image tag
    new_content = re.sub(r'<img\s+src="images/logo\.png"[^>]*>', replacer, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned {file_path}")
    else:
        print(f"No changes in {file_path}")
