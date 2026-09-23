from pathlib import Path

folder = Path("test_files")
document_extensions = (".pdf", ".txt", ".docx", ".xlsx", ".pptx")
image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".webp")
video_extensions = (".mp4", ".mov", ".avi", ".mkv")
audio_extensions = (".mp3", ".wav", ".flac", ".m4a")
archive_extensions = (".zip", ".rar", ".7z")
program_extensions = (".exe", ".msi")

for file in folder.iterdir():
    file_name = file.name.lower()

    if file_name.endswith(document_extensions):

        print(file.name, "->", "Document")

    elif file_name.endswith(image_extensions):

        print(file.name, "->", "Image")

    elif file_name.endswith(video_extensions):

        print(file.name, "->", "Video")

    elif file_name.endswith(audio_extensions):

        print(file.name, "->", "Audio")

    elif file_name.endswith(archive_extensions):
    
            print(file.name, "->", "Archive")

    elif file_name.endswith(program_extensions):

        print(file.name, "->", "Pogram")

    else:

        print(file.name, "->", "Other")