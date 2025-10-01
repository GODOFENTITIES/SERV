import os
import shutil

# Customize the folder categories and extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def sort_directory(path):
    if not os.path.isdir(path):
        print(f"❌ The path '{path}' is not a valid directory.")
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            category = get_category(ext)
            category_path = os.path.join(path, category)

            # Create category folder if it doesn't exist
            os.makedirs(category_path, exist_ok=True)

            # Move file to category folder
            new_location = os.path.join(category_path, filename)
            shutil.move(file_path, new_location)
            print(f"✅ Moved '{filename}' to '{category}/'")

if __name__ == "__main__":
    target_directory = input("Enter the path of the directory to sort: ").strip()
    sort_directory(target_directory)
