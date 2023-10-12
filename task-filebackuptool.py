import shutil
import os
import datetime

def backup_files(source_paths, backup_location):
    timestamp = datetime.datetime.now().isoformat().replace(":", "_").replace(".", "_")
    backup_folder = os.path.join(backup_location, timestamp)

    try:
        os.makedirs(backup_folder)
    except FileExistsError:
        print("Backup folder already exists. Please choose a different location.")
        return

    for source_path in source_paths:
        source_path = os.path.abspath(source_path)
        base_name = os.path.basename(source_path)
        destination_path = os.path.join(backup_folder, base_name)

        try:
            if os.path.isfile(source_path):
                shutil.copy2(source_path, destination_path)
            elif os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path)
            print(f"Backup completed for: {source_path}")
        except Exception as e:
            print(f"Error while backing up {source_path}: {str(e)}")

    print(f"Backup completed to: {backup_folder}")

if __name__ == "__main__":
    source_paths = input("Enter files/directories to backup (separated by spaces): ").split()
    backup_location = input("Enter the backup location: ")

    backup_files(source_paths, backup_location)
