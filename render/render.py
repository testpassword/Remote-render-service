# Kulbako Artemy 2020 for Luxoft

import bpy
import sys
import os
from os import path
import json
import glob


def absoluteFilePaths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


# Applies texture to materials if they have the same name
def applyTextures(materials, textures):
    for m in materials:
        for t in textures:
            fileName = path.basename(path.splitext(t)[0])
            if m.name == fileName:
                m.use_nodes = True
                bsdf = m.node_tree.nodes["Principled BSDF"]
                texImage = m.node_tree.nodes.new('ShaderNodeTexImage')
                fullImagePath = os.path.abspath(t)
                print(fullImagePath)
                texImage.image = bpy.data.images.load(fullImagePath)
                m.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])


# Sets render parameters and launches it
def render():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]
    params = json.loads(argv[0])
    textures = glob.glob(params["textures"] + "/*.jpg")
    applyTextures(bpy.data.materials, textures)
    renderParams = bpy.context.scene.render
    bpy.context.scene.display.render_aa = params["aa"]
    renderParams.image_settings.file_format = params["format"]
    renderParams.filepath = params["output"]
    renderParams.resolution_x = params["width"]
    renderParams.resolution_y = params["height"]
    bpy.data.scenes["Scene"].render.image_settings.compression = int(params["compress"])
    bpy.ops.render.render(write_still=True, use_viewport=True)


if __name__ == "__main__": render()
