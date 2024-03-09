import base64
import os
import requests
from dotenv import load_dotenv
import zipfile
from flask import send_file

load_dotenv()

engine_id = "stable-diffusion-v1-6"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = os.getenv("STABILITY_API_KEY")

if api_key is None:
    raise Exception("Missing Stability API key.")

# Replace spaces with underscores and convert to lowercase
def format_keyword(keyword):
    formatted_keyword = keyword.replace(" ", "_").lower()
    return formatted_keyword

# This function generates images with Stability AI
def stability(keyword):
    text_before = "an abstract image of "
    text_after = ", vibrant colors"
    text_prompt = text_before + keyword + text_after

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": text_prompt
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    
    return data

# Generate and save multiple images with Stability AI
def stability_images(keyword, num_images):
    formatted_keyword = format_keyword(keyword)
    # Create directory if it doesn't exist
    stability_directory = os.path.join(os.getcwd(), "stability")
    os.makedirs(stability_directory, exist_ok=True)
    keyword_directory = os.path.join(stability_directory, format_keyword(keyword))
    os.makedirs(keyword_directory, exist_ok=True)
    
    generated_image_paths = []  # List to store paths of generated images
    
    for i in range(1, num_images + 1):
        # Generate stability data
        stability_data = stability(keyword)
        # Extract image data from stability data
        image_data = stability_data["artifacts"][0]["base64"]
        # Decode base64 image data and save the image
        image_path = os.path.join(keyword_directory, f"{i:04d}.jpg")
        with open(image_path, 'wb') as f:
            f.write(base64.b64decode(image_data))
        generated_image_paths.append(image_path)
    
    return generated_image_paths
            
def stability_zip(keyword, num_images):
    formatted_keyword = format_keyword(keyword)
    stability_images(keyword, num_images)
    image_directory = os.path.join(os.getcwd(), "stability", formatted_keyword)
    zip_filename = f"{formatted_keyword}_stability.zip"
    zip_folder = os.path.join(os.getcwd(), "ZIP")  # New folder for zip files
    os.makedirs(zip_folder, exist_ok=True)
    zip_path = os.path.join(zip_folder, zip_filename)  # Path to the zip file

    # Create a ZIP file and add images to it
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(image_directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, image_directory))

    # Return the path to the ZIP file
    return zip_path