from tempfile import NamedTemporaryFile

from flask import jsonify, request

from . import cfg, neural
from .cfg import app


@app.route('/api/processImages', methods=['POST'])
def processImage():
    results = {}

    for name, uploaded_image in request.files.items():
        if not uploaded_image.mimetype.startswith('image/'):
            continue

        with NamedTemporaryFile() as file:
            for b in iter(lambda: uploaded_image.read(cfg.chunk), b''):
                file.write(b)
            try:
                result = float(neural.predict_image(file.name))
            except:
                continue
        results[name] = result

    return jsonify(results)
