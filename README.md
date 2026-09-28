# Smart File Organizer

A Python desktop application that automatically organizes files into categories based on their file types.

## Features

- Automatically detects and organizes files
- Supports multiple file extensions
- Classifies files into Documents, Images, Videos, Audio, Archives, Programs, and Other
- Provides a graphical user interface (GUI) using Tkinter
- Allows users to select folders using a folder picker
- Displays a preview before organizing files
- Asks for confirmation before moving files
- Automatically creates category folders
- Prevents duplicate filenames by automatically renaming files
- Handles file-moving errors without crashing the program
- Handles empty folders safely
- Shows an organization summary by category
- Reports successfully organized and failed files
- Supports uppercase and lowercase file extensions

## Screenshots

### File Preview

![Smart File Organizer Preview](screenshots/gui-preview.png)

### Organization Summary

![Organization Summary](screenshots/summary.png)

## How It Works

1. Select a folder to organize.
2. The program scans the files inside the selected folder.
3. Each file is classified based on its file extension.
4. A preview shows the category of each file.
5. The user confirms whether to organize the files.
6. Files are moved into their corresponding category folders.
7. A summary displays the organization results.

## Categories

- Documents
- Images
- Videos
- Audio
- Archives
- Programs
- Other

## How to Run

### Windows Executable

Download and run:

`Smart File Organizer.exe`

No Python installation is required.

### Run with Python

Make sure Python is installed, then run:

```bash
python gui.py
```

## Built With

- Python
- pathlib
- Tkinter
- PyInstaller
- Git
- GitHub

## What I Learned

Through this project, I learned about:

- Python file system operations
- Working with `pathlib`
- Functions and reusable code
- Lists and dictionaries
- File extension classification
- Error handling with `try/except`
- Building graphical interfaces with Tkinter
- Handling duplicate filenames safely
- Git and GitHub version control
- Packaging a Python application as a Windows executable with PyInstaller

## Status

✅ Version 1.0