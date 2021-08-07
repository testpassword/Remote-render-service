# Kulbako Artemy 2020 for Luxoft

from flask import Flask, request, jsonify
import time
import json
from os import path
import os
from shutil import rmtree
from jenkinsapi.jenkins import Jenkins
import utils

# configure app context
with open("../jen_config.json") as f:
    jenConf = json.load(f)
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = jenConf["UPLOAD_FOLDER"]


@app.route("/api/render", methods=["POST"])
def launch_pipeline():
    try:
        params = {
            "INPUT_FILE": utils.upload_file(request),
            "WIDTH": request.form["WIDTH"],
            "HEIGHT": request.form["HEIGHT"],
            "FORMAT": request.form["FORMAT"],
            "COMPRESSION": request.form["COMPRESSION"],
            "ANTIALIASING_ALGORITHM": request.form["ANTIALIASING_ALGORITHM"]
        }
        jen_server = Jenkins(jenConf["URL"], jenConf["USERNAME"], jenConf["PASSWORD"], useCrumb=True)
        jen_job = jen_server[jenConf["PIPELINE"]]
        jen_build = jen_job.invoke(block=True, build_params=params, securitytoken=jenConf["TOKEN"]).get_build()
        while jen_build.is_running():
            time.sleep(5)
        artifacts = jen_build.get_artifact_dict()
        artifacts_names = list(artifacts.keys())
        for it in artifacts.values():
            it.save_to_dir(app.config["UPLOAD_FOLDER"])
        return jsonify({
            "log": open(path.join(app.config["UPLOAD_FOLDER"], artifacts_names[1]), "r", encoding="utf-8").readlines(),
            "img": utils.encode_image(path.join(app.config["UPLOAD_FOLDER"], artifacts_names[0]))
        })
    finally:
        serv_dir = app.config["UPLOAD_FOLDER"]
        rmtree(serv_dir)  # because rmtree removes the directory in the end of arg path, remake it
        os.mkdir(serv_dir)


if __name__ == "__main__":
    app.run(debug=True)
