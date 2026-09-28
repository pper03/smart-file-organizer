import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

document_extensions = (".pdf", ".txt", ".docx", ".xlsx", ".pptx")
image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
video_extensions = (".mp4", ".mov", ".avi", ".mkv")
audio_extensions = (".mp3", ".wav", ".flac", ".m4a")
archive_extensions = (".zip", ".rar", ".7z")
program_extensions = (".exe", ".msi")

categories = [
    {"name": "Document", "folder": "Documents", "extensions": document_extensions},
    {"name": "Image", "folder": "Images", "extensions": image_extensions},
    {"name": "Video", "folder": "Videos" ,"extensions": video_extensions},
    {"name": "Audio", "folder": "Audio", "extensions": audio_extensions},
    {"name": "Archive", "folder": "Archives", "extensions": archive_extensions},
    {"name": "Programs", "folder": "Programs", "extensions": program_extensions},
]

def select_folder():
    folder_path = filedialog.askdirectory()

    if folder_path:
        selected_folder.set(folder_path)
        folder_label.config(text=folder_path)

def move_file(file, target_folder):
    try:
        target_folder.mkdir(exist_ok=True)

        destination = target_folder / file.name
        stem = file.stem
        suffix = file.suffix
        counter = 1

        while destination.exists():
            destination = target_folder / f"{stem}_{counter}{suffix}"
            counter += 1

        file.rename(destination)
        return True

    except Exception as error:
        print("Failed to move:", file.name)
        print("Error:", error)
        return False

def organize_files():
    folder_path = selected_folder.get()

    if not folder_path:
        messagebox.showwarning(
            "Smart File Organizer",
            "Please select a folder first."
        )
        return

    preview_text.delete("1.0", tk.END)
    
    folder = Path(folder_path)

    files_to_organize = []

    for file in folder.iterdir():

        if not file.is_file():
            continue

        file_name = file.name.lower()

        for category in categories:
            if file_name.endswith(category["extensions"]):
                category_name = category["name"]
                target_folder = folder / category["folder"]
                files_to_organize.append((file, category_name, target_folder))

                preview_text.insert(
                    tk.END,
                    f"{file_name} -> {category_name}\n"
                )
                break
        else:
            category_name = "Other"
            target_folder = folder / "Other"
            files_to_organize.append((file, category_name, target_folder))

            preview_text.insert(
                tk.END,
                f"{file_name} -> Other\n"
            )

    if not files_to_organize:
        messagebox.showinfo(
            "Smart File Organizer",
            "No files to organize."
        )
        return

    confirmed = messagebox.askyesno(
        "Confirm",
        "Move these files?"
        )
    
    if not confirmed:
        return

    organized_count = 0
    failed_count = 0

    file_counts = {
        "Document": 0,
        "Image": 0,
        "Video": 0,
        "Audio": 0,
        "Archive": 0,
        "Programs": 0,
        "Other": 0
    }

    for file, category_name, target_folder in files_to_organize:
        result = move_file(file, target_folder)

        if result:
            organized_count += 1
            file_counts[category_name] += 1
        else:
            failed_count += 1
    summary = "===== Summary =====\n"

    for category, count in file_counts.items():
        summary += f"{category}: {count}\n"

    summary += f"\nTotal organized: {organized_count}"
    summary += f"\nFailed: {failed_count}"

    messagebox.showinfo("Summary", summary)
    
root = tk.Tk()
selected_folder = tk.StringVar()

root.title("Smart File Organizer")
root.geometry("600x500")
title_label = tk.Label(
    root,
    text="Smart File Organizer",
    font=("Arial", 20, "bold")
)
 
title_label.pack(pady=20)

folder_label = tk.Label(
    root,
    text="No folder selected"
)

folder_label.pack(pady=10)

preview_text = tk.Text(
    root,
    height=12,
    width=60
)

preview_text.pack(pady=10)

select_button = tk.Button(
    root,
    text="Select Folder",
    command=select_folder
)

select_button.pack(pady=10)

organize_button = tk.Button(
    root,
    text="Organize Files",
    command=organize_files
)

organize_button.pack(pady=10)

root.mainloop()
