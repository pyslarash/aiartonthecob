import os

def upload_image(file):
    try:
        # Ensure the 'mockup_upload_pics' directory exists
        upload_folder = 'mockup_upload_pics'
        os.makedirs(upload_folder, exist_ok=True)
        
        # Save the file to the 'mockup_upload_pics' directory
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        
        return file_path
    except Exception as e:
        return str(e)