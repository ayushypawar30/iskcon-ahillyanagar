
import os

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The link to add
admin_link = '\n                    <p style="margin-top: 15px; font-size: 0.8rem;"><a href="admin.html" style="color: #999; text-decoration: none;">Admin Login</a></p>'

# Find the insertion point: after the newsletter div
# The newsletter div contains the form
target_str = '</form>'
idx = content.find(target_str)

if idx != -1:
    # Find the next closing div after form
    next_div_idx = content.find('</div>', idx)
    if next_div_idx != -1:
        # Insert after this div
        insert_pos = next_div_idx + 6 # len('</div>')
        new_content = content[:insert_pos] + admin_link + content[insert_pos:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully added Admin Login link.")
    else:
        print("Could not find closing div for newsletter.")
else:
    print("Could not find newsletter form.")
