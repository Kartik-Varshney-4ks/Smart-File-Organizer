import os


def search_files(folder_path, search_name):

    results = []

    for root, folders, files in os.walk(folder_path):

        for file in files:

            if search_name.lower() in file.lower():

                file_path = os.path.join(root, file)

                results.append(file_path)

    return results