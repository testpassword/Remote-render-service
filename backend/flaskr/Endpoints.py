# Kulbako Artemy 2020 for Luxoft

from flask import Flask, request, jsonify
import time
import json
from os import path
import os
from shutil import rmtree
from jenkinsapi.jenkins import Jenkins
import Utils

# configure app context
with open("../jen_config.json") as f:
    jenConf = json.load(f)
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = jenConf["UPLOAD_FOLDER"]


@app.route("/api/render", methods=["POST"])
def launchPipeline():
    try:
        absPath = Utils.uploadFile(request)
        PARAMETERS = {
            "INPUT_FILE": absPath,
            "WIDTH": request.form["WIDTH"],
            "HEIGHT": request.form["HEIGHT"],
            "FORMAT": request.form["FORMAT"],
            "COMPRESSION": request.form["COMPRESSION"],
            "ANTIALIASING_ALGORITHM": request.form["ANTIALIASING_ALGORITHM"]
        }
        jenServer = Jenkins(jenConf["URL"], jenConf["USERNAME"], jenConf["PASSWORD"], useCrumb=True)
        jenJob = jenServer[jenConf["PIPELINE"]]
        jenBuild = jenJob.invoke(block=True, build_params=PARAMETERS, securitytoken=jenConf["TOKEN"]).get_build()
        while jenBuild.is_running():
            time.sleep(5)
        artifacts = jenBuild.get_artifact_dict()
        artifactsNames = list(artifacts.keys())
        for it in artifacts.values():
            it.save_to_dir(app.config["UPLOAD_FOLDER"])
        encodedImg = Utils.encodeImage(path.join(app.config["UPLOAD_FOLDER"], artifactsNames[0]))
        logText = open(path.join(app.config["UPLOAD_FOLDER"], artifactsNames[1]), "r", encoding="utf-8").readlines()
        response = {
            "log": logText,
            "img": encodedImg
        }
        return jsonify(response)
    finally:
        servDir = app.config["UPLOAD_FOLDER"]
        rmtree(servDir)  # because rmtree removes the directory in the end of arg path, remake it
        os.mkdir(servDir)


if __name__ == "__main__":
    app.run(debug=True)
