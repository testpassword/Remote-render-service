# Kulbako Artemy 2020 for Luxoft

import argparse
import subprocess
from datetime import datetime
import os
from os import path
import sys
import zipfile
from shutil import rmtree
import json


# Checks for the correctness of those arguments that the parser cannot check
def check_args(args):
    fp = args.input
    if not path.exists(fp):
        sys.exit("Input path " + fp + " didn't exist or denied")
    if not zipfile.is_zipfile(fp):
        sys.exit("Extension should be .zip")
    if args.output is None:
        args.output = path.dirname(fp)
    if not path.exists(args.output):
        sys.exit("Directory " + args.output + " didn't exist")


# Returns the first found blend scene in the directory, or throws an exception if none are present
def find_scene(dir):
    for file in os.listdir(dir):
        if file.endswith(".blend"):
            return os.path.join(dir, file)
    raise FileNotFoundError()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to .zip file")
    parser.add_argument("--output", help="Path to output directory")
    parser.add_argument("--width", type=int, default=1280, help="Resolution by X of result image",
                        choices=range(2, 15360))
    parser.add_argument("--height", type=int, default=720, help="Resolution by Y of result image",
                        choices=range(2, 15360))
    parser.add_argument("--format", default="JPEG", help="File format for render", choices=["JPEG", "PNG", "BMP"])
    parser.add_argument("--compress", type=int, default=0, choices=range(0, 101),
                        help="Compression ratio: 0 = no compression, 100 = max")
    parser.add_argument("--aa", default="FXAA", help="Use antialiasing: OFF, FXAA or SSAA ration 5, 8, 11, 16, 32",
                        choices=["OFF", "FXAA", "5", "8", "11", "16", "32"])
    args = parser.parse_args()
    check_args(args)
    tmp_dir = os.path.join(path.dirname(args.input), "render_tmp") # get the directory with the archive and create folder for temporary files inside
    os.mkdir(tmp_dir)
    try:
        with zipfile.ZipFile(args.input, "r") as archive:  # распаковывает архив в временную директорию
            archive.extractall(tmp_dir)
        scene = find_scene(tmp_dir)  # unpacks the archive into a temporary directory
        log_name = args.output + "/log" + datetime.now().strftime("%Y%m%d-%H-%M-%S.txt")
        image_name = args.output + "/image" + datetime.now().strftime("%Y%m%d-%H-%M-%S")  # give a name to the output file
        params = vars(args)  # form a map with render parameters
        params["output"] = image_name
        params["textures"] = path.dirname(scene)
        renderscript_path = os.getenv("bpr", "render.py") # get script path from env variable or from current directory
        command = ["blender", "--background", scene,
                   "--engine", "RPR",
                   "--python", renderscript_path,
                   "--", json.dumps(params)]
        # We call the blender process in the background, passing it the scene, render parameters and script.
        # The log is simultaneously output to the console and file.
        with open(log_name, "w", encoding="utf-8") as f:
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, encoding="utf-8")
            for line in proc.stdout:
                sys.stdout.write(line)
                f.write(line)
    except FileNotFoundError:
        sys.exit("Can't find .blend file in archive")
    finally:
        rmtree(tmp_dir)  # delete temporary files after ourselves


if __name__ == "__main__": main()
