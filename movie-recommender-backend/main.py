from flask import Flask
from flask_cors import CORS
from app.routes import register_routes
import logging

logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

register_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    logger.info("Flask app started!")
