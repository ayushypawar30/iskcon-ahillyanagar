
import shutil
import os

source_dir = r"C:\Users\intel\.gemini\antigravity\brain\915a13de-741c-40d8-8d4b-ee99cc0cf806"
dest_dir = r"images"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

files = [
    ("uploaded_image_0_1766558602286.jpg", "gallery_uploaded_1.jpg"),
    ("uploaded_image_1_1766558602286.jpg", "gallery_uploaded_2.jpg"),
    ("uploaded_image_2_1766558602286.jpg", "gallery_uploaded_3.jpg"),
    ("uploaded_image_3_1766558602286.jpg", "gallery_uploaded_4.jpg"),
    ("uploaded_image_4_1766558602286.jpg", "gallery_uploaded_5.jpg"),
]

for src_name, dest_name in files:
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    try:
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_name} to {dest_name}")
    except Exception as e:
        print(f"Error copying {src_name}: {e}")
