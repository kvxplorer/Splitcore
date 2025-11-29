import subprocess

def convert_audio_video(i, o, q, b):
    c = ["ffmpeg", "-y", "-i", i]
    if q:
        if q == "high":
            c += ["-crf", "18"]
        elif q == "medium":
            c += ["-crf", "23"]
        elif q == "low":
            c += ["-crf", "30"]
    if b:
        c += ["-b:a", b]
    c.append(o)
    subprocess.run(c)
