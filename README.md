# Folder Size Scanner
A Python script that scans folders and calculates their total size by summing up the sizes of all files inside.

## How to Use
1. Install Python.
2. Install Tkinter if it is not already installed (required for the file dialog window):
   ```sh
   pip install tk
   ```
3. Run the script:
   ```sh
   python getsize.py
   ```
4. Provide a folder path either:
   - As a command-line argument.
   - Through the file selection dialog window.

## How It Works
- The directory path can be provided via command-line arguments or selected using a GUI file dialog.
- The program uses `os.walk()` to traverse the directory.
- Files inside the directory are structured in a tree-like format where each node represents a file.
- The size of each file is determined using `os.path.getsize()` and summed up for the respective folder.
- The total size of the folder is displayed in the console.

## Notes
- Tested on Windows.
- May require adjustments for Linux/macOS (because of differences in file path handling).
