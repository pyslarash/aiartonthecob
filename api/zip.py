from zipfile import ZipFile
import os

def create_zip(image_paths):
    # Create a directory for storing the ZIP file
    zip_dir = 'ZIP'
    os.makedirs(zip_dir, exist_ok=True)

    # Extract the folder name from the first image path
    first_image_path = image_paths[0]
    folder_name = os.path.basename(os.path.dirname(first_image_path))

    # Define the base name for the ZIP file
    base_zip_name = folder_name

    # Check if a ZIP file with the base name already exists
    zip_file_path = os.path.join(zip_dir, f'{base_zip_name}.zip')
    if os.path.exists(zip_file_path):
        # If the ZIP file already exists, add a number suffix to the base name
        count = 1
        while True:
            zip_file_path = os.path.join(zip_dir, f'{base_zip_name}_{count}.zip')
            if not os.path.exists(zip_file_path):
                break
            count += 1

    # Create a new ZIP file and add each image to it
    with ZipFile(zip_file_path, 'w') as zipf:
        for index, image_path in enumerate(image_paths):
            # Check if the image exists
            if os.path.exists(image_path):
                # Add the image to the ZIP file with a unique name
                zipf.write(image_path, os.path.basename(image_path))

    return zip_file_path