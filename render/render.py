# Kulbako Artemy 2020 for Luxoft

import bpy
import sys
import os
from os import path
import json
import glob


def abs_filepath(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))


# Applies texture to materials if they have the same name
def apply_textures(materials, textures):
    for m in materials:
        for t in list(filter(lambda it: m.name == it, map(lambda it: path.basename(path.splitext(t)[0]), textures))):
            m.use_nodes = True
            bsdf = m.node_tree.nodes["Principled BSDF"]
            tex_image = m.node_tree.nodes.new('ShaderNodeTexImage')
            full_image_path = os.path.abspath(t)
            tex_image.image = bpy.data.images.load(full_image_path)
            m.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])


# Sets render parameters and launches it
def render():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]
    raw_params = json.loads(argv[0])
    textures = glob.glob(raw_params["textures"] + "/*.jpg")
    apply_textures(bpy.data.materials, textures)
    render_params = bpy.context.scene.render
    bpy.context.scene.display.render_aa = raw_params["aa"]
    render_params.image_settings.file_format = raw_params["format"]
    render_params.filepath = raw_params["output"]
    render_params.resolution_x = raw_params["width"]
    render_params.resolution_y = raw_params["height"]
    bpy.data.scenes["Scene"].render.image_settings.compression = int(raw_params["compress"])
    bpy.ops.render.render(write_still=True, use_viewport=True)


if __name__ == "__main__": render()
