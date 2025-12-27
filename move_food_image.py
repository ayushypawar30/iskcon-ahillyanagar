
import shutil
import os

source = r"C:\Users\intel\.gemini\antigravity\brain\915a13de-741c-40d8-8d4b-ee99cc0cf806\uploaded_image_1766561143875.jpg"
dest = r"images\food_distribution_real.jpg"

try:
    if os.path.exists(source):
        shutil.copy2(source, dest)
        print(f"Successfully copied {source} to {dest}")
    else:
        print(f"Source file NOT FOUND: {source}")
except Exception as e:
    print(f"Error copying file: {e}")
