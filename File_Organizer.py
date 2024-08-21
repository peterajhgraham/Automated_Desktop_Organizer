import os
import pathlib
import shutil

# File format dictionary
file_categories = {
    "Web Content": [".html", ".htm", ".php", ".asp", ".js", ".css", ".xml", ".json", ".rss"], 
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".ico", ".heif", ".raw"], 
    "Movies": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".3gp", ".vob", ".ogv"], 
    "Text Files": [".txt", ".pdf", ".doc", ".docx", ".odt", ".rtf", ".html", ".epub", ".md", ".tex"], 
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".dmg", ".tar.gz"], 
    "Audio Tracks": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".m4b", ".opus", ".wma", ".aiff"], 
}

def organize_files():
    # Scan through files in the current directory
    for item in os.scandir():
        if item.is_file():  # Process only files
            file_path = pathlib.Path(item)
            file_extension = file_path.suffix.lower()
            
            src = str(file_path)
            dest_folder = "Miscellaneous"  # Default folder if no match
            
            if file_extension == "":
                print(f"{src} has no file extension!")
                continue

            # Determine the correct folder based on file extension
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    dest_folder = category
                    break
            else:
                # Create "Miscellaneous" folder if it doesn't exist
                if not os.path.isdir("Miscellaneous"):
                    os.mkdir("Miscellaneous")
                dest_folder = "Miscellaneous"
            
            # Create the destination folder if it doesn't exist
            if not os.path.isdir(dest_folder):
                os.mkdir(dest_folder)
            
            # Move the file to the appropriate folder
            shutil.move(src, os.path.join(dest_folder, file_path.name))
            print(f"{src} moved to {dest_folder}!")

    # Optionally remove the script file if it's in the "Miscellaneous" folder
    script_name = "File_Organizer.py"
    if os.path.isfile(os.path.join("Miscellaneous", script_name)):
        os.remove(os.path.join("Miscellaneous", script_name))
        print(f"{script_name} removed from 'Miscellaneous' folder.")
    
    input("\nPRESS ENTER TO EXIT")

if __name__ == "__main__":
    organize_files()
