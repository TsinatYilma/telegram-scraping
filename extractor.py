import re

def extract_title(text):
    parts = text.strip().split("\n\n", 2)
    title = parts[0] if len(parts) > 0 else None
    return title
    
def extract_description(text):
    parts = text.strip().split("\n\n", 2)
    description = parts[1] if len(parts) > 1 else None
    return description

def extract_date(text):
    match = re.search(r"🗓 Date:\s*(.+)", text)
    return match.group(1).strip() if match else None

def extract_location(text):
    match = re.search(r"📍 Event Location:\s*(.+)", text)
    return match.group(1).strip() if {match} else None

def extract_city(text):
    match = re.search(r"🏙 Event In:\s*(.+)", text)
    return match.group(1).strip() if match else None

def extract_pricing(text):
    match = re.search(r"• Per Person:\s*([\d,]+ ETB)", text)
    return match.group(1).strip() if match else None

def extract_contact(text):
    match = re.search(r"📞 Ticket Info:\s*(.+)", text)
    return match.group(1).strip() if match else None
