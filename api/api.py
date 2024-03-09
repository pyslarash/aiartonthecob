from flask import request, jsonify
from stability import stability_images
from dalle import dalle_images
from description import description_creation
from zip import create_zip

# Test function
def hello():
    return 'Hi there!'

# Generating an X amount of Stability images
def stability():
    # Get the text prompt from the request
    keyword = request.json.get('keyword')
    num_images = request.json.get('num_images')

    if keyword is None or num_images is None:
        return jsonify({'error': 'Keyword and number of images are required'}), 400

    try:
        image_paths = stability_images(keyword, num_images)
        
        formatted_image_paths = image_paths
        
        # Send success response
        return jsonify({'image_paths': formatted_image_paths}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Generating an X amount of Dall-E images
def dalle():
    base_url = request.base_url  # Get the base URL of the current request
    backend_base_url = base_url.rsplit('/', 1)[0]  # Extract the backend base URL
    # Get the keyword and number of images from the request
    keyword = request.json.get('keyword')
    num_images = request.json.get('num_images')

    if keyword is None or num_images is None:
        return jsonify({'error': 'Keyword and number of images are required'}), 400

    try:
        # Generate and save the images based on the inputs
        image_paths = dalle_images(keyword, num_images)
        # Modify the image paths to include the backend base URL
        formatted_image_paths = image_paths
        # If there's a problem with correct linking, work with this:
        # formatted_image_paths = [f"{backend_base_url}/dalle/{image_path.split('api/dalle/')[1]}" for image_path in image_paths]
        # Send success response
        return jsonify({'image_paths': formatted_image_paths}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Generating a product description
def description():
    # Get the text prompt from the request
    keyword = request.json.get('keyword')

    if keyword is None:
        return jsonify({'error': 'Keyword is required'}), 400

    try:
        # Generate the description based on the keyword
        title, description, tags = description_creation(keyword)

        # Construct the JSON response with title, description, and tags
        response_data = {
            'title': title,
            'description': description,
            'tags': tags
        }

        # Return the JSON response
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Creating a ZIP file to download
def zip():
    # Get the list of image paths from the request data
    data = request.json
    image_paths = data.get('image_paths', [])

    # Check if the image_paths parameter is provided
    if not image_paths:
        return jsonify({'error': 'No image paths provided'}), 400

    # Create the ZIP file
    zip_file_path = create_zip(image_paths)

    # Return the path to the created ZIP file
    return jsonify({'zip_file_path': zip_file_path}), 200