from flask import Flask
from api import stability, dalle, description, hello

# Create a Flask application
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)