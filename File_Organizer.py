import os
import pathlib
import shutil

fileFormat = {
    "Web": [".html5", ".html", ".htm", ".xhtml"], 
    "Picture": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"], 
    "Video": [".avi", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"], 
    "Document": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"], 
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"], 
    "Audio": [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"], 
}

def organize_files():
    # List all files in the current directory
    for file in os.scandir():
        if file.is_file():  # Process only files
            fileName = pathlib.Path(file)
            fileFormatType = fileName.suffix.lower()
            
            src = str(fileName)
            dest = "Other"
            
            if fileFormatType == "":
                print(src, 'has no file extension!')
                continue

            # Determine the correct folder based on file extension
            for folder, formats in fileFormat.items():
                if fileFormatType in formats:
                    dest = folder
                    break
            else:
                # Create "Other" folder if not exists
                if not os.path.isdir("Other"):
                    os.mkdir("Other")
                dest = "Other"
            
            # Create destination folder if it doesn't exist
            if not os.path.isdir(dest):
                os.mkdir(dest)
            
            # Move the file to the destination folder
            shutil.move(src, os.path.join(dest, fileName.name))
            print(src, "moved to", dest, "!")
    
    # Remove the script file if it is in the "Other" folder
    script_path = "Other/FileOrganizer.py"
    if os.path.isfile(script_path):
        os.remove(script_path)
        print("FileOrganizer.py removed from 'Other' folder.")
    
    input("\nPRESS ENTER TO EXIT")

if __name__ == "__main__":
    organize_files()
