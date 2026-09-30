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
    {"name": "Video", "folder": "Videos", "extensions": video_extensions},
    {"name": "Audio", "folder": "Audio", "extensions": audio_extensions},
    {"name": "Archive", "folder": "Archives", "extensions": archive_extensions},
    {"name": "Programs", "folder": "Programs", "extensions": program_extensions},
]


def get_category(file):
    file_name = file.name.lower()

    for category in categories:
        if file_name.endswith(category["extensions"]):
            return category["name"]

    return "Other"


def get_target_folder(folder, category_name):
    for category in categories:
        if category["name"] == category_name:
            return folder / category["folder"]

    return folder / "Other"


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


def toggle_all():
    state = all_var.get()

    for category_var in category_vars.values():
        category_var.set(state)

    for file_var in file_vars.values():
        file_var.set(state)


def toggle_category(category_name):
    state = category_vars[category_name].get()

    for file, file_var in file_vars.items():
        if file_categories[file] == category_name:
            file_var.set(state)

    update_all_state()


def toggle_file(file):
    category_name = file_categories[file]

    category_files = [
        file_var
        for current_file, file_var in file_vars.items()
        if file_categories[current_file] == category_name
    ]

    category_vars[category_name].set(
        all(file_var.get() for file_var in category_files)
    )

    update_all_state()


def update_all_state():
    if not file_vars:
        all_var.set(False)
        return

    all_var.set(
        all(file_var.get() for file_var in file_vars.values())
    )


def clear_table():
    for widget in table_content.winfo_children():
        widget.destroy()

    category_vars.clear()
    file_vars.clear()
    file_categories.clear()

    all_var.set(False)


def build_table(folder):
    clear_table()

    grouped_files = {}

    for file in folder.iterdir():
        if not file.is_file():
            continue

        category_name = get_category(file)

        if category_name not in grouped_files:
            grouped_files[category_name] = []

        grouped_files[category_name].append(file)

    if not grouped_files:
        empty_label = tk.Label(
            table_content,
            text="No files to organize.",
            font=("Segoe UI", 11),
            bg="white",
            fg="#666666"
        )
        empty_label.pack(pady=40)
        return

    total_files = sum(len(files) for files in grouped_files.values())

    all_row = tk.Frame(
        table_content,
        bg="#EAEAEA",
        highlightbackground="#CCCCCC",
        highlightthickness=1
    )
    all_row.pack(fill="x")

    all_checkbox = tk.Checkbutton(
        all_row,
        text="ALL",
        variable=all_var,
        command=toggle_all,
        font=("Segoe UI", 10, "bold"),
        bg="#EAEAEA",
        activebackground="#EAEAEA"
    )
    all_checkbox.pack(side="left", padx=12, pady=10)

    all_count = tk.Label(
        all_row,
        text=f"{total_files} files",
        font=("Segoe UI", 9),
        bg="#EAEAEA",
        fg="#666666"
    )
    all_count.pack(side="right", padx=15)

    category_order = [
        "Document",
        "Image",
        "Video",
        "Audio",
        "Archive",
        "Programs",
        "Other"
    ]

    for category_name in category_order:
        if category_name not in grouped_files:
            continue

        files = grouped_files[category_name]

        category_var = tk.BooleanVar()
        category_vars[category_name] = category_var

        category_box = tk.Frame(
            table_content,
            bg="white",
            highlightbackground="#DDDDDD",
            highlightthickness=1
        )
        category_box.pack(fill="x", pady=(8, 0))

        category_header = tk.Frame(
            category_box,
            bg="#F5F5F5"
        )
        category_header.pack(fill="x")

        category_checkbox = tk.Checkbutton(
            category_header,
            text=category_name,
            variable=category_var,
            command=lambda name=category_name: toggle_category(name),
            font=("Segoe UI", 10, "bold"),
            bg="#F5F5F5",
            activebackground="#F5F5F5"
        )
        category_checkbox.pack(
            side="left",
            padx=12,
            pady=8
        )

        file_word = "file" if len(files) == 1 else "files"

        category_count = tk.Label(
            category_header,
            text=f"{len(files)} {file_word}",
            font=("Segoe UI", 9),
            bg="#F5F5F5",
            fg="#777777"
        )
        category_count.pack(
            side="right",
            padx=15
        )

        for file in files:
            file_var = tk.BooleanVar()

            file_vars[file] = file_var
            file_categories[file] = category_name

            file_row = tk.Frame(
                category_box,
                bg="white"
            )
            file_row.pack(fill="x")

            file_checkbox = tk.Checkbutton(
                file_row,
                text=file.name,
                variable=file_var,
                command=lambda f=file: toggle_file(f),
                font=("Segoe UI", 10),
                bg="white",
                activebackground="white",
                anchor="w"
            )
            file_checkbox.pack(
                fill="x",
                padx=(35, 12),
                pady=5
            )


