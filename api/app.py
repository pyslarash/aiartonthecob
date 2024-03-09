from flask import Flask
from flask_cors import CORS
from api import stability, dalle, description, hello, zip

# Create a Flask application
app = Flask(__name__)
CORS(app)

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

if __name__ == '__main__':
    app.run(debug=True)