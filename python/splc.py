import argparse
import os
import magic
from router import route_conversion

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--to", required=True)
    parser.add_argument("--quality", default=None)
    parser.add_argument("--bitrate", default=None)
    args = parser.parse_args()

    i = args.input
    t = args.to
    q = args.quality
    b = args.bitrate

    if not os.path.isfile(i):
        print("File not found")
        return

    mime = magic.from_file(i, mime=True)
    o = os.path.splitext(i)[0] + "." + t

    route_conversion(i, o, t, mime, q, b)
    print(o)

if __name__ == "__main__":
    main()
