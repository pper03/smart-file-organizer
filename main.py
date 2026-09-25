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

def move_file(file, target_folder):
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

organized_count = 0

files_to_organize = []

for file in folder.iterdir():
    
    if not file.is_file():
        continue
    file_name = file.name.lower()

    if file_name.endswith(document_extensions):
        print(file.name, "->", "Document")
        files_to_organize.append((file, document_folder))

    elif file_name.endswith(image_extensions):
        print(file.name, "->", "Image")
        files_to_organize.append((file, image_folder))

    elif file_name.endswith(video_extensions):
        print(file.name, "->", "Video")
        files_to_organize.append((file, video_folder))

    elif file_name.endswith(audio_extensions):
        print(file.name, "->", "Audio")
        files_to_organize.append((file, audio_folder))

    elif file_name.endswith(archive_extensions):
        print(file.name, "->", "Archive")
        files_to_organize.append((file, archives_folder))

    elif file_name.endswith(program_extensions):
        print(file.name, "->", "Program")
        files_to_organize.append((file, program_folder))

    else:
        print(file.name, "->", "Other")
        files_to_organize.append((file, other_folder))

if not files_to_organize:
    print("No files to organize.")
    exit()

print("\nPreview:")

for file, target_folder in files_to_organize:
    print(file.name, "->", target_folder.name)

choice = input("Move these files? (y/n): ").strip().lower()

if choice == "y":
    for file, target_folder in files_to_organize:
        result = move_file(file, target_folder)

        if result:
            organized_count += 1

    print("Organization complete!")
    print(f"{organized_count} files organized.")

else:
    print("Organization cancelled.")