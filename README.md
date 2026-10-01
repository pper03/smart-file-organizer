# Smart File Organizer

A Python desktop application that groups files by filename extension and moves selected files into category folders after user confirmation.

## Features

- Automatically detects and organizes files
- Supports multiple file extensions
- Classifies files into Documents, Images, Videos, Audio, Archives, Programs, and Other
- Provides a graphical user interface (GUI) using Tkinter
- Allows users to select folders using a folder picker
- Displays files in a clean category-based interface
- Allows users to select individual files before organizing
- Allows users to select or deselect an entire category
- Includes an ALL option to select or deselect every file
- Automatically updates category and ALL selection states
- Hides categories that contain no files
- Supports scrolling through large file lists
- Asks for confirmation before moving selected files
- Automatically creates category folders
- Prevents duplicate filenames by automatically renaming files
- Reports file-system errors when a file cannot be moved
- Shows failed filenames and error details in the summary (up to five failures)
- Displays an error dialog if the selected folder cannot be read
- Handles empty folders safely
- Shows an organization summary by category
- Reports successfully organized and failed files
- Supports uppercase and lowercase file extensions

## Screenshots

### File Selection

![Smart File Organizer](screenshots/gui-preview.png)

### Organization Summary

![Organization Summary](screenshots/summary.png)

## How It Works

1. Select a folder to organize.
2. The program scans the files inside the selected folder.
3. Each file is classified based on its file extension.
4. Only categories containing files are displayed.
5. Select individual files, categories, or use ALL to select everything.
6. Click **Organize Selected Files**.
7. Confirm the operation.
8. Selected files are moved into their corresponding category folders.
9. A summary displays successful moves by category, the total moved, and the number of failures.
10. If any moves fail, the summary also shows filenames and error details for up to five failures. The file list is then refreshed.

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

If you have a packaged Windows build, run `Smart File Organizer.exe`.
No Python installation is required for the packaged build.

The Windows executable was rebuilt on 2026-10-01. Manual tests confirmed successful movement of one selected file and a failure summary showing the filename and error details when the source folder was renamed.

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
- Working with dynamic GUI elements
- Managing checkbox states with `BooleanVar`
- Creating scrollable interfaces
- Handling duplicate filenames safely
- Git and GitHub version control
- Packaging a Python application as a Windows executable with PyInstaller

## Version 1.1

Version 1.1 introduces a new file selection interface.

Users can now:

- Select individual files
- Select all files inside a category
- Select all detected files at once
- See only categories that contain files
- Scroll through large file lists
- Organize only the selected files

## Error-Handling Update — 2026-10-01

- Catch `OSError` while scanning a folder and show a readable error dialog.
- Return both the success status and error message from `move_file()`.
- Include failed filenames and error details in the GUI summary.
- Keep the existing file-selection interface and duplicate-name handling.

## Validation

Checks performed on the updated Python source on 2026-10-01:

| Check | Result | Method |
|---|---|---|
| Empty folder | Displays “No files to organize.” without ALL | Manual Windows GUI test |
| Folder containing files | Displays file categories and a total of seven files | Manual Windows GUI test |
| Folder renamed after selection | Displays “Cannot open folder” | Manual Windows GUI test |
| Select folder again after error | File list appears again | Manual Windows GUI test |
| Failed move | Summary shows zero moved, one failed, filename and error details | Manual Windows GUI test |
| Duplicate filename | Original remains intact; moved file receives `_1` suffix | Temporary-file function test |
| Mixed successful and failed moves | Correct counts and failure details | Temporary-file test with GUI dialogs replaced by test doubles |

The temporary-file tests do not replace testing the packaged Windows application.

## Limitations

- Scans only files directly inside the selected folder; does not scan subfolders recursively.
- Uses filename extensions, not file contents, to classify files.
- Moves files rather than copying them; there is no undo feature.
- Renames a file when its destination name already exists. Avoid other programs changing the same files during organization.
- Shows details for at most five failed files; additional failures are counted but their details are not displayed.
- Large folders may temporarily make the interface unresponsive because processing runs on the GUI thread.

Use a folder containing disposable test files when trying the application for the first time.

## Development and AI Assistance

This is a learning project developed with assistance from ChatGPT for code examples, debugging, explanations, and documentation. I applied the changes and performed the manual Windows GUI tests described above. The temporary-file function checks were run by the AI assistant in its execution environment.

## Status

Version 1.1 with error-handling improvements. The Windows executable was rebuilt and passed the successful-move and failed-move tests on 2026-10-01.