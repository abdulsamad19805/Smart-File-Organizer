# Smart File Organizer

A lightweight, automated Python utility designed to clean up messy directories (like your `Downloads` or `Desktop` folders) by intelligently categorizing loose files into structured subdirectories based on their file extensions.

** Features

** Smart Directory Routing: Automatically groups development files (`.java`, `.py`), documentation (`.pdf`), and archives (`.zip`) into dedicated folders.

** Collision Prevention: Dynamically handles duplicate filenames by automatically appending a unique counter instead of overwriting existing files.

** Folder Safety: Safely ignores existing directories to preserve structural project folders.

** Fallback Catch-All: Routes unrecognized file types into an `Other/` directory for safe keeping.

** How It Works
The core allocation engine evaluates the extension of each loose file in the target directory and matches it against a mapped routing dictionary:

| File Extension | Target Destination Folder |
| :--- | :--- |
| `.java` | `Development/Java/` |
| `.py` | `Development/Python/` |
| `.pdf` | `Documents/PDFs/` |
| `.zip` | `Archives/` |
| Unrecognized | `Other/` |

** Usage
Run the script directly from your terminal using Python 3:

```bash
python3 fileOrganizer.py