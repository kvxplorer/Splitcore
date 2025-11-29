import subprocess

def convert_image(i, o):
    subprocess.run(["magick", i, o])
