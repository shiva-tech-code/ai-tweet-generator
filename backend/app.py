import os
import sys
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

# Import blueprints
from routes.tweets_routes import tweets_bp

# Create Flask app
app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# Enable CORS with specific settings
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Register blueprints
app.register_blueprint(tweets_bp, url_prefix='/api')

# Serve frontend
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    port = int(os.getenv('SERVER_PORT', 8888))
    print(f"🚀 Starting server on port {port}")
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
