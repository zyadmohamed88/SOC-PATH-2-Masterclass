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

elements = []
for p in doc_root.iter(f'{{{w_ns}}}p'):
    p_text = ''.join([t.text for t in p.iter(f'{{{w_ns}}}t') if t.text]).strip()
    p_imgs = []
    for blip in p.iter(f'{{{a_ns}}}blip'):
        embed = blip.attrib.get(f'{{{r_ns}}}embed')
        if embed in rel_map:
            p_imgs.append(rel_map[embed])
    
    if p_text or p_imgs:
        elements.append({
            'text': p_text,
            'imgs': p_imgs
        })

print(f"Total sequential elements: {len(elements)}")

# Group into sections
sections = []
current_sec = None
current_sub = None

for el in elements:
    txt = el['text']
    imgs = el['imgs']
    
    # Heuristics for headings
    # Main sections: numbered like "1- LOG Analysis", "2. Advanced Splunk", etc.
    if txt and any(txt.startswith(prefix) for prefix in ['1-', '2.', '3.', '4.', '5.', '6.', '1.']) and len(txt) < 80:
        # Check if it's a major topic
        pass
    
    if txt:
        if not current_sec or len(txt) < 60 and not txt.startswith('-') and ('SOC' in txt or 'Analysis' in txt or 'Splunk' in txt or 'ELK' in txt or 'Detection' in txt or 'Threat' in txt or 'Cloud' in txt or 'Wazuh' in txt or 'Malware' in txt or 'Traffic' in txt or 'Incident' in txt or 'Intelligence' in txt or 'Microsoft' in txt):
            current_sec = {
                'title': txt,
                'subsections': []
            }
            sections.append(current_sec)
            current_sub = {
                'title': 'Overview',
                'items': []
            }
            current_sec['subsections'].append(current_sub)
        elif current_sec and len(txt) < 100:
            current_sub = {
                'title': txt,
                'items': []
            }
            current_sec['subsections'].append(current_sub)
        else:
            if not current_sec:
                current_sec = {'title': 'General SOC Content', 'subsections': []}
                sections.append(current_sec)
                current_sub = {'title': 'General', 'items': []}
                current_sec['subsections'].append(current_sub)
            current_sub['items'].append({'type': 'text', 'content': txt})

    for img in imgs:
        if not current_sec:
            current_sec = {'title': 'General SOC Content', 'subsections': []}
            sections.append(current_sec)
            current_sub = {'title': 'General', 'items': []}
            current_sec['subsections'].append(current_sub)
        if not current_sub:
            current_sub = {'title': 'Screenshots', 'items': []}
            current_sec['subsections'].append(current_sub)
        current_sub['items'].append({'type': 'img', 'src': img})

print(f"Extracted {len(sections)} sections.")
for s in sections:
    total_imgs = sum(sum(1 for item in sub['items'] if item['type'] == 'img') for sub in s['subsections'])
    print(f"Section: {s['title']} | Subsections: {len(s['subsections'])} | Images: {total_imgs}")
