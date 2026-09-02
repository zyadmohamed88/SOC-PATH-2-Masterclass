import json
import os
import io
import base64
import time
from PIL import Image

start_time = time.time()
print("Starting HTML generation script...")

# Load raw document items
with open('document_raw.json', 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Cache directory for base64 webp images
cache_dir = 'b64_cache'
os.makedirs(cache_dir, exist_ok=True)

def get_b64_image(img_name):
    cache_file = os.path.join(cache_dir, img_name + '.b64')
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    img_path = os.path.join('extracted_images', img_name)
    if not os.path.exists(img_path):
        return ""
    
    try:
        with Image.open(img_path) as im:
            if im.mode in ("RGBA", "P"):
                im_rgb = im.convert("RGB")
            else:
                im_rgb = im
            
            buf = io.BytesIO()
            im_rgb.save(buf, format="WEBP", quality=80, method=3)
            b64_str = "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode('utf-8')
            
            with open(cache_file, 'w', encoding='utf-8') as f:
                f.write(b64_str)
            return b64_str
    except Exception as e:
        print(f"Error processing {img_name}: {e}")
        return ""

print("Pre-caching image Base64 data (this runs once)...")
# Process all extracted images
all_imgs = sorted(os.listdir('extracted_images'))
count = 0
for img_name in all_imgs:
    get_b64_image(img_name)
    count += 1
    if count % 100 == 0:
        print(f"Processed {count}/{len(all_imgs)} images...")

print(f"All {len(all_imgs)} images converted to WebP Base64 in cache.")
print(f"Time taken so far: {time.time() - start_time:.2f} seconds.")
