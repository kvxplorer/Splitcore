import subprocess

def convert_ebook(i, o):
    subprocess.run(["ebook-convert", i, o])
