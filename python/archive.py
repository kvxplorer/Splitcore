import subprocess

def convert_archive(i, o):
    subprocess.run(["7z", "x", i, "-o", "splc_tmp"])
    subprocess.run(["7z", "a", o, "splc_tmp"])
