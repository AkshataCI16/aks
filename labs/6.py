import os
import re

folder = input("Enter folder path: ")

if not os.path.exists(folder):
    print("Folder does not exist")

else:
    for filename in os.listdir(folder):

        match = re.search(
            r'(\d{2})-(\d{2})-(\d{4})',
            filename
        )

        if match:
            month, day, year = match.groups()

            new_date = f"{day}-{month}-{year}"

            new_filename = filename.replace(
                match.group(0), new_date
            )

            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_filename)

            os.rename(old_path, new_path)

            print(filename, "->", new_filename)

    print("Renaming completed")