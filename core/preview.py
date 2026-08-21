import os


def preview_organization(folder_path):

    previews = []

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        if extension in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
            category = "Images"

        elif extension in [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"]:
            category = "Documents"

        elif extension in [".mp4", ".mkv", ".avi", ".mov"]:
            category = "Videos"

        elif extension in [".mp3", ".wav", ".flac"]:
            category = "Music"

        elif extension in [".py", ".java", ".cpp", ".html", ".css", ".js"]:
            category = "Programming"

        elif extension in [".zip", ".rar", ".7z"]:
            category = "Archives"

        else:
            category = "Others"

        previews.append((file, category))

    return previews