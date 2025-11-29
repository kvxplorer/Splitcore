import subprocess

def convert_font(i, o):
    subprocess.run(["fonttools", "ttx", "-o", o, i])
