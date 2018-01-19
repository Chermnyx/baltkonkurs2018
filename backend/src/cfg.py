import os
from pathlib import Path

from flask import Flask

app = Flask(__name__)
debug = 'APP_RELEASE' not in os.environ
chunk = 1024 * 1024 * 4

if debug:
    app.debug = True

p = Path(__file__).parent
keras_model_path = p / 'neural' / 'model.h5'
