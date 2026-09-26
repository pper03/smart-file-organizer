from pathlib import Path

folder_path = input("Enter folder path: ").strip().strip('"')

if not folder_path:
    print("Please enter a folder path")
    exit()

folder = Path(folder_path)

if not folder.exists():
    print("Folder not found")
    exit()

if not folder.is_dir():
    print("Path is not a folder")
    exit()

print(f"Organizing: {folder}")


document_extensions = (".pdf", ".txt", ".docx", ".xlsx", ".pptx")
image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
video_extensions = (".mp4", ".mov", ".avi", ".mkv")
audio_extensions = (".mp3", ".wav", ".flac", ".m4a")
archive_extensions = (".zip", ".rar", ".7z")
program_extensions = (".exe", ".msi")

document_folder = folder / "Documents"
image_folder = folder / "Images"
video_folder = folder / "Videos"
audio_folder = folder / "Audio"
archives_folder = folder / "Archives"
program_folder = folder / "Programs"
other_folder = folder / "Other"

categories = [
    {
        "name": "Document",
        "folder": document_folder,
        "extensions": document_extensions
    },
    {
        "name": "Image",
        "folder": image_folder,
        "extensions": image_extensions
    },
    {
        "name": "Video",
        "folder": video_folder,
        "extensions": video_extensions
    },
    {
        "name": "Audio",
        "folder": audio_folder,
        "extensions": audio_extensions
    },
    {
        "name": "Archive",
        "folder": archives_folder,
        "extensions": archive_extensions
    },
    {
        "name": "Programs",
        "folder": program_folder,
        "extensions": program_extensions
    }
]

def get_target_folder(file_name):

    for category in categories:
        if file_name.endswith(category["extensions"]):
            return category["name"], category["folder"]

    return "Other", other_folder

def scan_files(folder):
    files_to_organize = []

    for file in folder.iterdir():

        if not file.is_file():
            continue

        file_name = file.name.lower()

        category_name, target_folder = get_target_folder(file_name)

        print(file.name, "->", category_name)
        files_to_organize.append((file, category_name, target_folder))

    return files_to_organize

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

files_to_organize = scan_files(folder)

if not files_to_organize:
    print("No files to organize.")
    exit()

print("\nPreview:")

for file, category_name, target_folder in files_to_organize:
    print(file.name, "->", category_name)

choice = input("Move these files? (y/n): ").strip().lower()

if choice == "y":
    for file, category_name, target_folder in files_to_organize:
        result = move_file(file, target_folder)

        if result:
            organized_count += 1
            file_counts[category_name] += 1
        else:
            failed_count += 1

    print("\n===== Summary =====")

    for category, count in file_counts.items():
        print(f"{category}: {count}")

    print(f"\nTotal organized: {organized_count}")
    print(f"Failed: {failed_count}")
    print("===================")
else:
    print("Organization cancelled.")
    