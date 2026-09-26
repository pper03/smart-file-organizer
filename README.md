# Smart File Organizer

A Python project that automatically identifies and organizes files by their file types.

## Current Features

- Detects files inside a folder
- Supports multiple file extensions
- Classifies files into:
  - Documents
  - Images
  - Videos
  - Audio
  - Archives
  - Programs
  - Other
- Handles uppercase and lowercase file extensions
- Automatically creates category folders
- Automatically moves files into the correct folders
- Prevents duplicate filenames by automatically renaming files
- Allows users to choose a folder to organize
- Validates folder paths before organizing
- Shows the number of files organized
- Shows a preview before moving files
- Asks for confirmation before organizing files
- Cancels safely without moving files
- Handles empty folders without unnecessary actions
- Uses a structured category system for file classification
- Refactored file scanning and classification into reusable functions

## Status

🚧 Work in Progress — Prototype v0.6

## Built With

- Python
- pathlib