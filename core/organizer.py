import os
import shutil

from core.logger import log_info, log_error


def organize_files(folder_path):

    organized_count = 0
    move_history = []

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        # Images
        if extension in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
            category = "Images"

        # Documents
        elif extension in [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"]:
            category = "Documents"

        # Videos
        elif extension in [".mp4", ".mkv", ".avi", ".mov"]:
            category = "Videos"

        # Music
        elif extension in [".mp3", ".wav", ".flac"]:
            category = "Music"

        # Programming
        elif extension in [".py", ".java", ".cpp", ".html", ".css", ".js"]:
            category = "Programming"

        # Archives
        elif extension in [".zip", ".rar", ".7z"]:
            category = "Archives"

        # Other files
        else:
            category = "Others"

        category_folder = os.path.join(
            folder_path,
            category
        )

        os.makedirs(
            category_folder,
            exist_ok=True
        )

        destination = os.path.join(
            category_folder,
            file
        )

        try:

            shutil.move(
                file_path,
                destination
            )

            organized_count += 1

            move_history.append(
                (file_path, destination)
            )

            print(
                f"Moved: {file} → {category}"
            )

            log_info(
                f"{file} moved from "
                f"{file_path} to {destination}"
            )

        except Exception as error:

            print(
                f"Could not move {file}: {error}"
            )

            log_error(
                f"Could not move {file}: {error}"
            )

    return organized_count, move_history


def undo_organization(move_history):

    if not move_history:

        print("\n❌ Nothing to undo.")

        return 0

    restored_count = 0

    print("\n↩️ Restoring files...\n")

    for original_path, new_path in reversed(move_history):

        try:

            if not os.path.exists(new_path):

                print(
                    f"File not found: {new_path}"
                )

                continue

            original_folder = os.path.dirname(
                original_path
            )

            os.makedirs(
                original_folder,
                exist_ok=True
            )

            shutil.move(
                new_path,
                original_path
            )

            restored_count += 1

            print(
                f"Restored: "
                f"{os.path.basename(original_path)}"
            )

            log_info(
                f"Restored {new_path} "
                f"to {original_path}"
            )

        except Exception as error:

            print(
                f"Could not restore "
                f"{new_path}: {error}"
            )

            log_error(
                f"Could not restore "
                f"{new_path}: {error}"
            )

    return restored_count