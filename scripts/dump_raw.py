import zipfile
import xml.etree.ElementTree as ET
import json
import os

docx_path = 'SOC PATH 2.docx'

with zipfile.ZipFile(docx_path) as z:
    doc_xml = z.read('word/document.xml')
    rels_xml = z.read('word/_rels/document.xml.rels')

rels_root = ET.fromstring(rels_xml)
rel_map = {r.attrib['Id']: r.attrib['Target'] for r in rels_root}

doc_root = ET.fromstring(doc_xml)
w_ns = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
a_ns = 'http://schemas.openxmlformats.org/drawingml/2006/main'
r_ns = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'

items = []
for p in doc_root.iter(f'{{{w_ns}}}p'):
    p_text = ''.join([t.text for t in p.iter(f'{{{w_ns}}}t') if t.text]).strip()
    p_imgs = []
    for blip in p.iter(f'{{{a_ns}}}blip'):
        embed = blip.attrib.get(f'{{{r_ns}}}embed')
        if embed in rel_map:
            img_file = os.path.basename(rel_map[embed])
            p_imgs.append(img_file)
    
    if p_text or p_imgs:
        items.append({
            'text': p_text,
            'imgs': p_imgs
        })

print(f"Total sequential items: {len(items)}")

# Save to JSON
with open('document_raw.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved raw items to document_raw.json")
