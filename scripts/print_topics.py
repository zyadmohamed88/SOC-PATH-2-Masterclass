import json

with open('document_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i, item in enumerate(items):
    if item['text']:
        print(f"[{i:03d}] {item['text']}")
