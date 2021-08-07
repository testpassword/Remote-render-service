# Kulbako Artemy 2020 for Luxoft

import base64
from PIL import Image
from io import BytesIO
from werkzeug.utils import secure_filename
from os import path
from flask import current_app


# upload file to server temporary folder
def upload_file(req):
    raw_file = req.files["INPUT_FILE"]
    filename = secure_filename(raw_file.filename)
    abs_path = path.join(current_app.config["UPLOAD_FOLDER"], filename)
    raw_file.save(abs_path)
    return abs_path.replace("\\", "/")  # normalize string to compatibility on Unix and Windows


# encode image to base64 string representation
def encode_image(imagePath):
    with open(imagePath, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")