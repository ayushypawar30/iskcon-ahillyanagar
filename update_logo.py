
import glob
import os

files = glob.glob('*.html')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update logo path
    new_content = content.replace('images/iskcon_logo.png', 'images/logo.png')
    
    # 2. Specific fix for admin.html
    if 'admin.html' in file_path:
        # Remove the text header <h2>ISKCON Admin</h2>
        # We also might want to remove the <i> tag if it exists, but grep showed it might have been replaced by img
        # Let's just remove the specific h2 line or tag
        new_content = new_content.replace('<h2>ISKCON Admin</h2>', '')
        # Also cleanup simple icons if they were next to it (legacy)
        new_content = new_content.replace('<i class="fas fa-om"></i>', '') 
        
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes in {file_path}")