def select_folder():
    folder_path = filedialog.askdirectory()

    if not folder_path:
        return

    selected_folder.set(folder_path)
    folder_label.config(text=folder_path)

    build_table(Path(folder_path))


def organize_files():
    folder_path = selected_folder.get()

    if not folder_path:
        messagebox.showwarning(
            "Smart File Organizer",
            "Please select a folder first."
        )
        return

    selected_files = [
        file
        for file, file_var in file_vars.items()
        if file_var.get()
    ]

    if not selected_files:
        messagebox.showinfo(
            "Smart File Organizer",
            "No files selected."
        )
        return

    confirmed = messagebox.askyesno(
        "Confirm",
        f"Move {len(selected_files)} selected file(s)?"
    )

    if not confirmed:
        return

    folder = Path(folder_path)

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

    for file in selected_files:
        category_name = file_categories[file]
        target_folder = get_target_folder(folder, category_name)

        if move_file(file, target_folder):
            organized_count += 1
            file_counts[category_name] += 1
        else:
            failed_count += 1

    summary = "===== Summary =====\n"

    for category, count in file_counts.items():
        if count > 0:
            summary += f"{category}: {count}\n"

    summary += f"\nTotal organized: {organized_count}"
    summary += f"\nFailed: {failed_count}"

    messagebox.showinfo(
        "Summary",
        summary
    )

    build_table(folder)


root = tk.Tk()
root.title("Smart File Organizer")
root.geometry("700x650")
root.minsize(600, 500)

selected_folder = tk.StringVar()
all_var = tk.BooleanVar()

category_vars = {}
file_vars = {}
file_categories = {}


title_label = tk.Label(
    root,
    text="Smart File Organizer",
    font=("Segoe UI", 22, "bold")
)
title_label.pack(pady=(20, 5))


subtitle_label = tk.Label(
    root,
    text="Select a folder and choose the files you want to organize.",
    font=("Segoe UI", 10),
    fg="#666666"
)
subtitle_label.pack()


folder_frame = tk.Frame(root)
folder_frame.pack(
    fill="x",
    padx=30,
    pady=15
)


select_button = tk.Button(
    folder_frame,
    text="Select Folder",
    command=select_folder,
    font=("Segoe UI", 10),
    padx=12,
    pady=5
)
select_button.pack(side="left")


folder_label = tk.Label(
    folder_frame,
    text="No folder selected",
    font=("Segoe UI", 9),
    fg="#666666",
    anchor="w"
)
folder_label.pack(
    side="left",
    padx=12,
    fill="x",
    expand=True
)


table_outer = tk.Frame(
    root,
    highlightbackground="#CCCCCC",
    highlightthickness=1
)
table_outer.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=(0, 15)
)


canvas = tk.Canvas(
    table_outer,
    bg="white",
    highlightthickness=0
)


scrollbar = tk.Scrollbar(
    table_outer,
    orient="vertical",
    command=canvas.yview
)


table_content = tk.Frame(
    canvas,
    bg="white"
)


table_window = canvas.create_window(
    (0, 0),
    window=table_content,
    anchor="nw"
)


def update_scroll_region(event):
    canvas.configure(
        scrollregion=canvas.bbox("all")
    )


def resize_table(event):
    canvas.itemconfig(
        table_window,
        width=event.width
    )


table_content.bind(
    "<Configure>",
    update_scroll_region
)

canvas.bind(
    "<Configure>",
    resize_table
)


canvas.configure(
    yscrollcommand=scrollbar.set
)


canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)

def on_mousewheel(event):
    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


canvas.bind_all("<MouseWheel>", on_mousewheel)


organize_button = tk.Button(
    root,
    text="Organize Selected Files",
    command=organize_files,
    font=("Segoe UI", 11, "bold"),
    padx=18,
    pady=8
)
organize_button.pack(pady=(0, 20))


root.mainloop()