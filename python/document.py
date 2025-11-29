import subprocess
import os

def convert_document(i, o):
    d = os.path.dirname(o) or "."
    subprocess.run(["libreoffice", "--headless", "--convert-to", o.split(".")[-1], i, "--outdir", d])
