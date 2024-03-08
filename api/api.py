from flask import request, jsonify
from stability import stability_zip
from dalle import dalle_zip
from description import description_creation

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
        zip_path = stability_zip(keyword, num_images)
        # Send success response
        return jsonify({'message': f"{num_images} images generated successfully for keyword '{keyword}'",
                        'zip_file': zip_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Generating an X amount of Dall-E images
def dalle():
    # Get the keyword and number of images from the request
    keyword = request.json.get('keyword')
    num_images = request.json.get('num_images')

    if keyword is None or num_images is None:
        return jsonify({'error': 'Keyword and number of images are required'}), 400

    try:
        # Generate and save the images based on the inputs
        zip_path = dalle_zip(keyword, num_images)
        # Send success response
        return jsonify({'message': f"{num_images} images generated successfully for keyword '{keyword}'",
                        'zip_file': zip_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Generating a product description
def description():
    # Get the text prompt from the request
    keyword = request.json.get('keyword')

    if keyword is None:
        return jsonify({'error': 'Keyword is required'}), 400

    try:
        # Generate the image based on the text prompt
        description_path = description_creation(keyword)

        # Send the image path as a response
        return jsonify({'description_path': description_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500