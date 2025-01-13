# src/cli/cli_script.py

# Relative Imports   
# python -m src.cli.cli_script 
#from ..summarizer.summarizer import process_text
#from ..summarizer.utils import extract_from_url, read_file

# python src/cli/cli_script.py with set PYTHONPATH=.
from src.summarizer.summarizer import process_text
from src.summarizer.utils import extract_from_url, read_file

def main():
    text = "Hello, World!"
    url = "http://example.com"
    print(process_text(text))
    print(extract_from_url(url))

if __name__ == "__main__":
    main()