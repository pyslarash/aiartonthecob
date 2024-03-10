from flask import Flask
from flask_cors import CORS
from api import stability, dalle, description, hello, zip, mockups, handle_image_upload

# Create a Flask application
app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

# Define routes for the API endpoints
@app.route('/hello')
def hello_endpoint():
    return hello()

@app.route('/stability', methods=['POST'])
def stability_endpoint():
    return stability()

@app.route('/dalle', methods=['POST'])
def dalle_endpoint():
    return dalle()

@app.route('/description', methods=['POST'])
def description_endpoint():
    return description()

@app.route('/zip', methods=['POST'])
def zip_endpoint():
    return zip()

@app.route('/mockups', methods=['POST'])
def mockups_endpoint():
    return mockups()

@app.route('/upload_image', methods=['POST'])
def upload_image_endpoint():
    return handle_image_upload()

if __name__ == '__main__':
    app.run(debug=True)