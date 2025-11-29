import subprocess

def convert_vector(i, o):
    subprocess.run(["inkscape", i, "--export-filename", o])
