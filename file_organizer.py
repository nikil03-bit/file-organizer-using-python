import os
from pathlib import Path

# Dictionary of file types and their extensions
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".svg"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm"],
    "DOCUMENTS": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "AUDIO": [".mp3", ".wav", ".aac", ".flac", ".wma"],
    "ARCHIVES": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "PYTHON": [".py"],
}

FILE_FORMATS = {ext: folder for folder, exts in DIRECTORIES.items() for ext in exts}

def organize_files(folder_path):
    # Convert to Path object
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("The folder path is not valid. Please check and try again.")
        return

    # Go through each file in the folder
    for file_path in folder.iterdir():
        if file_path.is_file(): 
            ext = file_path.suffix.lower()
            if ext in FILE_FORMATS:
                # Get the folder name for this file extension
                target_folder_name = FILE_FORMATS[ext]
                target_folder_path = folder / target_folder_name

                # Create the folder if it doesn't already exist
                target_folder_path.mkdir(exist_ok=True)

                # Move the file
                new_file_path = target_folder_path / file_path.name
                file_path.rename(new_file_path)
                print(f"Moved: {file_path.name} → {target_folder_name}/")


if __name__ == "__main__":
    folder_to_organize = input("Enter the path of the folder to organize: ")
    organize_files(folder_to_organize)
    print("Files have been organized.")
