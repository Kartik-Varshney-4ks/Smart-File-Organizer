import os

from core.organizer import organize_files, undo_organization
from core.duplicate import find_duplicates, delete_duplicate
from core.statistics import get_statistics
from core.search import search_files
from core.preview import preview_organization


def show_menu():

    print("\n" + "=" * 50)
    print("          SMART FILE ORGANIZER")
    print("=" * 50)

    print("\n1. Organize Files")
    print("2. Preview Organization")
    print("3. Find Duplicate Files")
    print("4. Show Statistics")
    print("5. Search Files")
    print("6. View Activity Log")
    print("7. Manage Duplicates")
    print("8. Undo Last Organization")
    print("9. Exit")


# Get folder path
folder_path = input("\nEnter the folder path: ").strip()


# Check folder
if not os.path.isdir(folder_path):

    print("\n❌ Folder not found!")
    print("Please enter a valid folder path.")

    exit()


# Stores the most recent organization history
last_move_history = []


# Main menu
while True:

    show_menu()

    choice = input("\nEnter your choice: ").strip()


    # ========================================
    # OPTION 1 - ORGANIZE
    # ========================================

    if choice == "1":

        print("\n📂 Organizing files...\n")

        try:

            organized_count, move_history = organize_files(
                folder_path
            )

            last_move_history = move_history

            print("\n✅ Organization completed!")
            print(f"Files organized: {organized_count}")

        except PermissionError:

            print("\n❌ Permission denied!")

        except Exception as error:

            print("\n❌ Organization error:")
            print(error)


    # ========================================
    # OPTION 2 - PREVIEW
    # ========================================

    elif choice == "2":

        print("\n📋 Organization Preview\n")

        try:

            previews = preview_organization(folder_path)

            if previews:

                for file, category in previews:

                    destination = os.path.join(
                        folder_path,
                        category,
                        file
                    )

                    print(f"File: {file}")
                    print(f"Category: {category}")
                    print(f"Destination: {destination}")
                    print()

                confirmation = input(
                    "Proceed with organization? (y/n): "
                ).strip().lower()

                if confirmation == "y":

                    (
                        organized_count,
                        move_history
                    ) = organize_files(folder_path)

                    last_move_history = move_history

                    print(
                        f"\n✅ {organized_count} "
                        "file(s) organized."
                    )

                elif confirmation == "n":

                    print("\n❌ Organization cancelled.")

                else:

                    print(
                        "\n❌ Invalid choice. "
                        "Organization cancelled."
                    )

            else:

                print("No files need organization.")

        except Exception as error:

            print("\n❌ Preview error:")
            print(error)


    # ========================================
    # OPTION 3 - FIND DUPLICATES
    # ========================================

    elif choice == "3":

        print("\n🔁 Checking for duplicate files...\n")

        try:

            duplicates = find_duplicates(folder_path)

            if duplicates:

                print("Duplicate Files:")

                for original, duplicate in duplicates:

                    print("\nOriginal:")
                    print(original)

                    print("Duplicate:")
                    print(duplicate)

            else:

                print("✅ No duplicate files found.")

        except Exception as error:

            print("\n❌ Duplicate detection error:")
            print(error)


    # ========================================
    # OPTION 4 - STATISTICS
    # ========================================

    elif choice == "4":

        print("\n📊 Organization Statistics\n")

        try:

            total_files, statistics = get_statistics(
                folder_path
            )

            print(f"Total files: {total_files}")

            for category, count in statistics.items():

                print(f"{category}: {count}")

        except Exception as error:

            print("\n❌ Statistics error:")
            print(error)


    # ========================================
    # OPTION 5 - SEARCH
    # ========================================

    elif choice == "5":

        search_name = input(
            "\n🔎 Enter file name to search: "
        ).strip()

        try:

            search_results = search_files(
                folder_path,
                search_name
            )

            print("\n🔎 Search Results")

            if search_results:

                for file in search_results:

                    print(file)

            else:

                print("No matching files found.")

        except Exception as error:

            print("\n❌ Search error:")
            print(error)


    # ========================================
    # OPTION 6 - ACTIVITY LOG
    # ========================================

    elif choice == "6":

        print("\n📝 Activity Log\n")

        log_file = "organizer.log"

        try:

            if os.path.exists(log_file):

                with open(
                    log_file,
                    "r",
                    encoding="utf-8"
                ) as file:

                    logs = file.readlines()

                if logs:

                    print("Recent Activity:\n")

                    for log in logs[-10:]:

                        print(log.strip())

                else:

                    print("No activity recorded yet.")

            else:

                print("No activity log found.")

        except Exception as error:

            print("\n❌ Could not read activity log:")
            print(error)


    # ========================================
    # OPTION 7 - MANAGE DUPLICATES
    # ========================================

    elif choice == "7":

        print("\n🗑️ Duplicate Management\n")

        try:

            duplicates = find_duplicates(folder_path)

            if not duplicates:

                print("✅ No duplicate files found.")

            else:

                for number, (original, duplicate) in enumerate(
                    duplicates,
                    start=1
                ):

                    print(f"\nDuplicate {number}")
                    print(f"Original : {original}")
                    print(f"Duplicate: {duplicate}")

                    confirmation = input(
                        "\nDelete this duplicate? (y/n): "
                    ).strip().lower()

                    if confirmation == "y":

                        delete_duplicate(duplicate)

                    else:

                        print("Skipped.")

        except Exception as error:

            print(
                "\n❌ Duplicate management error:"
            )

            print(error)


    # ========================================
    # OPTION 8 - UNDO LAST ORGANIZATION
    # ========================================

    elif choice == "8":

        print("\n↩️ Undo Last Organization\n")

        if not last_move_history:

            print("❌ Nothing to undo.")

        else:

            confirmation = input(
                "Undo the last organization? (y/n): "
            ).strip().lower()

            if confirmation == "y":

                try:

                    restored_count = undo_organization(
                        last_move_history
                    )

                    print(
                        f"\n✅ {restored_count} "
                        "file(s) restored."
                    )

                    last_move_history = []

                except Exception as error:

                    print(
                        "\n❌ Undo error:"
                    )

                    print(error)

            else:

                print("\n❌ Undo cancelled.")


    # ========================================
    # OPTION 9 - EXIT
    # ========================================

    elif choice == "9":

        print(
            "\n👋 Thank you for using "
            "Smart File Organizer!"
        )

        break


    # ========================================
    # INVALID CHOICE
    # ========================================

    else:

        print("\n❌ Invalid choice. Please enter 1-9.")