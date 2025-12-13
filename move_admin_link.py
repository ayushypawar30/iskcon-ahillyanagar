
import os

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The link to add
admin_link = '\n                <p style="margin-top: 10px; font-size: 0.8rem;"><a href="admin.html" style="color: #666; text-decoration: none;">Admin Login</a></p>'

# Find the insertion point: after the copyright paragraph
target_str = '&copy; 2025 ISKCON Ahilyanagar. All rights reserved.</p>'
idx = content.find(target_str)

if idx != -1:
    # Insert after the closing </p>
    insert_pos = idx + len(target_str)
    new_content = content[:insert_pos] + admin_link + content[insert_pos:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully added Admin Login link.")
else:
    print("Could not find copyright text.")
