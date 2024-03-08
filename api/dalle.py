from openai import OpenAI
from dotenv import load_dotenv
import requests
import os
import zipfile
from flask import send_file

load_dotenv()
client = OpenAI()

# Replace spaces with underscores and convert to lowercase
def format_keyword(keyword):
    formatted_keyword = keyword.replace(" ", "_").lower()
    return formatted_keyword

# This function generates and saves an image with Dall-E 3
def dalle(keyword):
    text_before = "an abstract image of "
    text_after = ", vibrant colors"
    response = client.images.generate(
        model="dall-e-3",
        prompt=text_before + keyword + text_after,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    return response.data[0].url
        
# Generate and save multiple images with Dall-E 3
def dalle_images(keyword, num_images):
    formatted_keyword = format_keyword(keyword)
    # Create directory if it doesn't exist
    image_directory = os.path.join(os.getcwd(), "dalle", formatted_keyword)
    os.makedirs(image_directory, exist_ok=True)
    
    for i in range(1, num_images + 1):
        # Generate image URL
        image_url = dalle(keyword)
        
        # Generate the image filename with 4-digit format
        image_filename = f"{i:04d}.jpg"
        
        # Download and save the image
        image_path = os.path.join(image_directory, image_filename)
        with open(image_path, 'wb') as f:
            f.write(requests.get(image_url).content)
            
# Function to zip images and return the link to the ZIP file
def dalle_zip(keyword, num_images):
    formatted_keyword = format_keyword(keyword)
    dalle_images(keyword, num_images)
    image_directory = os.path.join(os.getcwd(), "dalle", formatted_keyword)
    zip_filename = f"{formatted_keyword}_dalle.zip"
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
