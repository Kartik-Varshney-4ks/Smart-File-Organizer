import os
import hashlib


def get_file_hash(file_path):

    hash_object = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            hash_object.update(data)

    return hash_object.hexdigest()


def find_duplicates(folder_path):

    file_sizes = {}
    duplicates = []

    for root, folders, files in os.walk(folder_path):

        for file in files:

            file_path = os.path.join(root, file)

            try:

                file_size = os.path.getsize(file_path)

                # Ignore empty files
                if file_size == 0:
                    continue

                # Files with unique sizes cannot be duplicates
                if file_size not in file_sizes:

                    file_sizes[file_size] = []

                file_sizes[file_size].append(file_path)

            except OSError as error:

                print(
                    f"Could not read {file}: {error}"
                )


    # Compare hashes only for files
    # that have the same size

    for size, files in file_sizes.items():

        if len(files) < 2:
            continue

        hashes = {}

        for file_path in files:

            try:

                file_hash = get_file_hash(file_path)

                if file_hash in hashes:

                    original_file = hashes[file_hash]

                    duplicates.append(
                        (original_file, file_path)
                    )

                else:

                    hashes[file_hash] = file_path

            except OSError as error:

                print(
                    f"Could not calculate hash "
                    f"for {file_path}: {error}"
                )

    return duplicates


def delete_duplicate(file_path):

    try:

        if not os.path.exists(file_path):

            print(
                "\n❌ File does not exist."
            )

            return False

        os.remove(file_path)

        print(
            f"\n🗑️ Deleted duplicate: "
            f"{file_path}"
        )

        return True

    except PermissionError:

        print(
            "\n❌ Permission denied. "
            "Cannot delete this file."
        )

        return False

    except OSError as error:

        print(
            f"\n❌ Could not delete file: "
            f"{error}"
        )

        return False