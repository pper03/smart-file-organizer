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
document_folder.mkdir(exist_ok=True)
image_folder = folder / "Images"
image_folder.mkdir(exist_ok=True)
video_folder = folder / "Videos"
video_folder.mkdir(exist_ok=True)
audio_folder = folder / "Audio"
audio_folder.mkdir(exist_ok=True)
archives_folder = folder / "Archives"
archives_folder.mkdir(exist_ok=True)
program_folder = folder / "Programs"
program_folder.mkdir(exist_ok=True)
other_folder = folder / "Other"
other_folder.mkdir(exist_ok=True)

def move_file(file, target_folder):
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

for file in folder.iterdir():
    
    if not file.is_file():
        continue
    file_name = file.name.lower()

    if file_name.endswith(document_extensions):
        print(file.name, "->", "Document")
        result = move_file(file, document_folder)
        if result:
            organized_count += 1

    elif file_name.endswith(image_extensions):
        print(file.name, "->", "Image")
        result = move_file(file, image_folder)
        if result:
            organized_count += 1

    elif file_name.endswith(video_extensions):
        print(file.name, "->", "Video")
        result = move_file(file, video_folder)
        if result:
            organized_count += 1

    elif file_name.endswith(audio_extensions):
        print(file.name, "->", "Audio")
        result = move_file(file, audio_folder)
        if result:
            organized_count += 1


    elif file_name.endswith(archive_extensions):
        print(file.name, "->", "Archive")
        result = move_file(file, archives_folder)
        if result:
            organized_count += 1

    elif file_name.endswith(program_extensions):
        print(file.name, "->", "Program")
        result = move_file(file, program_folder)
        if result:
            organized_count += 1

    else:
        print(file.name, "->", "Other")
        result = move_file(file, other_folder)
        if result:
            organized_count += 1

print("Organization complete!")
print(f"{organized_count} files organized.")