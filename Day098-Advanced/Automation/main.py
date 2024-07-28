import os
import shutil
import fnmatch


def organize_downloads(downloads_path):
    # Define directories for different file types
    directories = {
        'images': 'Images',
        'documents': 'Documents',
        'videos': 'Videos',
        'music': 'Music',
        'others': 'Others'
    }

    # Create directories if they don't exist
    for dir_name in directories.values():
        dir_path = os.path.join(downloads_path, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Iterate over all files in the downloads directory
    for filename in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Determine the file type based on its extension
            for dir_name, ext_pattern in directories.items():
                if fnmatch.fnmatch(filename, f'*.{ext_pattern}'):
                    target_dir = directories[dir_name]
                    target_path = os.path.join(downloads_path, target_dir, filename)

                    # Move the file to the appropriate directory
                    shutil.move(file_path, target_path)
                    break
            else:
                # If no match was found, move the file to the 'Others' directory
                shutil.move(file_path, os.path.join(downloads_path, 'Others', filename))


# Example usage
downloads_folder_path = '/path/to/your/downloads/folder'
organize_downloads(downloads_folder_path)
