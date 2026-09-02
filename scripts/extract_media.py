import zipfile
import xml.etree.ElementTree as ET
import os
import json
import base64
from io import BytesIO
from PIL import Image

docx_path = 'SOC PATH 2.docx'
output_img_dir = 'extracted_images'
os.makedirs(output_img_dir, exist_ok=True)

# Remove temp file if present
if os.path.exists('~$C PATH 2.docx'):
    try:
        os.remove('~$C PATH 2.docx')
        print("Removed temporary file ~$C PATH 2.docx")
    except Exception as e:
        print(f"Could not remove temp file: {e}")

print("Extracting media files from DOCX...")
with zipfile.ZipFile(docx_path) as z:
    media_files = [f for f in z.namelist() if f.startswith('word/media/')]
    print(f"Found {len(media_files)} images in DOCX archive.")
    
    # Extract all images to extracted_images folder
    for mf in media_files:
        filename = os.path.basename(mf)
        dest_path = os.path.join(output_img_dir, filename)
        with open(dest_path, 'wb') as f_out:
            f_out.write(z.read(mf))

print(f"All {len(media_files)} images extracted to '{output_img_dir}'.")
