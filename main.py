from pathlib import Path

folder = Path("test_files")
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

for file in folder.iterdir():
    
    if not file.is_file():
        continue
    file_name = file.name.lower()

    if file_name.endswith(document_extensions):
        print(file.name, "->", "Document")
        move_file(file, document_folder)

    elif file_name.endswith(image_extensions):
        print(file.name, "->", "Image")
        move_file(file, image_folder)

    elif file_name.endswith(video_extensions):
        print(file.name, "->", "Video")
        move_file(file, video_folder)

    elif file_name.endswith(audio_extensions):
        print(file.name, "->", "Audio")
        move_file(file, audio_folder)


    elif file_name.endswith(archive_extensions):
            print(file.name, "->", "Archive")
            move_file(file, archives_folder)

    elif file_name.endswith(program_extensions):
        print(file.name, "->", "Program")
        move_file(file, program_folder)
    else:
        print(file.name, "->", "Other")
        move_file(file, other_folder)