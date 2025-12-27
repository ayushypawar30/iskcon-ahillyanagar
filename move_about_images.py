
import shutil
import os

files = [
    (r"C:\Users\intel\.gemini\antigravity\brain\915a13de-741c-40d8-8d4b-ee99cc0cf806\uploaded_image_0_1766560858294.jpg", "images\prabhupada_real.jpg"),
    (r"C:\Users\intel\.gemini\antigravity\brain\915a13de-741c-40d8-8d4b-ee99cc0cf806\uploaded_image_1_1766560858294.jpg", r"images\food_distribution_real.jpg")
]

for src, dest in files:
    try:
        if os.path.exists(src):
            shutil.copy2(src, dest)
            print(f"Copied {src} to {dest}")
        else:
            print(f"Source not found: {src}")
    except Exception as e:
        print(f"Error copying {src}: {e}")
