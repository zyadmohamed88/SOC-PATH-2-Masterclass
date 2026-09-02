import os
import glob
from PIL import Image
import io
import base64

images = sorted(glob.glob('extracted_images/*'))
sample = images[:10]

total_b64_len = 0
for img_path in images:
    with Image.open(img_path) as im:
        # Convert RGBA to RGB if saving to JPEG/WebP
        if im.mode in ("RGBA", "P"):
            im_rgb = im.convert("RGB")
        else:
            im_rgb = im
        
        buf = io.BytesIO()
        # Save as WebP quality 82 for extreme compression and crystal clear quality
        im_rgb.save(buf, format="WEBP", quality=82, method=4)
        b64_str = base64.b64encode(buf.getvalue()).decode('utf-8')
        total_b64_len += len(b64_str)

print(f"Total WebP Base64 size for all 907 images: {total_b64_len / (1024*1024):.2f} MB")
