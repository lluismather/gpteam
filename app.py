
from flask import Flask
import os
import logging
from dotenv import load_dotenv

from routes.web import web

# load environment variables
load_dotenv()

# set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create the Flask app
app = Flask(__name__)

# routes from routes/web.py
app.register_blueprint(web)

# run the app
if __name__ == '__main__':
    app.run(
        debug=os.getenv('APP_DEBUG', False),
    )
