## Here is the directory structure for a testing package:

```bash
package-relative-import-test
└── src
    ├── __init__.py
    ├── cli
    │   ├── __init__.py
    │   └── cli_script.py
    └── summarizer
        ├── __init__.py
        ├── summarizer.py
        └── utils.py
```

To run the script using its relative module path correctly, you need to adjust your command.

## Here is a step-by-step guide:

### Option 1: Using -m Option
Navigate to the root directory of your project/package:

```bash
cd package-relative-import-test
python -m src.cli.cli_script
```

```bash
# src/cli/cli_script.py
 
from ..summarizer.summarizer import process_text
from ..summarizer.utils import extract_from_url, read_file

def main():
    text = "Hello, World!"
    url = "http://example.com"
    print(process_text(text))
    print(extract_from_url(url))

if __name__ == "__main__":
    main()
```

### Option 2: Direct Script Execution with Adjusted Paths
If you want to run the script directly without the -m option, you need to adjust the PYTHONPATH and use the correct file path:

#### In the root directory
```bash
cd package-relative-import-test
export PYTHONPATH=.:$PYTHONPATH
python src/cli/cli_script.py
```

```bash
# src/cli/cli_script.py

from src.summarizer.summarizer import process_text
from src.summarizer.utils import extract_from_url, read_file

def main():
    text = "Hello, World!"
    url = "http://example.com"
    print(process_text(text))
    print(extract_from_url(url))

if __name__ == "__main__":
    main()
```

#### Navigate to the src/cli directory:

```bash
cd package-relative-import-test/src/cli
export PYTHONPATH=../..:$PYTHONPATH
python cli_script.py
```


Explanation
Using -m Option: This treats src.cli.cli_script as a module and runs it within the **package** context, allowing Python to resolve the relative imports correctly.

Direct Script Execution: By setting PYTHONPATH to include the parent directory of src, Python can resolve the package structure and relative imports when running cli_script.py directly.

Choose the option that best fits your workflow. Using the -m option is generally recommended for running scripts within a package.
