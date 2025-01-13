# src/summarizer/utils.py

def extract_from_url(url):
    return f"Extracted content from {url}"

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()