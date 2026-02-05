import re

def extract_title(text):
    parts = text.strip().split("\n\n", 2)
    title = parts[0] if len(parts) > 0 else None
    return title
    
def extract_description(text):
    parts = text.strip().split("\n\n", 2)
    description = parts[1] if len(parts) > 1 else None
    return description

def extract_price(text):
    match = re.search(r'(\d+)\s*ETB', text)
    return match.group(0) if match else None