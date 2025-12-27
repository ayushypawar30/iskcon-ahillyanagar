
import shutil
import os

# Source is the third uploaded image (Acharya)
source = r"C:\Users\intel\.gemini\antigravity\brain\915a13de-741c-40d8-8d4b-ee99cc0cf806\uploaded_image_1766560313863.jpg"
dest = r"images\prabhupada_nav.jpg"

try:
    if os.path.exists(source):
        shutil.copy2(source, dest)
        print(f"Successfully swapped image to {dest}")
    else:
        print(f"Source file not found: {source}")
except Exception as e:
    print(f"Error copying file: {e}")
