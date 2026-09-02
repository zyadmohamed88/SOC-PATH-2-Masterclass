import os
import glob
from PIL import Image

images = glob.glob('extracted_images/*')
print(f"Total extracted images: {len(images)}")

total_raw_bytes = sum(os.path.getsize(f) for f in images)
print(f"Total raw size of images: {total_raw_bytes / (1024*1024):.2f} MB")
