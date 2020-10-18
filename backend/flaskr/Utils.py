# Kulbako Artemy 2020 for Luxoft

import base64
from PIL import Image
from io import BytesIO
from werkzeug.utils import secure_filename
from os import path
from flask import current_app


# upload file to server temporary folder
def uploadFile(req):
    rawFile = req.files["INPUT_FILE"]
    filename = secure_filename(rawFile.filename)
    absPath = path.join(current_app.config["UPLOAD_FOLDER"], filename)
    rawFile.save(absPath)
    return absPath.replace("\\", "/")  # normalize string to compatibility on Unix and Windows


# encode image to base64 string representation
def encodeImage(imagePath):
    with open(imagePath, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")