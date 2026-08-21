import os


def get_statistics(folder_path):

    statistics = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Music": 0,
        "Programming": 0,
        "Archives": 0,
        "Others": 0
    }

    total_files = 0

    for root, folders, files in os.walk(folder_path):

        for file in files:

            total_files += 1

            extension = os.path.splitext(file)[1].lower()

            if extension in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
                statistics["Images"] += 1

            elif extension in [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"]:
                statistics["Documents"] += 1

            elif extension in [".mp4", ".mkv", ".avi", ".mov"]:
                statistics["Videos"] += 1

            elif extension in [".mp3", ".wav", ".flac"]:
                statistics["Music"] += 1

            elif extension in [".py", ".java", ".cpp", ".html", ".css", ".js"]:
                statistics["Programming"] += 1

            elif extension in [".zip", ".rar", ".7z"]:
                statistics["Archives"] += 1

            else:
                statistics["Others"] += 1

    return total_files, statistics